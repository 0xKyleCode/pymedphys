import math
from abc import ABC, abstractmethod

from typing import Dict

from pyvic.util.data_structures import NDVoxelArray
from pyvic.util.file import list_files_by_wildcard
from pyvic.util.dicom import PythonFileAutoDicom

from vic_pydicom.autodicom.kv_obi_image_autodicom import KVOBIImageAutoDicom
from vic_pydicom.autodicom.mv_epid_image_autodicom import MVEPIDImageAutoDicom
from vic_pydicom.autodicom.vic_ct_image_slice_autodicom import VICCTImageSliceAutoDicom
from vic_pydicom.autodicom.vic_dose_autodicom import VICDoseAutoDicom
from vic_pydicom.autodicom.vic_qaplan_autodicom import VICQAPlanAutoDicom
from vic_pydicom.autodicom.vic_rt_structure_autodicom import VICRTStructureAutoDicom
from vic_pydicom.autodicom.vic_eclipse_plan_write_autodicom import (
    VICRTPlanAutoDicom,
    VICRTPlanBeamAutoDicom,
    VICRTPlanFractionGroupAutoDicom,
    VICRTPlanPatientSetupAutoDicom,
    VICRTPlanReferencedBeamAutoDicom,
)


from pyvic.rt.geometry import BeamAperture


# ODF = TypeVar('ODF', bound=PythonFileAutoDicom) # Original DICOM file
# PDF = TypeVar('PDF', bound=List[PythonFileAutoDicom]) # list of DICOM to pair
# PAIR_WC_LIST = TypeVar('PAIR_WC_LIST', bound=List[str]) # list of file wildcards to match pairs


class PairedDicomFile(ABC):
    AUTOLOAD_PAIRED_FILES = True

    def __init__(
        self,
        *args,
        find_paired_files=True,
        autoload_paired_files=AUTOLOAD_PAIRED_FILES,
        **kwargs
    ):
        super().__init__(*args, **kwargs)

        assert issubclass(self.PAIRING_TYPE, PythonFileAutoDicom)

        if not hasattr(self, "paired_files"):
            self.paired_files = {}
            self._paired_dicom = {}

        if find_paired_files:
            print("\tSearching for paired DICOM files...")
            paired_file = self.find_paired_file(self)

            if paired_file is not None:
                if self.PAIRING_TYPE in self.paired_files.keys():
                    raise NotImplementedError(
                        "multiple paired files of same type not implemented"
                    )

                self.paired_files[self.PAIRING_TYPE] = paired_file

                if autoload_paired_files:
                    self._paired_dicom[self.PAIRING_TYPE] = self.get_paired_dicom(
                        self.PAIRING_TYPE
                    )

    def base_paring_key(self, dicom_handle):
        return self.get_pairing_key(dicom_handle)

    @abstractmethod
    def get_pairing_key(self, dicom_handle) -> str:
        pass

    @property
    @abstractmethod
    def PAIRING_TYPE(self) -> PythonFileAutoDicom:
        pass

    @property
    @abstractmethod
    def PAIRING_WC(self) -> str:
        pass

    @classmethod
    def find_paired_file(cls, file_or_dicom_to_pair, search_dir=None):
        import os

        if isinstance(file_or_dicom_to_pair, str) and os.path.isfile(
            file_or_dicom_to_pair
        ):
            file_or_dicom_to_pair = cls(file_or_dicom_to_pair)

        if search_dir is None:
            dir_name = os.path.dirname(file_or_dicom_to_pair.file_name)
        else:
            base_dir = search_dir
            assert os.path.isdir(base_dir)

        search_wc = os.path.join(dir_name, cls.PAIRING_WC)
        cand_files = list_files_by_wildcard(search_wc)
        key_to_match = cls.base_paring_key(file_or_dicom_to_pair)

        if issubclass(cls.PAIRING_TYPE, PairedDicomFile):
            id_list = [
                cls.get_pairing_key(
                    cls.PAIRING_TYPE(s, verbose=False, load_paired_files=False)
                )
                for s in cand_files
            ]
        else:
            id_list = [
                cls.get_pairing_key(cls.PAIRING_TYPE(s, verbose=False))
                for s in cand_files
            ]

        matching_id = [
            ind for ind in range(0, len(id_list)) if id_list[ind] == key_to_match
        ]

        if len(matching_id) == 0:
            print("\t\tFailed to find file matching %s" % cls.PAIRING_WC)
            return None
        elif len(matching_id) == 1:
            print(
                "\t\tFound matching %s file: %s"
                % (cls.PAIRING_TYPE.__name__, cand_files[matching_id[0]])
            )
            return cand_files[matching_id[0]]
        else:
            raise RuntimeError("multiple files in dir match dose ID")

    def get_paired_dicom(
        self, pairing_type: PythonFileAutoDicom, force_reload: bool = False
    ):
        """
        Load paired data object from file
        :param pairing_type: type of paired file inherits PythonFileAutoDicom
        :param force_reload: force reload of data if already loaded
        :return: paired DICOM object of pairing_type
        """
        if pairing_type not in self.paired_files.keys():
            print(self.paired_files.keys())
            raise FileNotFoundError("paired %s file not found" % pairing_type)

        paired_file = self.paired_files[pairing_type]

        if force_reload or not pairing_type in self._paired_dicom.keys():
            if issubclass(pairing_type, PairedDicomFile):
                self._paired_dicom[pairing_type] = pairing_type(
                    paired_file, find_paired_files=False
                )
            else:
                self._paired_dicom[pairing_type] = pairing_type(paired_file)

        return self._paired_dicom[pairing_type]


class KVOBIImage(KVOBIImageAutoDicom):
    pass


class MVEPIDImage(MVEPIDImageAutoDicom):
    def __init__(self, file_name: str, verbose=True):
        super().__init__(file_name=file_name, verbose=verbose)
        self.collimator_angle = math.fmod(self.beam_limiting_device_angle, 360.0)
        self.sid_mm = self.rt_image_sid

    @property
    def magnification(self, iso_sid_mm=1000.0):
        return self.sid_mm / iso_sid_mm

    @property
    def gantry_angle(self):
        return math.fmod(super().gantry_angle, 360.0)

    @property
    def jaw_positions(self):
        """

        :return: [x1, x2],[y1, y2] jaw positions in mm
        """

        if len(self.exposure_sequence) != 1:
            raise NotImplementedError("multiple exposures not implemented")

        bld_seq = self.exposure_sequence[0].beam_limiting_device_sequence

        xjaw = [
            s.leafjaw_positions
            for s in bld_seq
            if s.rt_beam_limiting_device_type == "ASYMX"
        ]
        yjaw = [
            s.leafjaw_positions
            for s in bld_seq
            if s.rt_beam_limiting_device_type == "ASYMY"
        ]

        if len(xjaw) != 1 or len(yjaw) != 1:
            raise NotImplementedError("multiple jaw positions not implemented")

        return xjaw[0], yjaw[0]

    def calculate_dimensions(self):
        row_spacing, column_spacing = self.image_plane_pixel_spacing
        nr, nc = self.rows, self.columns

        ysize = nr * row_spacing
        xsize = nc * column_spacing

        imager_lat = self.xray_image_receptor_translation[0]
        imager_lng = self.xray_image_receptor_translation[1]
        imager_vrt = self.xray_image_receptor_translation[2]

        imager_angle = self.xray_image_receptor_angle
        imager_plan = self.rt_image_plane

        self.reported_values_origin

        origin_y = -1 * ysize / 2.0 + imager_lng
        origin_x = -1 * xsize / 2.0 + imager_lat

        origin = [origin_y, origin_x]

        if self.reported_values_origin != "ACTUAL":
            raise NotImplementedError()

        return origin, (row_spacing, column_spacing)

    def get_image(self) -> NDVoxelArray:
        return self._get_ndimage()

    def get_beam_aperture(self):
        xjaw, yjaw = self.jaw_positions

        return BeamAperture(xjaw, yjaw, self.collimator_angle, self.sid_mm)


class VICQAPlan(VICQAPlanAutoDicom):
    pass


class VIStructureSet(VICRTStructureAutoDicom):
    FILENAME_WC = "RS*.dcm"

    pass


class VICRTPlan(VICRTPlanAutoDicom):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._field_order = None

    def save_as(self, filename):
        self.set_varian_xml()
        super().save_as(filename)

    @property
    def isocenter(self) -> list[float]:
        self.beam_sequence[0].control_point_sequence[0].isocenter_position

        first_iso = self.beam_sequence[0].control_point_sequence[0].isocenter_position

        if not all(
            [
                c[0].isocenter_position == first_iso
                for c in [s.control_point_sequence for s in self.beam_sequence]
            ]
        ):
            raise RuntimeError("only single-isocenter plans implemented")
        else:
            return first_iso

    def new_beam_from_id(self, new_beam_name, orig_beam_name, total_mu: float = None):
        from copy import deepcopy

        beam_to_copy = self.get_beam(orig_beam_name)
        bc = deepcopy(beam_to_copy)
        fg = deepcopy(self.get_fraction_group(beam_to_copy))
        ps = deepcopy(self.get_patient_setup(beam_to_copy))

        if total_mu is not None:
            fg.beam_meterset = total_mu

        bc.beam_name = new_beam_name
        self.add_beam(bc, fg, ps)
        return bc

    def remove_beam(self, beam_name: str):
        beam = self.get_beam(beam_name)

        fg = self.get_fraction_group(beam)
        ps = self.get_patient_setup(beam)

        # remove beam from beam sequence
        self.beam_sequence.remove(beam)

        # remove beam from fraction group sequence
        self.fraction_group_sequence[0].referenced_beam_sequence.remove(fg)

        # remove beam from patient setup sequence
        self.patient_setup_sequence.remove(ps)

        self.fraction_group_sequence[0].number_of_beams -= 1

        self.renumber()

    # function to add beam to plan
    def add_beam(
        self,
        beam: VICRTPlanBeamAutoDicom,
        fg: VICRTPlanReferencedBeamAutoDicom,
        ps: VICRTPlanPatientSetupAutoDicom,
    ):
        if beam.beam_name in [b.beam_name for b in self.beam_sequence]:
            raise ValueError("beam name already exists")

        max_beam_number = max([b.beam_number for b in self.beam_sequence])
        new_beam_number = max_beam_number + 1

        # add beam to beam sequence
        beam.beam_number = new_beam_number

        fg.referenced_beam_number = new_beam_number
        self.add_fraction_group(fg)

        new_ps_number = self.add_patient_setup(ps)
        beam.referenced_patient_setup_number = new_ps_number

        self.beam_sequence.append(beam)

        self._add_field_order(beam.beam_name)

        self.fraction_group_sequence[0].number_of_beams += 1

        self.renumber()

    def add_fraction_group(self, fg: VICRTPlanFractionGroupAutoDicom):
        self.fraction_group_sequence[0].referenced_beam_sequence.append(fg)

    # method to add new patient setup, checking max patient setup and incrementing, adding
    def add_patient_setup(self, ps: VICRTPlanPatientSetupAutoDicom) -> int:
        max_patient_setup_number = max(
            [ps.patient_setup_number for ps in self.patient_setup_sequence]
        )
        new_patient_setup_number = max_patient_setup_number + 1
        ps.patient_setup_number = new_patient_setup_number
        self.patient_setup_sequence.append(ps)
        return new_patient_setup_number

    # method to renumber beam numbers, patient setup numbers, and fraction group numbers
    def renumber(self):
        # renumber beam sequence
        for i, beam in enumerate(self.beam_sequence):
            beam.beam_number = i + 1

        # renumber patient setup sequence
        for i, ps in enumerate(self.patient_setup_sequence):
            ps.patient_setup_number = i + 1

        # renumber fraction group sequence
        for i, fg in enumerate(self.fraction_group_sequence):
            fg.fraction_group_number = i + 1

    # method to add field order to a beam
    def _add_field_order(self, beam_name):
        assert beam_name not in self.field_order.keys()
        max_field_order = max(self.field_order.values())
        self.field_order[beam_name] = max_field_order + 1

    # method to remove field order from a beam
    def _remove_field_order(self, beam_name):
        del self.field_order[beam_name]

    # fix field order
    def fix_field_order(self):
        beam_names = [
            b.beam_name
            for b in self.beam_sequence
            if b.beam_name in self.field_order.keys()
        ]
        beam_field_orders = [self.field_order[b] for b in beam_names]

        # sort beam names by corresponding field orders
        beam_names = [x for _, x in sorted(zip(beam_field_orders, beam_names))]
        sorted_beam_names = beam_names + [
            b.beam_name for b in self.beam_sequence if b.beam_name not in beam_names
        ]

        # generate dict of beam_name:index for sorted_beam_names
        beam_name_index = {
            beam_name: i + 1 for i, beam_name in enumerate(sorted_beam_names)
        }
        self.field_order = beam_name_index

    # Method goes through fraction group sequences, patient setup sequences, beam sequences and
    # and make sure all the sequences numbers, beam numbers start at 1 and are consistent
    # method must check actual reference numbers on items as they are not necessarily in order
    def renumber(self):
        # get beams
        beams = self.beam_sequence

        # get patient setups for these beams in the same order
        patient_setup_numbers = [
            self.get_patient_setup(b).patient_setup_number for b in self.beam_sequence
        ]

        # get fraction group numbers for these beams in the same order
        fraction_group_numbers = [
            self.get_fraction_group(b).referenced_beam_number
            for b in self.beam_sequence
        ]

        # get field orders
        field_orders = [self.field_order[b.beam_name] for b in self.beam_sequence]

        new_field_order = {}

        for i in range(len(self.beam_sequence)):
            self.beam_sequence[i].beam_number = i + 1
            self.patient_setup_sequence.patient_setup_number = i + 1
            self.fraction_group_sequence[0].referenced_beam_sequence[
                i
            ].referenced_beam_number = (i + 1)
            new_field_order[self.beam_sequence[i].beam_name] = field_orders[i]

        self.field_order = new_field_order
        self.fix_field_order()

    def get_patient_setup(self, beam):
        # repeat for patient setup sequece matching referenced patient setup number
        ps_rbs = [
            s
            for s in self.patient_setup_sequence
            if s.patient_setup_number == beam.referenced_patient_setup_number
        ]
        if len(ps_rbs) != 1:
            raise RuntimeError("beam not found in patient setup")
        else:
            return ps_rbs[0]

    def get_fraction_group(self, beam: VICRTPlanBeamAutoDicom):
        if len(self.fraction_group_sequence) > 1:
            raise NotImplementedError("multiple fraction groups not implemented")

        # find fraction group sequence matching by referenced beam number
        fg_rbs = [
            s
            for s in self.fraction_group_sequence[0].referenced_beam_sequence
            if s.referenced_beam_number == beam.beam_number
        ]
        if len(fg_rbs) != 1:
            raise RuntimeError("beam not found in fraction group")
        else:
            fg_rbs = fg_rbs[0]
        return fg_rbs

    def get_beam(self, beam_name: str):
        for beam in self.beam_sequence:
            if beam.beam_name == beam_name:
                return beam
        raise ValueError("beam not found")

    @property
    def beam_id(self) -> Dict[int, str]:
        return {b.beam_number: b.beam_name for b in self.beam_sequence}

    @property
    def beam_number(self) -> Dict[str, int]:
        return {b.beam_name: b.beam_number for b in self.beam_sequence}

    @property
    def field_order(self):
        if self._field_order is None:
            import xml.etree.ElementTree as ET

            root = ET.fromstring(self.xml_stream.decode("utf-8"))

            pairs = {}
            for beam in root.iter("Beam"):
                beam_number = int(beam.find("ReferencedBeamNumber").text)
                field_order = int(beam.find("BeamExtension/FieldOrder").text)
                d = self.beam_id.keys()

                if beam_number in self.beam_id.keys():
                    pairs[self.beam_id[beam_number]] = field_order

            self._field_order = pairs
        return self._field_order

    @field_order.setter
    def field_order(self, value):
        self._field_order = value

    def set_varian_xml(self):
        # ensure all values in order_dict start at 1 and are sequential
        all_values = sorted(list(self.field_order.values()))
        if all_values != list(range(1, len(all_values) + 1)):
            raise ValueError("field order values must start at 1 and be sequential")

        return_xml = r'<?xml version="1.0" encoding="utf-8"?><ExtendedVAPlanInterface Version="1"><Beams>'

        beam_xml = ""
        for beam_name, field_order in self.field_order.items():
            return_xml += (
                "<Beam><ReferencedBeamNumber>%s</ReferencedBeamNumber><BeamExtension><FieldOrder>%s</FieldOrder><GantryRtnExtendedStart>false</GantryRtnExtendedStart><GantryRtnExtendedStop>false</GantryRtnExtendedStop></BeamExtension></Beam>"
                % (self.beam_number[beam_name], field_order)
            )

        import warnings

        warnings.warn("Tolerance tables not implemented for dicom editing")
        # TODO tolerance tables
        return_xml += "</Beams><ToleranceTables/><DoseReferences>"

        for dr in self.dose_reference_sequence:
            return_xml += (
                "<DoseReference><ReferencedDoseReferenceNumber>%s</ReferencedDoseReferenceNumber><DoseReferenceExtension/></DoseReference>"
                % (dr.dose_reference_number)
            )

        return_xml += "</DoseReferences></ExtendedVAPlanInterface>"

        self.xml_stream = return_xml.encode("utf-8")
        self.data_length_of_the_xml_stream = str(len(self.xml_stream)).encode("utf-8")


class VIBeamDicom(VICRTPlanBeamAutoDicom):
    pass


class VIDoseStorage(VICDoseAutoDicom):
    @property
    def plan_dicom(self) -> VICRTPlan:
        return self.get_paired_dicom(self.PAIRING_TYPE)

    @property
    def dose_array_cgy(self) -> NDVoxelArray:
        if self.dose_units == "GY":
            mult_factor = 100
        else:
            raise NotImplementedError()

        return self._get_ndimage() * self.dose_grid_scaling * mult_factor

    def calculate_dimensions(self):
        row_spacing = self.pixel_spacing[0]
        column_spacing = self.pixel_spacing[1]
        origin = [
            self.image_position_patient[2],
            self.image_position_patient[1],
            self.image_position_patient[0],
        ]

        row_direction_cosine = [
            self.image_orientation_patient[2],
            self.image_orientation_patient[1],
            self.image_orientation_patient[0],
        ]
        column_direction_cosine = [
            self.image_orientation_patient[5],
            self.image_orientation_patient[4],
            self.image_orientation_patient[3],
        ]

        if not all([a == b for a, b in zip(row_direction_cosine, [0.0, 0.0, 1.0])]):
            raise NotImplementedError("only x-row, y-col, z-slice data implemented!")
        if not all([a == b for a, b in zip(column_direction_cosine, [0.0, 1.0, 0.0])]):
            raise NotImplementedError("only x-row, y-col, z-slice data implemented!")

        slice_spacing = self.grid_frame_offset_vector[1]

        dz, dy, dx = [slice_spacing, column_spacing, row_spacing]

        origin = [
            origin[0] - (dz / 2.0),
            origin[1] - (dy / 2.0),
            origin[2] - (dx / 2.0),
        ]

        return origin, (dz, dy, dx)


class PairedRTPlan(PairedDicomFile):
    @classmethod
    def get_pairing_key(cls, dicom_handle):
        return dicom_handle.sop_instance_uid

    @classmethod
    def base_paring_key(self, dicom_handle):
        return dicom_handle.referenced_rt_plan_sequence[0].referenced_sop_instance_uid

    PAIRING_TYPE = VICRTPlan
    PAIRING_WC = "RP*.dcm"


class PairedStructureFile(PairedDicomFile):
    AUTOLOAD_PAIRED_FILES = False

    @classmethod
    def get_pairing_key(cls, dicom_handle):
        return dicom_handle.referenced_frame_of_reference_sequence[
            0
        ].frame_of_reference_uid

    @classmethod
    def base_paring_key(self, dicom_handle):
        return dicom_handle.frame_of_reference_uid

    PAIRING_TYPE = VIStructureSet
    PAIRING_WC = "RS*.dcm"


class PairedDoseFile(PairedDicomFile):
    @classmethod
    def get_pairing_key(cls, dicom_handle):
        return dicom_handle.frame_of_reference_uid

    @classmethod
    def base_paring_key(self, dicom_handle):
        return dicom_handle.frame_of_reference_uid

    PAIRING_TYPE = VIDoseStorage
    PAIRING_WC = "RD*.dcm"


class VICTSlice(VICCTImageSliceAutoDicom):
    @property
    def slice_location_mm(self):
        return self.slice_location

    # @property
    # def plan_dicom(self) -> VICRTPlan:
    #     return self.get_paired_dicom(self.PAIRING_TYPE)
    #
    # @property
    # def dose_array_cgy(self) -> NDVoxelArray:
    #
    #     if (self.dose_units == "GY"):
    #         mult_factor = 100
    #     else:
    #         raise NotImplementedError()
    #
    #     return self._get_ndimage() * self.dose_grid_scaling

    def calculate_dimensions(self):
        row_spacing = self.pixel_spacing[0]
        column_spacing = self.pixel_spacing[1]
        slice_spacing = self.slice_thickness

        origin = [
            self.image_position_patient[2],
            self.image_position_patient[1],
            self.image_position_patient[0],
        ]
        #
        row_direction_cosine = [
            self.image_orientation_patient[2],
            self.image_orientation_patient[1],
            self.image_orientation_patient[0],
        ]
        column_direction_cosine = [
            self.image_orientation_patient[5],
            self.image_orientation_patient[4],
            self.image_orientation_patient[3],
        ]
        #
        if not all([a == b for a, b in zip(row_direction_cosine, [0.0, 0.0, 1.0])]):
            raise NotImplementedError("only x-row, y-col, z-slice data implemented!")
        if not all([a == b for a, b in zip(column_direction_cosine, [0.0, 1.0, 0.0])]):
            raise NotImplementedError("only x-row, y-col, z-slice data implemented!")
        #
        # slice_spacing = self.grid_frame_offset_vector[1]
        #
        dz, dy, dx = [slice_spacing, column_spacing, row_spacing]
        #
        origin = [origin[1] - (dy / 2.0), origin[2] - (dx / 2.0)]

        return origin, (dy, dx)

    pass
