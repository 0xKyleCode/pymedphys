import abc
from typing import Type

import pydicom
from pyvic.util.data_structures import NDVoxelArray


class PythonAutoDicom(abc.ABC):
    def __init__(self, pydicom_obj):
        self._pydicom_obj = pydicom_obj


class PythonFileAutoDicom(PythonAutoDicom):
    def __init__(self, file_name: str, verbose=True):
        self.file_name = file_name

        self._verbose = verbose

        if verbose:
            print("Loading DICOM file %s" % file_name)

        super().__init__(
            pydicom_obj=pydicom.read_file(file_name, stop_before_pixels=True)
        )

    @property
    @abc.abstractmethod
    def description(self) -> str:
        """Description of dicom files used to create autodicom code"""

    def save_as(self, filename):
        # if SOP instance UID is not set, generate one
        if (0x0008, 0x0018) in self._pydicom_obj:
            self._pydicom_obj[0x0008, 0x0018].value = pydicom.uid.generate_uid()

        self._pydicom_obj.save_as(filename)


class PythonImageFileAutoDicom(PythonFileAutoDicom):
    def __init__(self, file_name: str, verbose=True):
        self._image_ndarray = None
        super().__init__(file_name=file_name, verbose=verbose)

    def calculate_dimensions(self):
        raise NotImplementedError()

    def get_image(self):
        raise NotImplementedError()

    def _load_pixel_array(self, force_load_image=False):
        if (not hasattr(self._pydicom_obj, "pixel_array")) or force_load_image:
            self._pydicom_obj = pydicom.read_file(
                self.file_name, stop_before_pixels=False
            )

        return self._pydicom_obj.pixel_array

    def _get_ndimage(self, force_load_image=False) -> NDVoxelArray:
        if self._image_ndarray is None or force_load_image:
            print("Loading DICOM image for %s" % self.file_name)
            image_data = self._load_pixel_array(force_load_image=force_load_image)

            origin, dims = self.calculate_dimensions()

            self._image_ndarray = NDVoxelArray(image_data, origin=origin, voxdims=dims)

        return self._image_ndarray


class AutoDicomSequence(list):
    def __init__(
        self, dicom_sequence: pydicom.Sequence, autodicom_type: Type[PythonAutoDicom]
    ):
        super().__init__(autodicom_type(s) for s in dicom_sequence)
        self._sequence = dicom_sequence
        self.autodicom_type = autodicom_type

    def __get_item__(self, index):
        return super().__getitem__(index)

    def __setitem__(self, index, value):
        assert issubclass(value.__class__, self.autodicom_type) or isinstance(
            value, self.autodicom_type
        )
        super().__set_item__(index, value)
        self._sequence.__setitem__(index, value._pydicom_obj)

    def append(self, value):
        assert isinstance(value, self.autodicom_type) or issubclass(
            value.__class__, self.autodicom_type
        )
        super().append(value)
        self._sequence.append(value._pydicom_obj)

    def extend(self, values):
        assert all(
            [
                (
                    issubclass(s.__class__, self.autodicom_type)
                    or isinstance(s, self.autodicom_type)
                )
                for s in values
            ]
        )
        super().extend([s for s in values])
        self._sequence.extend([s._pydicom_obj for s in values])

    def insert(self, __index, __object) -> None:
        assert issubclass(__object.__class__, self.autodicom_type) or isinstance(
            __object, self.autodicom_type
        )
        super().insert(__index, __object)
        self._sequence.insert(__index, __object._pydicom_obj)

    def remove(self, value):
        assert issubclass(value.__class__, self.autodicom_type) or isinstance(
            value, self.autodicom_type
        )
        to_rm = next((s for s in self if s._pydicom_obj == value._pydicom_obj), None)
        super().remove(to_rm)
        self._sequence.remove(value._pydicom_obj)

    def clear(self) -> None:
        super().clear()
        self._sequence.clear()

    def sort(self, *args, **kwargs):
        super().sort(*args, **kwargs)
        self._sequence.sort(*args, **kwargs)


class PythonDicomClassMakerV2:
    CASTING_DICOM_TO_PYTHON_DICT = {"DS": "float(%s)", "DSfloat": "float(%s)"}

    CASTING_PYTHON_TO_DICOM_DICT = {"DS": "str(%s)", "DSfloat": "str(%s)"}

    import logging

    _logger = logging.getLogger(__name__)
    _logger.setLevel(logging.INFO)

    def __init__(
        self,
        dicom_file_object_list,
        class_name,
        description,
        base_prefix=None,
        base_suffix="AutoDicom",
        has_image=True,
    ):
        import pydicom

        dicom_handles = dicom_file_object_list  # [pydicom.read_file(df, stop_before_pixels=True) for df in dicom_file_list]
        # check all class id's match

        assert description != ""
        assert description != None

        self.base_suffix = base_suffix
        self.base_prefix = base_prefix
        self.description = description
        self.has_image = has_image

        if dicom_handles[0].__class__ == pydicom.dataset.FileDataset:
            self.toplevel = True

            class_id_tag = pydicom.tag.Tag("0008", "0016")

            assert all(
                [
                    s[class_id_tag].value.name
                    == dicom_handles[0][class_id_tag].value.name
                    for s in dicom_handles
                ]
            )

            # check if file has pixel data tag

        else:
            self.toplevel = False
            self.has_image = False

        if class_name is None:
            class_id_tag = pydicom.tag.Tag("0008", "0016")
            class_name = dicom_handles[0][class_id_tag].value.name

        if self.toplevel:
            self.class_name = class_name + self.base_suffix
        else:
            self.class_name = self.base_prefix + class_name + self.base_suffix

        self.tag_list = {
            (self.dicom_to_pep(s.name), s.tag, s.VR)
            for dh in dicom_handles
            for s in dh
            if s.value.__class__ != pydicom.sequence.Sequence
        }

        self.sequence_list = {
            (s.name, s.tag)
            for dh in dicom_handles
            for s in dh
            if s.value.__class__ == pydicom.sequence.Sequence
        }

        duplicate_tags = []
        for tag_name, tag_val, tag_type in self.tag_list:
            for tag_name1, tag_val1, tag_type1 in self.tag_list:
                if tag_name == tag_name1 and tag_val != tag_val1:
                    duplicate_tags.append((tag_name, tag_val, tag_type))
                    self._logger.warning(
                        "found duplicate tags with different addresses -- thanks dicom 'standard' -- discarding tags %s [%s != %s]"
                        % (tag_name, tag_val, tag_val1)
                    )

        for dup_tag in duplicate_tags:
            self.tag_list.remove(dup_tag)

        if len(self.sequence_list) > 0:
            self._logger.info(
                "found %s sub-sequences %s"
                % (
                    len(self.sequence_list),
                    [s[0] for s in self.sequence_list].__str__(),
                )
            )

        assert len({s[0] for s in self.tag_list}) == len(self.tag_list)

        self.sub_class_makers = []

        for name, tag in self.sequence_list:
            obj_seq_list = [s[tag].value for s in dicom_file_object_list if tag in s]

            obj_list = []
            for obj_seq in obj_seq_list:
                for obj in obj_seq:
                    obj_list.append(obj)

            self.sub_class_makers.append(
                PythonDicomClassMakerV2(
                    obj_list,
                    description="AutoDicom inner class of %s" % self.class_name,
                    base_suffix=base_suffix,
                    base_prefix=self.base_prefix,
                    class_name=self._sequence_item_name(name),
                    has_image=False,
                )
            )

    @property
    def base_name(self):
        return self.class_name + self.base_suffix

    def base_class_def_string(self):
        outstr = ""

        if self.toplevel and self.has_image:
            outstr += "class %s(PythonImageFileAutoDicom):\n" % self.class_name
        elif self.toplevel:
            outstr += "class %s(PythonFileAutoDicom):\n" % self.class_name
        else:
            outstr += "class %s(PythonAutoDicom):\n" % self.class_name

        return outstr

    # def copy_str(self):
    #
    #     import textwrap
    #     to_str = '''
    #         def deepcopy(self):
    #             new_copy = self.__class__(self._pydicom_obj.copy())\
    #         '''
    #     for seq_name, tag in self.sequence_list:
    #         full_name = "%s%s%s" % (self.base_prefix, self._sequence_item_name(seq_name), self.base_suffix)
    #         prop_name = self.dicom_to_pep(seq_name)
    #         to_str += '''
    #             %s = Sequence([ s.deepcopy()._pydicom_obj for s in self.%s])\
    #         ''' % (self._tag_to_evalstr(tag), prop_name)
    #
    #     to_str += '''
    #             return new_copy
    #         '''
    #
    #
    #     return textwrap.indent(textwrap.dedent(to_str),'\t')

    def base_constructor_string(self):
        to_str = '\tdescription = "%s"\n' % self.description

        # if self.toplevel:
        #     to_str += "\tdef __init__(self, file_name, stop_before_pixels=True): \n"
        #     to_str += '\t\t"""\n\t\t :rtype: %s\n\t\t"""\n' % self.class_name
        #     to_str += '\t\tsuper().__init__(file_name)\n'

        # to_str += "\t\tself._pydicom_obj =  pydicom.read_file(file_name,stop_before_pixels=stop_before_pixels)\n\n" \
        #           "\t\tself.file_name = file_name\n\n"

        # else:
        #     to_str += "\tdef __init__(self, pydicom_obj): \n" \
        #               "\t\tsuper().__init__(pydicom_obj)\n"
        #
        #               # "\t\tself._pydicom_obj = pydicom_obj\n\n"

        for name, val, ttype in self.tag_list:
            to_str += "\t@property\n"
            to_str += "\tdef %s(self):\n" % name

            try:
                type_cast_str = self.CASTING_DICOM_TO_PYTHON_DICT[ttype]
            except KeyError:
                type_cast_str = "%s"

            valstr = "self._pydicom_obj[%s].value" % self._tag_to_defstr(val)

            to_str += "\t\tif (%s) in self._pydicom_obj:\n" % self._tag_to_defstr(val)
            # to_str += "\t\t\tval = %s\n" % self._tag_to_evalstr(val)
            to_str += "\t\t\tif (isinstance(%s, BaseTag)):\n" % valstr
            to_str += "\t\t\t\treturn %s\n" % valstr
            to_str += "\t\t\telif (isinstance(%s, MultiValue)):\n" % valstr
            to_str += "\t\t\t\treturn [{} for s in {}]\n".format(
                type_cast_str % "s",
                valstr,
            )
            to_str += "\t\t\telse:\n"
            to_str += "\t\t\t\treturn %s\n" % (type_cast_str % valstr)
            to_str += "\t\telse:\n"
            to_str += "\t\t\treturn None\n\n"

            # UPDATE
            to_str += "\t@%s.setter\n" % name
            to_str += "\tdef %s(self, value):\n" % name
            to_str += "\t\t%s = value\n\n" % valstr

        for seq_name, tag in self.sequence_list:
            full_name = "{}{}{}".format(
                self.base_prefix,
                self._sequence_item_name(seq_name),
                self.base_suffix,
            )
            to_str += "\t@property\n"
            to_str += "\tdef {}(self) -> List[{}]:\n".format(
                self.dicom_to_pep(seq_name),
                full_name,
            )

            to_str += "\t\tval = %s\n" % self._tag_to_evalstr(tag)

            to_str += "\t\tif val=='None' or val is None:\n"
            to_str += "\t\t\treturn None\n"
            to_str += "\t\telse:\n"
            # to_str += "\t\t\treturn [%s%s%s(s) for s in val]\n" % (
            # self.base_prefix, self._sequence_item_name(seq_name), self.base_suffix)

            # UPDATE
            to_str += "\t\t\treturn AutoDicomSequence(val, %s)\n\n" % (full_name)

        AutoDicomSequence
        # else:
        #     if len(self.sequence_list) > 0:
        #         to_str += '\t\t"""\n'
        #         for name, val in self.sequence_list:
        #             to_str += "\t\t:type %s: list of %s%s\n" % (
        #             self.dicom_to_pep(name), self._sequence_item_name(name), self.base_suffix)
        #         to_str += '\t\t"""\n\n'
        #
        #     for name, val, ttype in self.tag_list:
        #         to_str += "\t\tself.%s = %s\n" % (name, name)
        #     for name, val in self.sequence_list:
        #         to_str += "\t\tself.%s = %s or []\n" % (self.dicom_to_pep(name), self.dicom_to_pep(name))
        #
        #     if self.has_pixel_array:
        #         to_str += "\t\tself.pixel_array = pixel_array\n"
        #     to_str += "\t\tself.file_name = file_name\n"

        return to_str + "\n"

    def from_pydicom_method_str(self):
        to_str = "\t@classmethod\n"
        to_str += "\tdef from_pydicom_obj(cls,pydicom_obj):\n"

        if not self.toplevel:
            to_str += '\t\t""":rtype: %s"""\n' % self.base_name
        else:
            to_str += '\t\t""":rtype: %s"""\n' % self.class_name

        to_str += "\t\tfrom pydicom.tag import BaseTag\n"
        to_str += "\t\tfrom pydicom.multival import MultiValue\n"

        to_str += "\t\tfrom pydicom.multival import MultiValue\n"

        for name, val, ttype in self.tag_list:
            try:
                type_cast_str = self.CASTING_DICOM_TO_PYTHON_DICT[ttype]
            except KeyError:
                type_cast_str = "%s"

            to_str += "\t\tif (%s) in pydicom_obj:\n" % (self._tag_to_defstr(val))
            to_str += "\t\t\tval = %s\n" % self._tag_to_evalstr(val)
            to_str += "\t\t\tif (val is None or val=='NONE'):\n"
            to_str += "\t\t\t\t%s = None\n" % (name)
            to_str += "\t\t\telif (isinstance(val, BaseTag)):\n"
            to_str += "\t\t\t\t%s = val\n" % (name)
            to_str += "\t\t\telif (isinstance(val, MultiValue)):\n"
            to_str += "\t\t\t\t{} = [{} for s in val]\n".format(
                name, type_cast_str % "s"
            )
            to_str += "\t\t\telse:\n"
            to_str += "\t\t\t\t{} = {}\n".format(name, type_cast_str % "val")
            to_str += "\t\telse:\n"
            to_str += "\t\t\t%s = None\n" % (name)

        for seq_name, tag in self.sequence_list:
            to_str += "\t\tval = %s\n" % self._tag_to_evalstr(tag)
            to_str += (
                "\t\t%s = None if val=='NONE' else [%s%s.from_pydicom_obj(s) for s in val]\n"
                % (
                    self.dicom_to_pep(seq_name),
                    self._sequence_item_name(seq_name),
                    self.base_suffix,
                )
            )

        if self.has_pixel_array:
            to_str += "\t\ttry:\n"
            to_str += "\t\t\tpixel_array = pydicom_obj.pixel_array\n"
            to_str += "\t\texcept: \n"
            to_str += "\t\t\tpixel_array = None\n"

        to_str += "\n"
        to_str += "\t\treturn cls(\n"
        for name, val, ttype in self.tag_list:
            to_str += "\t\t\t {}={},\n".format(name, name)
        for name, val in self.sequence_list:
            to_str += "\t\t\t {}={},\n".format(
                self.dicom_to_pep(name),
                self.dicom_to_pep(name),
            )
        if self.has_pixel_array:
            to_str += "\t\t\t pixel_array=pixel_array,\n"
        to_str = to_str[0:-2] + ")\n"

        return to_str

    def to_pydicom_method_str(self):
        to_str = "\tdef to_pydicom_obj(self):\n"

        if not self.toplevel:
            to_str += '\t\t""":rtype: pydicom.dataset.FileDataSet"""\n'
        else:
            to_str += '\t\t""":rtype: pydicom.dataset.DataSet"""\n'

        to_str += "\t\timport pydicom\n"
        to_str += "\t\tfrom pydicom.dataset import Tag\n"
        to_str += "\t\tfrom pydicom.dataset import Dataset\n"
        to_str += "\t\tfrom pydicom.dataset import DataElement\n"
        to_str += "\t\tfrom pydicom.sequence import Sequence\n"
        to_str += "\t\tpydicom_obj = pydicom.dataset.Dataset()\n"

        for name, val, ttype in self.tag_list:
            to_str += (
                "\t\tpydicom_obj[%s] = DataElement( Tag((%s)), '%s', self.%s)\n"
                % (self._tag_to_defstr(val), self._tag_to_defstr(val), ttype, name)
            )

        for seq_name, tag in self.sequence_list:
            to_str += (
                "\t\tpydicom_obj[%s] = DataElement( Tag((%s)), 'SQ', Sequence([s.to_pydicom_obj() for s in self.%s]))\n"
                % (
                    self._tag_to_defstr(tag),
                    self._tag_to_defstr(tag),
                    self.dicom_to_pep(seq_name),
                )
            )
        #     to_str += "\t\ttry:\n"
        #     to_str += "\t\t\tval = %s\n" % self._tag_to_evalstr(tag)
        #     to_str += "\t\t\t%s = None if val=='NONE' else Sequence([%s%s.to_pydicom_obj() for s in val])\n" % (self.dicom_to_pep(seq_name),self._sequence_item_name(seq_name),self.base_suffix)
        #     to_str += "\t\texcept KeyError: \n"
        #     to_str += "\t\t\t%s = None\n" % self.dicom_to_pep(seq_name)

        to_str += "\n"
        to_str += "\t\treturn pydicom_obj\n"

        return to_str

    def to_str_str(self):
        to_str = "\tdef __str__(self):\n"
        to_str += "\t\tto_ret_str = ''\n"
        for name, val, ttype in self.tag_list:
            to_str += "\t\tto_ret_str += '{}: %s\\n'%(self.{})\n".format(name, name)
        for seq_name, val in self.sequence_list:
            to_str += "\t\tto_ret_str += '{}: %s\\n'%(self.{})\n".format(
                self.dicom_to_pep(seq_name),
                self.dicom_to_pep(seq_name),
            )

        to_str += "\t\treturn to_ret_str\n"
        return to_str

    def base_class_str(self):
        to_str = ""

        if self.toplevel:
            to_str += "from __future__ import annotations\n"
            to_str += "from typing import List\n"
            to_str += "from pydicom.sequence import Sequence\n"
            to_str += "from pydicom.tag import BaseTag\n"
            to_str += "from pydicom.multival import MultiValue\n"
            to_str += "from pydose.utils.dicom import PythonFileAutoDicom, PythonAutoDicom, PythonImageFileAutoDicom, AutoDicomSequence\n"
            to_str += "\n"

        to_str += self.base_class_def_string()
        to_str += self.base_constructor_string() + "\n"

        # to_str += self.from_pydicom_method_str()
        # to_str += self.to_pydicom_method_str()
        to_str += self.to_str_str()
        # to_str += self.copy_str()

        if self.toplevel:
            to_str += "\n" + self.dicom_file_factory_str() + "\n"

        for maker in self.sub_class_makers:
            to_str += maker.base_class_str() + "\n"

        return to_str

    def whole_class_str(self):
        return self.base_class_str()

    def dicom_file_factory_str(self):
        to_str = "\t@classmethod\n"
        to_str += "\tdef from_dicom_file(cls, path, stop_before_pixels=False):\n"
        to_str += '\t\t"""\n\t\t :rtype: %s\n\t\t"""\n' % self.class_name
        to_str += "\t\ttry:\n"
        to_str += "\t\t\timport dicom as pydicom\n"
        to_str += "\t\texcept ImportError:\n"
        to_str += "\t\t\timport pydicom\n"
        to_str += "\t\tdcm_hand = pydicom.read_file(path,stop_before_pixels=stop_before_pixels)\n"
        to_str += "\t\tto_ret = cls(dcm_hand, path)\n"
        # to_str += "\t\tto_ret.file_name = path\n"
        # to_str += "\t\tif hasattr(dcm_hand, 'PixelData') and dcm_hand.PixelData is not None:\n"
        # to_str += "\t\t\tto_ret.pixel_data = dcm_hand.PixelData\n"
        to_str += "\t\treturn to_ret\n"
        return to_str

    @classmethod
    def _tag_to_evalstr(cls, tag):
        key1 = "0x{:04x}".format(tag.group)
        key2 = "0x{:04x}".format(tag.element)
        return "self._pydicom_obj[{},{}].value".format(key1, key2)

    @classmethod
    def _tag_to_VRstr(cls, tag):
        key1 = "0x{:04x}".format(tag.group)
        key2 = "0x{:04x}".format(tag.element)
        return "self._pydicom_obj[{},{}].VR".format(key1, key2)

    @classmethod
    def _tag_to_defstr(cls, tag):
        key1 = "0x{:04x}".format(tag.group)
        key2 = "0x{:04x}".format(tag.element)
        return "{},{}".format(key1, key2)

    @classmethod
    def dicom_to_pep(cls, dicom_str):
        return cls.python_sanitize_str(dicom_str.lower().replace(" ", "_"))

    @classmethod
    def python_sanitize_str(cls, string_to_sanitize):
        danger_chars = ["(", ")", "[", "]", "'", ".", " ", "-", "/"]

        for c in danger_chars:
            string_to_sanitize = string_to_sanitize.replace(c, "")

        return string_to_sanitize

    @classmethod
    def _sequence_item_name(cls, sequence_name):
        sanitized = cls.python_sanitize_str(sequence_name)
        sanitized = sanitized.replace("Sequence", "")

        return sanitized  # sanitized.replace('Set', '')

    def write_to_file(self, path, overwrite=False):
        if overwrite:
            method = "w"
        else:
            method = "a"

        with open(path, method) as fh:
            fh.write(self.whole_class_str().replace("\t", "    "))

    @classmethod
    def from_dicom_file_list(
        cls,
        dicom_file_list,
        base_prefix,
        description,
        base_suffix="AutoDicom",
        has_image=True,
    ):
        try:
            import dicom as pydicom
        except ImportError:
            import pydicom

        return cls(
            [pydicom.read_file(df, stop_before_pixels=True) for df in dicom_file_list],
            base_prefix,
            description=description,
            base_suffix=base_suffix,
            base_prefix=base_prefix,
            has_image=has_image,
        )
