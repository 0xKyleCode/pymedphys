from pydicom.tag import BaseTag
from pydicom.multival import MultiValue
from pyvic.util.dicom import (
    PythonFileAutoDicom,
    PythonAutoDicom,
)


class VICRTStructureAutoDicom(PythonFileAutoDicom):
    description = "VIC RT Structure Dicom format"

    @property
    def structure_set_time(self):
        if (0x3006, 0x0009) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3006, 0x0009].value, BaseTag):
                return self._pydicom_obj[0x3006, 0x0009].value
            elif isinstance(self._pydicom_obj[0x3006, 0x0009].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3006, 0x0009].value]
            else:
                return self._pydicom_obj[0x3006, 0x0009].value
        else:
            return None

    @property
    def structure_set_date(self):
        if (0x3006, 0x0008) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3006, 0x0008].value, BaseTag):
                return self._pydicom_obj[0x3006, 0x0008].value
            elif isinstance(self._pydicom_obj[0x3006, 0x0008].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3006, 0x0008].value]
            else:
                return self._pydicom_obj[0x3006, 0x0008].value
        else:
            return None

    @property
    def sop_instance_uid(self):
        if (0x0008, 0x0018) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0018].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0018].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0018].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0018].value]
            else:
                return self._pydicom_obj[0x0008, 0x0018].value
        else:
            return None

    @property
    def modality(self):
        if (0x0008, 0x0060) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0060].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0060].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0060].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0060].value]
            else:
                return self._pydicom_obj[0x0008, 0x0060].value
        else:
            return None

    @property
    def manufacturers_model_name(self):
        if (0x0008, 0x1090) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x1090].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x1090].value
            elif isinstance(self._pydicom_obj[0x0008, 0x1090].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x1090].value]
            else:
                return self._pydicom_obj[0x0008, 0x1090].value
        else:
            return None

    @property
    def device_serial_number(self):
        if (0x0018, 0x1000) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0018, 0x1000].value, BaseTag):
                return self._pydicom_obj[0x0018, 0x1000].value
            elif isinstance(self._pydicom_obj[0x0018, 0x1000].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0018, 0x1000].value]
            else:
                return self._pydicom_obj[0x0018, 0x1000].value
        else:
            return None

    @property
    def structure_set_label(self):
        if (0x3006, 0x0002) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3006, 0x0002].value, BaseTag):
                return self._pydicom_obj[0x3006, 0x0002].value
            elif isinstance(self._pydicom_obj[0x3006, 0x0002].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3006, 0x0002].value]
            else:
                return self._pydicom_obj[0x3006, 0x0002].value
        else:
            return None

    @property
    def study_id(self):
        if (0x0020, 0x0010) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0020, 0x0010].value, BaseTag):
                return self._pydicom_obj[0x0020, 0x0010].value
            elif isinstance(self._pydicom_obj[0x0020, 0x0010].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0020, 0x0010].value]
            else:
                return self._pydicom_obj[0x0020, 0x0010].value
        else:
            return None

    @property
    def study_date(self):
        if (0x0008, 0x0020) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0020].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0020].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0020].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0020].value]
            else:
                return self._pydicom_obj[0x0008, 0x0020].value
        else:
            return None

    @property
    def operators_name(self):
        if (0x0008, 0x1070) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x1070].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x1070].value
            elif isinstance(self._pydicom_obj[0x0008, 0x1070].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x1070].value]
            else:
                return self._pydicom_obj[0x0008, 0x1070].value
        else:
            return None

    @property
    def patients_birth_date(self):
        if (0x0010, 0x0030) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0010, 0x0030].value, BaseTag):
                return self._pydicom_obj[0x0010, 0x0030].value
            elif isinstance(self._pydicom_obj[0x0010, 0x0030].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0010, 0x0030].value]
            else:
                return self._pydicom_obj[0x0010, 0x0030].value
        else:
            return None

    @property
    def patients_name(self):
        if (0x0010, 0x0010) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0010, 0x0010].value, BaseTag):
                return self._pydicom_obj[0x0010, 0x0010].value
            elif isinstance(self._pydicom_obj[0x0010, 0x0010].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0010, 0x0010].value]
            else:
                return self._pydicom_obj[0x0010, 0x0010].value
        else:
            return None

    @property
    def manufacturer(self):
        if (0x0008, 0x0070) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0070].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0070].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0070].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0070].value]
            else:
                return self._pydicom_obj[0x0008, 0x0070].value
        else:
            return None

    @property
    def specific_character_set(self):
        if (0x0008, 0x0005) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0005].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0005].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0005].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0005].value]
            else:
                return self._pydicom_obj[0x0008, 0x0005].value
        else:
            return None

    @property
    def instance_creation_date(self):
        if (0x0008, 0x0012) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0012].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0012].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0012].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0012].value]
            else:
                return self._pydicom_obj[0x0008, 0x0012].value
        else:
            return None

    @property
    def study_instance_uid(self):
        if (0x0020, 0x000D) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0020, 0x000D].value, BaseTag):
                return self._pydicom_obj[0x0020, 0x000D].value
            elif isinstance(self._pydicom_obj[0x0020, 0x000D].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0020, 0x000D].value]
            else:
                return self._pydicom_obj[0x0020, 0x000D].value
        else:
            return None

    @property
    def series_instance_uid(self):
        if (0x0020, 0x000E) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0020, 0x000E].value, BaseTag):
                return self._pydicom_obj[0x0020, 0x000E].value
            elif isinstance(self._pydicom_obj[0x0020, 0x000E].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0020, 0x000E].value]
            else:
                return self._pydicom_obj[0x0020, 0x000E].value
        else:
            return None

    @property
    def instance_creation_time(self):
        if (0x0008, 0x0013) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0013].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0013].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0013].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0013].value]
            else:
                return self._pydicom_obj[0x0008, 0x0013].value
        else:
            return None

    @property
    def instance_number(self):
        if (0x0020, 0x0013) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0020, 0x0013].value, BaseTag):
                return self._pydicom_obj[0x0020, 0x0013].value
            elif isinstance(self._pydicom_obj[0x0020, 0x0013].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0020, 0x0013].value]
            else:
                return self._pydicom_obj[0x0020, 0x0013].value
        else:
            return None

    @property
    def accession_number(self):
        if (0x0008, 0x0050) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0050].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0050].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0050].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0050].value]
            else:
                return self._pydicom_obj[0x0008, 0x0050].value
        else:
            return None

    @property
    def series_description(self):
        if (0x0008, 0x103E) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x103E].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x103E].value
            elif isinstance(self._pydicom_obj[0x0008, 0x103E].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x103E].value]
            else:
                return self._pydicom_obj[0x0008, 0x103E].value
        else:
            return None

    @property
    def approval_status(self):
        if (0x300E, 0x0002) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300E, 0x0002].value, BaseTag):
                return self._pydicom_obj[0x300E, 0x0002].value
            elif isinstance(self._pydicom_obj[0x300E, 0x0002].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300E, 0x0002].value]
            else:
                return self._pydicom_obj[0x300E, 0x0002].value
        else:
            return None

    @property
    def study_time(self):
        if (0x0008, 0x0030) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0030].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0030].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0030].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0030].value]
            else:
                return self._pydicom_obj[0x0008, 0x0030].value
        else:
            return None

    @property
    def patient_id(self):
        if (0x0010, 0x0020) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0010, 0x0020].value, BaseTag):
                return self._pydicom_obj[0x0010, 0x0020].value
            elif isinstance(self._pydicom_obj[0x0010, 0x0020].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0010, 0x0020].value]
            else:
                return self._pydicom_obj[0x0010, 0x0020].value
        else:
            return None

    @property
    def sop_class_uid(self):
        if (0x0008, 0x0016) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0016].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0016].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0016].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0016].value]
            else:
                return self._pydicom_obj[0x0008, 0x0016].value
        else:
            return None

    @property
    def patients_sex(self):
        if (0x0010, 0x0040) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0010, 0x0040].value, BaseTag):
                return self._pydicom_obj[0x0010, 0x0040].value
            elif isinstance(self._pydicom_obj[0x0010, 0x0040].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0010, 0x0040].value]
            else:
                return self._pydicom_obj[0x0010, 0x0040].value
        else:
            return None

    @property
    def series_number(self):
        if (0x0020, 0x0011) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0020, 0x0011].value, BaseTag):
                return self._pydicom_obj[0x0020, 0x0011].value
            elif isinstance(self._pydicom_obj[0x0020, 0x0011].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0020, 0x0011].value]
            else:
                return self._pydicom_obj[0x0020, 0x0011].value
        else:
            return None

    @property
    def referring_physicians_name(self):
        if (0x0008, 0x0090) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0090].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0090].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0090].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0090].value]
            else:
                return self._pydicom_obj[0x0008, 0x0090].value
        else:
            return None

    @property
    def patients_birth_time(self):
        if (0x0010, 0x0032) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0010, 0x0032].value, BaseTag):
                return self._pydicom_obj[0x0010, 0x0032].value
            elif isinstance(self._pydicom_obj[0x0010, 0x0032].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0010, 0x0032].value]
            else:
                return self._pydicom_obj[0x0010, 0x0032].value
        else:
            return None

    @property
    def station_name(self):
        if (0x0008, 0x1010) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x1010].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x1010].value
            elif isinstance(self._pydicom_obj[0x0008, 0x1010].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x1010].value]
            else:
                return self._pydicom_obj[0x0008, 0x1010].value
        else:
            return None

    @property
    def software_versions(self):
        if (0x0018, 0x1020) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0018, 0x1020].value, BaseTag):
                return self._pydicom_obj[0x0018, 0x1020].value
            elif isinstance(self._pydicom_obj[0x0018, 0x1020].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0018, 0x1020].value]
            else:
                return self._pydicom_obj[0x0018, 0x1020].value
        else:
            return None

    @property
    def structure_set_roi_sequence(self):
        val = self._pydicom_obj[0x3006, 0x0020].value
        if val == "None" or val is None:
            return None
        else:
            return [VICRTStructureStructureSetROIAutoDicom(s) for s in val]

    @property
    def coding_scheme_identification_sequence(self):
        val = self._pydicom_obj[0x0008, 0x0110].value
        if val == "None" or val is None:
            return None
        else:
            return [VICRTStructureCodingSchemeIdentificationAutoDicom(s) for s in val]

    @property
    def roi_contour_sequence(self):
        val = self._pydicom_obj[0x3006, 0x0039].value
        if val == "None" or val is None:
            return None
        else:
            return [VICRTStructureROIContourAutoDicom(s) for s in val]

    @property
    def referenced_frame_of_reference_sequence(self):
        val = self._pydicom_obj[0x3006, 0x0010].value
        if val == "None" or val is None:
            return None
        else:
            return [VICRTStructureReferencedFrameofReferenceAutoDicom(s) for s in val]

    @property
    def rt_roi_observations_sequence(self):
        val = self._pydicom_obj[0x3006, 0x0080].value
        if val == "None" or val is None:
            return None
        else:
            return [VICRTStructureRTROIObservationsAutoDicom(s) for s in val]

    @property
    def context_group_identification_sequence(self):
        val = self._pydicom_obj[0x0008, 0x0123].value
        if val == "None" or val is None:
            return None
        else:
            return [VICRTStructureContextGroupIdentificationAutoDicom(s) for s in val]

    @property
    def mapping_resource_identification_sequence(self):
        val = self._pydicom_obj[0x0008, 0x0124].value
        if val == "None" or val is None:
            return None
        else:
            return [
                VICRTStructureMappingResourceIdentificationAutoDicom(s) for s in val
            ]

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "structure_set_time: %s\n" % (self.structure_set_time)
        to_ret_str += "structure_set_date: %s\n" % (self.structure_set_date)
        to_ret_str += "sop_instance_uid: %s\n" % (self.sop_instance_uid)
        to_ret_str += "modality: %s\n" % (self.modality)
        to_ret_str += "manufacturers_model_name: %s\n" % (self.manufacturers_model_name)
        to_ret_str += "device_serial_number: %s\n" % (self.device_serial_number)
        to_ret_str += "structure_set_label: %s\n" % (self.structure_set_label)
        to_ret_str += "study_id: %s\n" % (self.study_id)
        to_ret_str += "study_date: %s\n" % (self.study_date)
        to_ret_str += "operators_name: %s\n" % (self.operators_name)
        to_ret_str += "patients_birth_date: %s\n" % (self.patients_birth_date)
        to_ret_str += "patients_name: %s\n" % (self.patients_name)
        to_ret_str += "manufacturer: %s\n" % (self.manufacturer)
        to_ret_str += "specific_character_set: %s\n" % (self.specific_character_set)
        to_ret_str += "instance_creation_date: %s\n" % (self.instance_creation_date)
        to_ret_str += "study_instance_uid: %s\n" % (self.study_instance_uid)
        to_ret_str += "series_instance_uid: %s\n" % (self.series_instance_uid)
        to_ret_str += "instance_creation_time: %s\n" % (self.instance_creation_time)
        to_ret_str += "instance_number: %s\n" % (self.instance_number)
        to_ret_str += "accession_number: %s\n" % (self.accession_number)
        to_ret_str += "series_description: %s\n" % (self.series_description)
        to_ret_str += "approval_status: %s\n" % (self.approval_status)
        to_ret_str += "study_time: %s\n" % (self.study_time)
        to_ret_str += "patient_id: %s\n" % (self.patient_id)
        to_ret_str += "sop_class_uid: %s\n" % (self.sop_class_uid)
        to_ret_str += "patients_sex: %s\n" % (self.patients_sex)
        to_ret_str += "series_number: %s\n" % (self.series_number)
        to_ret_str += "referring_physicians_name: %s\n" % (
            self.referring_physicians_name
        )
        to_ret_str += "patients_birth_time: %s\n" % (self.patients_birth_time)
        to_ret_str += "station_name: %s\n" % (self.station_name)
        to_ret_str += "software_versions: %s\n" % (self.software_versions)
        to_ret_str += "structure_set_roi_sequence: %s\n" % (
            self.structure_set_roi_sequence
        )
        to_ret_str += "coding_scheme_identification_sequence: %s\n" % (
            self.coding_scheme_identification_sequence
        )
        to_ret_str += "roi_contour_sequence: %s\n" % (self.roi_contour_sequence)
        to_ret_str += "referenced_frame_of_reference_sequence: %s\n" % (
            self.referenced_frame_of_reference_sequence
        )
        to_ret_str += "rt_roi_observations_sequence: %s\n" % (
            self.rt_roi_observations_sequence
        )
        to_ret_str += "context_group_identification_sequence: %s\n" % (
            self.context_group_identification_sequence
        )
        to_ret_str += "mapping_resource_identification_sequence: %s\n" % (
            self.mapping_resource_identification_sequence
        )
        return to_ret_str

    @classmethod
    def from_dicom_file(cls, path, stop_before_pixels=False):
        """
        :rtype: VICRTStructureAutoDicom
        """
        try:
            import dicom as pydicom
        except ImportError:
            import pydicom
        dcm_hand = pydicom.read_file(path, stop_before_pixels=stop_before_pixels)
        to_ret = cls(dcm_hand, path)
        return to_ret


class VICRTStructureStructureSetROIAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTStructureAutoDicom"

    @property
    def roi_generation_algorithm(self):
        if (0x3006, 0x0036) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3006, 0x0036].value, BaseTag):
                return self._pydicom_obj[0x3006, 0x0036].value
            elif isinstance(self._pydicom_obj[0x3006, 0x0036].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3006, 0x0036].value]
            else:
                return self._pydicom_obj[0x3006, 0x0036].value
        else:
            return None

    @property
    def roi_name(self):
        if (0x3006, 0x0026) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3006, 0x0026].value, BaseTag):
                return self._pydicom_obj[0x3006, 0x0026].value
            elif isinstance(self._pydicom_obj[0x3006, 0x0026].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3006, 0x0026].value]
            else:
                return self._pydicom_obj[0x3006, 0x0026].value
        else:
            return None

    @property
    def roi_number(self):
        if (0x3006, 0x0022) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3006, 0x0022].value, BaseTag):
                return self._pydicom_obj[0x3006, 0x0022].value
            elif isinstance(self._pydicom_obj[0x3006, 0x0022].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3006, 0x0022].value]
            else:
                return self._pydicom_obj[0x3006, 0x0022].value
        else:
            return None

    @property
    def referenced_frame_of_reference_uid(self):
        if (0x3006, 0x0024) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3006, 0x0024].value, BaseTag):
                return self._pydicom_obj[0x3006, 0x0024].value
            elif isinstance(self._pydicom_obj[0x3006, 0x0024].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3006, 0x0024].value]
            else:
                return self._pydicom_obj[0x3006, 0x0024].value
        else:
            return None

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "roi_generation_algorithm: %s\n" % (self.roi_generation_algorithm)
        to_ret_str += "roi_name: %s\n" % (self.roi_name)
        to_ret_str += "roi_number: %s\n" % (self.roi_number)
        to_ret_str += "referenced_frame_of_reference_uid: %s\n" % (
            self.referenced_frame_of_reference_uid
        )
        return to_ret_str


class VICRTStructureCodingSchemeIdentificationAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTStructureAutoDicom"

    @property
    def coding_scheme_responsible_organization(self):
        if (0x0008, 0x0116) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0116].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0116].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0116].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0116].value]
            else:
                return self._pydicom_obj[0x0008, 0x0116].value
        else:
            return None

    @property
    def coding_scheme_designator(self):
        if (0x0008, 0x0102) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0102].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0102].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0102].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0102].value]
            else:
                return self._pydicom_obj[0x0008, 0x0102].value
        else:
            return None

    @property
    def coding_scheme_name(self):
        if (0x0008, 0x0115) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0115].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0115].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0115].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0115].value]
            else:
                return self._pydicom_obj[0x0008, 0x0115].value
        else:
            return None

    @property
    def coding_scheme_uid(self):
        if (0x0008, 0x010C) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x010C].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x010C].value
            elif isinstance(self._pydicom_obj[0x0008, 0x010C].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x010C].value]
            else:
                return self._pydicom_obj[0x0008, 0x010C].value
        else:
            return None

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "coding_scheme_responsible_organization: %s\n" % (
            self.coding_scheme_responsible_organization
        )
        to_ret_str += "coding_scheme_designator: %s\n" % (self.coding_scheme_designator)
        to_ret_str += "coding_scheme_name: %s\n" % (self.coding_scheme_name)
        to_ret_str += "coding_scheme_uid: %s\n" % (self.coding_scheme_uid)
        return to_ret_str


class VICRTStructureROIContourAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTStructureAutoDicom"

    @property
    def referenced_roi_number(self):
        if (0x3006, 0x0084) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3006, 0x0084].value, BaseTag):
                return self._pydicom_obj[0x3006, 0x0084].value
            elif isinstance(self._pydicom_obj[0x3006, 0x0084].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3006, 0x0084].value]
            else:
                return self._pydicom_obj[0x3006, 0x0084].value
        else:
            return None

    @property
    def roi_display_color(self):
        if (0x3006, 0x002A) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3006, 0x002A].value, BaseTag):
                return self._pydicom_obj[0x3006, 0x002A].value
            elif isinstance(self._pydicom_obj[0x3006, 0x002A].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3006, 0x002A].value]
            else:
                return self._pydicom_obj[0x3006, 0x002A].value
        else:
            return None

    @property
    def contour_sequence(self):
        val = self._pydicom_obj[0x3006, 0x0040].value
        if val == "None" or val is None:
            return None
        else:
            return [VICRTStructureContourAutoDicom(s) for s in val]

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "referenced_roi_number: %s\n" % (self.referenced_roi_number)
        to_ret_str += "roi_display_color: %s\n" % (self.roi_display_color)
        to_ret_str += "contour_sequence: %s\n" % (self.contour_sequence)
        return to_ret_str


class VICRTStructureContourAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTStructureROIContourAutoDicom"

    @property
    def contour_data(self):
        if (0x3006, 0x0050) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3006, 0x0050].value, BaseTag):
                return self._pydicom_obj[0x3006, 0x0050].value
            elif isinstance(self._pydicom_obj[0x3006, 0x0050].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x3006, 0x0050].value]
            else:
                return float(self._pydicom_obj[0x3006, 0x0050].value)
        else:
            return None

    @property
    def number_of_contour_points(self):
        if (0x3006, 0x0046) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3006, 0x0046].value, BaseTag):
                return self._pydicom_obj[0x3006, 0x0046].value
            elif isinstance(self._pydicom_obj[0x3006, 0x0046].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3006, 0x0046].value]
            else:
                return self._pydicom_obj[0x3006, 0x0046].value
        else:
            return None

    @property
    def contour_geometric_type(self):
        if (0x3006, 0x0042) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3006, 0x0042].value, BaseTag):
                return self._pydicom_obj[0x3006, 0x0042].value
            elif isinstance(self._pydicom_obj[0x3006, 0x0042].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3006, 0x0042].value]
            else:
                return self._pydicom_obj[0x3006, 0x0042].value
        else:
            return None

    @property
    def contour_image_sequence(self):
        val = self._pydicom_obj[0x3006, 0x0016].value
        if val == "None" or val is None:
            return None
        else:
            return [VICRTStructureContourImageAutoDicom(s) for s in val]

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "contour_data: %s\n" % (self.contour_data)
        to_ret_str += "number_of_contour_points: %s\n" % (self.number_of_contour_points)
        to_ret_str += "contour_geometric_type: %s\n" % (self.contour_geometric_type)
        to_ret_str += "contour_image_sequence: %s\n" % (self.contour_image_sequence)
        return to_ret_str


class VICRTStructureContourImageAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTStructureContourAutoDicom"

    @property
    def referenced_sop_class_uid(self):
        if (0x0008, 0x1150) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x1150].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x1150].value
            elif isinstance(self._pydicom_obj[0x0008, 0x1150].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x1150].value]
            else:
                return self._pydicom_obj[0x0008, 0x1150].value
        else:
            return None

    @property
    def referenced_sop_instance_uid(self):
        if (0x0008, 0x1155) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x1155].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x1155].value
            elif isinstance(self._pydicom_obj[0x0008, 0x1155].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x1155].value]
            else:
                return self._pydicom_obj[0x0008, 0x1155].value
        else:
            return None

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "referenced_sop_class_uid: %s\n" % (self.referenced_sop_class_uid)
        to_ret_str += "referenced_sop_instance_uid: %s\n" % (
            self.referenced_sop_instance_uid
        )
        return to_ret_str


class VICRTStructureReferencedFrameofReferenceAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTStructureAutoDicom"

    @property
    def frame_of_reference_uid(self):
        if (0x0020, 0x0052) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0020, 0x0052].value, BaseTag):
                return self._pydicom_obj[0x0020, 0x0052].value
            elif isinstance(self._pydicom_obj[0x0020, 0x0052].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0020, 0x0052].value]
            else:
                return self._pydicom_obj[0x0020, 0x0052].value
        else:
            return None

    @property
    def rt_referenced_study_sequence(self):
        val = self._pydicom_obj[0x3006, 0x0012].value
        if val == "None" or val is None:
            return None
        else:
            return [VICRTStructureRTReferencedStudyAutoDicom(s) for s in val]

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "frame_of_reference_uid: %s\n" % (self.frame_of_reference_uid)
        to_ret_str += "rt_referenced_study_sequence: %s\n" % (
            self.rt_referenced_study_sequence
        )
        return to_ret_str


class VICRTStructureRTReferencedStudyAutoDicom(PythonAutoDicom):
    description = (
        "AutoDicom inner class of VICRTStructureReferencedFrameofReferenceAutoDicom"
    )

    @property
    def referenced_sop_class_uid(self):
        if (0x0008, 0x1150) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x1150].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x1150].value
            elif isinstance(self._pydicom_obj[0x0008, 0x1150].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x1150].value]
            else:
                return self._pydicom_obj[0x0008, 0x1150].value
        else:
            return None

    @property
    def referenced_sop_instance_uid(self):
        if (0x0008, 0x1155) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x1155].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x1155].value
            elif isinstance(self._pydicom_obj[0x0008, 0x1155].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x1155].value]
            else:
                return self._pydicom_obj[0x0008, 0x1155].value
        else:
            return None

    @property
    def rt_referenced_series_sequence(self):
        val = self._pydicom_obj[0x3006, 0x0014].value
        if val == "None" or val is None:
            return None
        else:
            return [VICRTStructureRTReferencedSeriesAutoDicom(s) for s in val]

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "referenced_sop_class_uid: %s\n" % (self.referenced_sop_class_uid)
        to_ret_str += "referenced_sop_instance_uid: %s\n" % (
            self.referenced_sop_instance_uid
        )
        to_ret_str += "rt_referenced_series_sequence: %s\n" % (
            self.rt_referenced_series_sequence
        )
        return to_ret_str


class VICRTStructureRTReferencedSeriesAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTStructureRTReferencedStudyAutoDicom"

    @property
    def series_instance_uid(self):
        if (0x0020, 0x000E) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0020, 0x000E].value, BaseTag):
                return self._pydicom_obj[0x0020, 0x000E].value
            elif isinstance(self._pydicom_obj[0x0020, 0x000E].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0020, 0x000E].value]
            else:
                return self._pydicom_obj[0x0020, 0x000E].value
        else:
            return None

    @property
    def contour_image_sequence(self):
        val = self._pydicom_obj[0x3006, 0x0016].value
        if val == "None" or val is None:
            return None
        else:
            return [VICRTStructureContourImageAutoDicom(s) for s in val]

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "series_instance_uid: %s\n" % (self.series_instance_uid)
        to_ret_str += "contour_image_sequence: %s\n" % (self.contour_image_sequence)
        return to_ret_str


class VICRTStructureContourImageAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTStructureRTReferencedSeriesAutoDicom"

    @property
    def referenced_sop_class_uid(self):
        if (0x0008, 0x1150) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x1150].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x1150].value
            elif isinstance(self._pydicom_obj[0x0008, 0x1150].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x1150].value]
            else:
                return self._pydicom_obj[0x0008, 0x1150].value
        else:
            return None

    @property
    def referenced_sop_instance_uid(self):
        if (0x0008, 0x1155) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x1155].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x1155].value
            elif isinstance(self._pydicom_obj[0x0008, 0x1155].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x1155].value]
            else:
                return self._pydicom_obj[0x0008, 0x1155].value
        else:
            return None

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "referenced_sop_class_uid: %s\n" % (self.referenced_sop_class_uid)
        to_ret_str += "referenced_sop_instance_uid: %s\n" % (
            self.referenced_sop_instance_uid
        )
        return to_ret_str


class VICRTStructureRTROIObservationsAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTStructureAutoDicom"

    @property
    def referenced_roi_number(self):
        if (0x3006, 0x0084) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3006, 0x0084].value, BaseTag):
                return self._pydicom_obj[0x3006, 0x0084].value
            elif isinstance(self._pydicom_obj[0x3006, 0x0084].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3006, 0x0084].value]
            else:
                return self._pydicom_obj[0x3006, 0x0084].value
        else:
            return None

    @property
    def roi_observation_label(self):
        if (0x3006, 0x0085) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3006, 0x0085].value, BaseTag):
                return self._pydicom_obj[0x3006, 0x0085].value
            elif isinstance(self._pydicom_obj[0x3006, 0x0085].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3006, 0x0085].value]
            else:
                return self._pydicom_obj[0x3006, 0x0085].value
        else:
            return None

    @property
    def observation_number(self):
        if (0x3006, 0x0082) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3006, 0x0082].value, BaseTag):
                return self._pydicom_obj[0x3006, 0x0082].value
            elif isinstance(self._pydicom_obj[0x3006, 0x0082].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3006, 0x0082].value]
            else:
                return self._pydicom_obj[0x3006, 0x0082].value
        else:
            return None

    @property
    def rt_roi_interpreted_type(self):
        if (0x3006, 0x00A4) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3006, 0x00A4].value, BaseTag):
                return self._pydicom_obj[0x3006, 0x00A4].value
            elif isinstance(self._pydicom_obj[0x3006, 0x00A4].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3006, 0x00A4].value]
            else:
                return self._pydicom_obj[0x3006, 0x00A4].value
        else:
            return None

    @property
    def roi_interpreter(self):
        if (0x3006, 0x00A6) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3006, 0x00A6].value, BaseTag):
                return self._pydicom_obj[0x3006, 0x00A6].value
            elif isinstance(self._pydicom_obj[0x3006, 0x00A6].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3006, 0x00A6].value]
            else:
                return self._pydicom_obj[0x3006, 0x00A6].value
        else:
            return None

    @property
    def roi_physical_properties_sequence(self):
        val = self._pydicom_obj[0x3006, 0x00B0].value
        if val == "None" or val is None:
            return None
        else:
            return [VICRTStructureROIPhysicalPropertiesAutoDicom(s) for s in val]

    @property
    def rt_roi_identification_code_sequence(self):
        val = self._pydicom_obj[0x3006, 0x0086].value
        if val == "None" or val is None:
            return None
        else:
            return [VICRTStructureRTROIIdentificationCodeAutoDicom(s) for s in val]

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "referenced_roi_number: %s\n" % (self.referenced_roi_number)
        to_ret_str += "roi_observation_label: %s\n" % (self.roi_observation_label)
        to_ret_str += "observation_number: %s\n" % (self.observation_number)
        to_ret_str += "rt_roi_interpreted_type: %s\n" % (self.rt_roi_interpreted_type)
        to_ret_str += "roi_interpreter: %s\n" % (self.roi_interpreter)
        to_ret_str += "roi_physical_properties_sequence: %s\n" % (
            self.roi_physical_properties_sequence
        )
        to_ret_str += "rt_roi_identification_code_sequence: %s\n" % (
            self.rt_roi_identification_code_sequence
        )
        return to_ret_str


class VICRTStructureROIPhysicalPropertiesAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTStructureRTROIObservationsAutoDicom"

    @property
    def roi_physical_property_value(self):
        if (0x3006, 0x00B4) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3006, 0x00B4].value, BaseTag):
                return self._pydicom_obj[0x3006, 0x00B4].value
            elif isinstance(self._pydicom_obj[0x3006, 0x00B4].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x3006, 0x00B4].value]
            else:
                return float(self._pydicom_obj[0x3006, 0x00B4].value)
        else:
            return None

    @property
    def roi_physical_property(self):
        if (0x3006, 0x00B2) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3006, 0x00B2].value, BaseTag):
                return self._pydicom_obj[0x3006, 0x00B2].value
            elif isinstance(self._pydicom_obj[0x3006, 0x00B2].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3006, 0x00B2].value]
            else:
                return self._pydicom_obj[0x3006, 0x00B2].value
        else:
            return None

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "roi_physical_property_value: %s\n" % (
            self.roi_physical_property_value
        )
        to_ret_str += "roi_physical_property: %s\n" % (self.roi_physical_property)
        return to_ret_str


class VICRTStructureRTROIIdentificationCodeAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTStructureRTROIObservationsAutoDicom"

    @property
    def code_value(self):
        if (0x0008, 0x0100) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0100].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0100].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0100].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0100].value]
            else:
                return self._pydicom_obj[0x0008, 0x0100].value
        else:
            return None

    @property
    def mapping_resource_name(self):
        if (0x0008, 0x0122) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0122].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0122].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0122].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0122].value]
            else:
                return self._pydicom_obj[0x0008, 0x0122].value
        else:
            return None

    @property
    def context_uid(self):
        if (0x0008, 0x0117) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0117].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0117].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0117].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0117].value]
            else:
                return self._pydicom_obj[0x0008, 0x0117].value
        else:
            return None

    @property
    def mapping_resource_uid(self):
        if (0x0008, 0x0118) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0118].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0118].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0118].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0118].value]
            else:
                return self._pydicom_obj[0x0008, 0x0118].value
        else:
            return None

    @property
    def code_meaning(self):
        if (0x0008, 0x0104) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0104].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0104].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0104].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0104].value]
            else:
                return self._pydicom_obj[0x0008, 0x0104].value
        else:
            return None

    @property
    def mapping_resource(self):
        if (0x0008, 0x0105) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0105].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0105].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0105].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0105].value]
            else:
                return self._pydicom_obj[0x0008, 0x0105].value
        else:
            return None

    @property
    def coding_scheme_designator(self):
        if (0x0008, 0x0102) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0102].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0102].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0102].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0102].value]
            else:
                return self._pydicom_obj[0x0008, 0x0102].value
        else:
            return None

    @property
    def coding_scheme_version(self):
        if (0x0008, 0x0103) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0103].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0103].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0103].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0103].value]
            else:
                return self._pydicom_obj[0x0008, 0x0103].value
        else:
            return None

    @property
    def context_group_version(self):
        if (0x0008, 0x0106) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0106].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0106].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0106].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0106].value]
            else:
                return self._pydicom_obj[0x0008, 0x0106].value
        else:
            return None

    @property
    def context_identifier(self):
        if (0x0008, 0x010F) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x010F].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x010F].value
            elif isinstance(self._pydicom_obj[0x0008, 0x010F].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x010F].value]
            else:
                return self._pydicom_obj[0x0008, 0x010F].value
        else:
            return None

    @property
    def equivalent_code_sequence(self):
        val = self._pydicom_obj[0x0008, 0x0121].value
        if val == "None" or val is None:
            return None
        else:
            return [VICRTStructureEquivalentCodeAutoDicom(s) for s in val]

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "code_value: %s\n" % (self.code_value)
        to_ret_str += "mapping_resource_name: %s\n" % (self.mapping_resource_name)
        to_ret_str += "context_uid: %s\n" % (self.context_uid)
        to_ret_str += "mapping_resource_uid: %s\n" % (self.mapping_resource_uid)
        to_ret_str += "code_meaning: %s\n" % (self.code_meaning)
        to_ret_str += "mapping_resource: %s\n" % (self.mapping_resource)
        to_ret_str += "coding_scheme_designator: %s\n" % (self.coding_scheme_designator)
        to_ret_str += "coding_scheme_version: %s\n" % (self.coding_scheme_version)
        to_ret_str += "context_group_version: %s\n" % (self.context_group_version)
        to_ret_str += "context_identifier: %s\n" % (self.context_identifier)
        to_ret_str += "equivalent_code_sequence: %s\n" % (self.equivalent_code_sequence)
        return to_ret_str


class VICRTStructureEquivalentCodeAutoDicom(PythonAutoDicom):
    description = (
        "AutoDicom inner class of VICRTStructureRTROIIdentificationCodeAutoDicom"
    )

    @property
    def code_value(self):
        if (0x0008, 0x0100) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0100].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0100].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0100].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0100].value]
            else:
                return self._pydicom_obj[0x0008, 0x0100].value
        else:
            return None

    @property
    def mapping_resource_name(self):
        if (0x0008, 0x0122) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0122].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0122].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0122].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0122].value]
            else:
                return self._pydicom_obj[0x0008, 0x0122].value
        else:
            return None

    @property
    def context_uid(self):
        if (0x0008, 0x0117) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0117].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0117].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0117].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0117].value]
            else:
                return self._pydicom_obj[0x0008, 0x0117].value
        else:
            return None

    @property
    def mapping_resource_uid(self):
        if (0x0008, 0x0118) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0118].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0118].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0118].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0118].value]
            else:
                return self._pydicom_obj[0x0008, 0x0118].value
        else:
            return None

    @property
    def code_meaning(self):
        if (0x0008, 0x0104) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0104].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0104].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0104].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0104].value]
            else:
                return self._pydicom_obj[0x0008, 0x0104].value
        else:
            return None

    @property
    def mapping_resource(self):
        if (0x0008, 0x0105) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0105].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0105].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0105].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0105].value]
            else:
                return self._pydicom_obj[0x0008, 0x0105].value
        else:
            return None

    @property
    def coding_scheme_designator(self):
        if (0x0008, 0x0102) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0102].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0102].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0102].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0102].value]
            else:
                return self._pydicom_obj[0x0008, 0x0102].value
        else:
            return None

    @property
    def coding_scheme_version(self):
        if (0x0008, 0x0103) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0103].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0103].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0103].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0103].value]
            else:
                return self._pydicom_obj[0x0008, 0x0103].value
        else:
            return None

    @property
    def context_group_version(self):
        if (0x0008, 0x0106) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0106].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0106].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0106].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0106].value]
            else:
                return self._pydicom_obj[0x0008, 0x0106].value
        else:
            return None

    @property
    def context_identifier(self):
        if (0x0008, 0x010F) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x010F].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x010F].value
            elif isinstance(self._pydicom_obj[0x0008, 0x010F].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x010F].value]
            else:
                return self._pydicom_obj[0x0008, 0x010F].value
        else:
            return None

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "code_value: %s\n" % (self.code_value)
        to_ret_str += "mapping_resource_name: %s\n" % (self.mapping_resource_name)
        to_ret_str += "context_uid: %s\n" % (self.context_uid)
        to_ret_str += "mapping_resource_uid: %s\n" % (self.mapping_resource_uid)
        to_ret_str += "code_meaning: %s\n" % (self.code_meaning)
        to_ret_str += "mapping_resource: %s\n" % (self.mapping_resource)
        to_ret_str += "coding_scheme_designator: %s\n" % (self.coding_scheme_designator)
        to_ret_str += "coding_scheme_version: %s\n" % (self.coding_scheme_version)
        to_ret_str += "context_group_version: %s\n" % (self.context_group_version)
        to_ret_str += "context_identifier: %s\n" % (self.context_identifier)
        return to_ret_str


class VICRTStructureContextGroupIdentificationAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTStructureAutoDicom"

    @property
    def context_uid(self):
        if (0x0008, 0x0117) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0117].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0117].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0117].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0117].value]
            else:
                return self._pydicom_obj[0x0008, 0x0117].value
        else:
            return None

    @property
    def mapping_resource(self):
        if (0x0008, 0x0105) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0105].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0105].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0105].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0105].value]
            else:
                return self._pydicom_obj[0x0008, 0x0105].value
        else:
            return None

    @property
    def context_group_version(self):
        if (0x0008, 0x0106) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0106].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0106].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0106].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0106].value]
            else:
                return self._pydicom_obj[0x0008, 0x0106].value
        else:
            return None

    @property
    def context_identifier(self):
        if (0x0008, 0x010F) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x010F].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x010F].value
            elif isinstance(self._pydicom_obj[0x0008, 0x010F].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x010F].value]
            else:
                return self._pydicom_obj[0x0008, 0x010F].value
        else:
            return None

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "context_uid: %s\n" % (self.context_uid)
        to_ret_str += "mapping_resource: %s\n" % (self.mapping_resource)
        to_ret_str += "context_group_version: %s\n" % (self.context_group_version)
        to_ret_str += "context_identifier: %s\n" % (self.context_identifier)
        return to_ret_str


class VICRTStructureMappingResourceIdentificationAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTStructureAutoDicom"

    @property
    def mapping_resource_uid(self):
        if (0x0008, 0x0118) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0118].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0118].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0118].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0118].value]
            else:
                return self._pydicom_obj[0x0008, 0x0118].value
        else:
            return None

    @property
    def mapping_resource(self):
        if (0x0008, 0x0105) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0105].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0105].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0105].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0105].value]
            else:
                return self._pydicom_obj[0x0008, 0x0105].value
        else:
            return None

    @property
    def mapping_resource_name(self):
        if (0x0008, 0x0122) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0122].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0122].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0122].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0122].value]
            else:
                return self._pydicom_obj[0x0008, 0x0122].value
        else:
            return None

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "mapping_resource_uid: %s\n" % (self.mapping_resource_uid)
        to_ret_str += "mapping_resource: %s\n" % (self.mapping_resource)
        to_ret_str += "mapping_resource_name: %s\n" % (self.mapping_resource_name)
        return to_ret_str
