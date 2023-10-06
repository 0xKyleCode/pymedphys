from pydicom.tag import BaseTag
from pydicom.multival import MultiValue
from pyvic.util.dicom import (
    PythonFileAutoDicom,
    PythonAutoDicom,
    PythonImageFileAutoDicom,
)


class VICCTImageSliceAutoDicom(PythonImageFileAutoDicom):
    description = "VIC CT Dicom format"

    @property
    def image_position_patient(self):
        if (0x0020, 0x0032) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0020, 0x0032].value, BaseTag):
                return self._pydicom_obj[0x0020, 0x0032].value
            elif isinstance(self._pydicom_obj[0x0020, 0x0032].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x0020, 0x0032].value]
            else:
                return float(self._pydicom_obj[0x0020, 0x0032].value)
        else:
            return None

    @property
    def window_width(self):
        if (0x0028, 0x1051) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0028, 0x1051].value, BaseTag):
                return self._pydicom_obj[0x0028, 0x1051].value
            elif isinstance(self._pydicom_obj[0x0028, 0x1051].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x0028, 0x1051].value]
            else:
                return float(self._pydicom_obj[0x0028, 0x1051].value)
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
    def bits_allocated(self):
        if (0x0028, 0x0100) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0028, 0x0100].value, BaseTag):
                return self._pydicom_obj[0x0028, 0x0100].value
            elif isinstance(self._pydicom_obj[0x0028, 0x0100].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0028, 0x0100].value]
            else:
                return self._pydicom_obj[0x0028, 0x0100].value
        else:
            return None

    @property
    def slice_thickness(self):
        if (0x0018, 0x0050) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0018, 0x0050].value, BaseTag):
                return self._pydicom_obj[0x0018, 0x0050].value
            elif isinstance(self._pydicom_obj[0x0018, 0x0050].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x0018, 0x0050].value]
            else:
                return float(self._pydicom_obj[0x0018, 0x0050].value)
        else:
            return None

    @property
    def filter_type(self):
        if (0x0018, 0x1160) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0018, 0x1160].value, BaseTag):
                return self._pydicom_obj[0x0018, 0x1160].value
            elif isinstance(self._pydicom_obj[0x0018, 0x1160].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0018, 0x1160].value]
            else:
                return self._pydicom_obj[0x0018, 0x1160].value
        else:
            return None

    @property
    def slice_location(self):
        if (0x0020, 0x1041) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0020, 0x1041].value, BaseTag):
                return self._pydicom_obj[0x0020, 0x1041].value
            elif isinstance(self._pydicom_obj[0x0020, 0x1041].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x0020, 0x1041].value]
            else:
                return float(self._pydicom_obj[0x0020, 0x1041].value)
        else:
            return None

    @property
    def rescale_slope(self):
        if (0x0028, 0x1053) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0028, 0x1053].value, BaseTag):
                return self._pydicom_obj[0x0028, 0x1053].value
            elif isinstance(self._pydicom_obj[0x0028, 0x1053].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x0028, 0x1053].value]
            else:
                return float(self._pydicom_obj[0x0028, 0x1053].value)
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
    def content_date(self):
        if (0x0008, 0x0023) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0023].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0023].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0023].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0023].value]
            else:
                return self._pydicom_obj[0x0008, 0x0023].value
        else:
            return None

    @property
    def rescale_type(self):
        if (0x0028, 0x1054) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0028, 0x1054].value, BaseTag):
                return self._pydicom_obj[0x0028, 0x1054].value
            elif isinstance(self._pydicom_obj[0x0028, 0x1054].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0028, 0x1054].value]
            else:
                return self._pydicom_obj[0x0028, 0x1054].value
        else:
            return None

    @property
    def irradiation_event_uid(self):
        if (0x0008, 0x3010) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x3010].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x3010].value
            elif isinstance(self._pydicom_obj[0x0008, 0x3010].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x3010].value]
            else:
                return self._pydicom_obj[0x0008, 0x3010].value
        else:
            return None

    @property
    def reconstruction_diameter(self):
        if (0x0018, 0x1100) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0018, 0x1100].value, BaseTag):
                return self._pydicom_obj[0x0018, 0x1100].value
            elif isinstance(self._pydicom_obj[0x0018, 0x1100].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x0018, 0x1100].value]
            else:
                return float(self._pydicom_obj[0x0018, 0x1100].value)
        else:
            return None

    @property
    def photometric_interpretation(self):
        if (0x0028, 0x0004) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0028, 0x0004].value, BaseTag):
                return self._pydicom_obj[0x0028, 0x0004].value
            elif isinstance(self._pydicom_obj[0x0028, 0x0004].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0028, 0x0004].value]
            else:
                return self._pydicom_obj[0x0028, 0x0004].value
        else:
            return None

    @property
    def generator_power(self):
        if (0x0018, 0x1170) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0018, 0x1170].value, BaseTag):
                return self._pydicom_obj[0x0018, 0x1170].value
            elif isinstance(self._pydicom_obj[0x0018, 0x1170].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0018, 0x1170].value]
            else:
                return self._pydicom_obj[0x0018, 0x1170].value
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
    def scan_options(self):
        if (0x0018, 0x0022) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0018, 0x0022].value, BaseTag):
                return self._pydicom_obj[0x0018, 0x0022].value
            elif isinstance(self._pydicom_obj[0x0018, 0x0022].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0018, 0x0022].value]
            else:
                return self._pydicom_obj[0x0018, 0x0022].value
        else:
            return None

    @property
    def image_orientation_patient(self):
        if (0x0020, 0x0037) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0020, 0x0037].value, BaseTag):
                return self._pydicom_obj[0x0020, 0x0037].value
            elif isinstance(self._pydicom_obj[0x0020, 0x0037].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x0020, 0x0037].value]
            else:
                return float(self._pydicom_obj[0x0020, 0x0037].value)
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
    def gantrydetector_tilt(self):
        if (0x0018, 0x1120) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0018, 0x1120].value, BaseTag):
                return self._pydicom_obj[0x0018, 0x1120].value
            elif isinstance(self._pydicom_obj[0x0018, 0x1120].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x0018, 0x1120].value]
            else:
                return float(self._pydicom_obj[0x0018, 0x1120].value)
        else:
            return None

    @property
    def exposure(self):
        if (0x0018, 0x1152) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0018, 0x1152].value, BaseTag):
                return self._pydicom_obj[0x0018, 0x1152].value
            elif isinstance(self._pydicom_obj[0x0018, 0x1152].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0018, 0x1152].value]
            else:
                return self._pydicom_obj[0x0018, 0x1152].value
        else:
            return None

    @property
    def distance_source_to_patient(self):
        if (0x0018, 0x1111) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0018, 0x1111].value, BaseTag):
                return self._pydicom_obj[0x0018, 0x1111].value
            elif isinstance(self._pydicom_obj[0x0018, 0x1111].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x0018, 0x1111].value]
            else:
                return float(self._pydicom_obj[0x0018, 0x1111].value)
        else:
            return None

    @property
    def data_collection_diameter(self):
        if (0x0018, 0x0090) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0018, 0x0090].value, BaseTag):
                return self._pydicom_obj[0x0018, 0x0090].value
            elif isinstance(self._pydicom_obj[0x0018, 0x0090].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x0018, 0x0090].value]
            else:
                return float(self._pydicom_obj[0x0018, 0x0090].value)
        else:
            return None

    @property
    def rotation_direction(self):
        if (0x0018, 0x1140) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0018, 0x1140].value, BaseTag):
                return self._pydicom_obj[0x0018, 0x1140].value
            elif isinstance(self._pydicom_obj[0x0018, 0x1140].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0018, 0x1140].value]
            else:
                return self._pydicom_obj[0x0018, 0x1140].value
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
    def series_time(self):
        if (0x0008, 0x0031) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0031].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0031].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0031].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0031].value]
            else:
                return self._pydicom_obj[0x0008, 0x0031].value
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
    def acquisition_number(self):
        if (0x0020, 0x0012) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0020, 0x0012].value, BaseTag):
                return self._pydicom_obj[0x0020, 0x0012].value
            elif isinstance(self._pydicom_obj[0x0020, 0x0012].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0020, 0x0012].value]
            else:
                return self._pydicom_obj[0x0020, 0x0012].value
        else:
            return None

    @property
    def patient_position(self):
        if (0x0018, 0x5100) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0018, 0x5100].value, BaseTag):
                return self._pydicom_obj[0x0018, 0x5100].value
            elif isinstance(self._pydicom_obj[0x0018, 0x5100].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0018, 0x5100].value]
            else:
                return self._pydicom_obj[0x0018, 0x5100].value
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
    def content_time(self):
        if (0x0008, 0x0033) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0033].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0033].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0033].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0033].value]
            else:
                return self._pydicom_obj[0x0008, 0x0033].value
        else:
            return None

    @property
    def convolution_kernel(self):
        if (0x0018, 0x1210) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0018, 0x1210].value, BaseTag):
                return self._pydicom_obj[0x0018, 0x1210].value
            elif isinstance(self._pydicom_obj[0x0018, 0x1210].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0018, 0x1210].value]
            else:
                return self._pydicom_obj[0x0018, 0x1210].value
        else:
            return None

    @property
    def rows(self):
        if (0x0028, 0x0010) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0028, 0x0010].value, BaseTag):
                return self._pydicom_obj[0x0028, 0x0010].value
            elif isinstance(self._pydicom_obj[0x0028, 0x0010].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0028, 0x0010].value]
            else:
                return self._pydicom_obj[0x0028, 0x0010].value
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
    def bits_stored(self):
        if (0x0028, 0x0101) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0028, 0x0101].value, BaseTag):
                return self._pydicom_obj[0x0028, 0x0101].value
            elif isinstance(self._pydicom_obj[0x0028, 0x0101].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0028, 0x0101].value]
            else:
                return self._pydicom_obj[0x0028, 0x0101].value
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
    def image_type(self):
        if (0x0008, 0x0008) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0008].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0008].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0008].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0008].value]
            else:
                return self._pydicom_obj[0x0008, 0x0008].value
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
    def distance_source_to_detector(self):
        if (0x0018, 0x1110) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0018, 0x1110].value, BaseTag):
                return self._pydicom_obj[0x0018, 0x1110].value
            elif isinstance(self._pydicom_obj[0x0018, 0x1110].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x0018, 0x1110].value]
            else:
                return float(self._pydicom_obj[0x0018, 0x1110].value)
        else:
            return None

    @property
    def xray_tube_current(self):
        if (0x0018, 0x1151) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0018, 0x1151].value, BaseTag):
                return self._pydicom_obj[0x0018, 0x1151].value
            elif isinstance(self._pydicom_obj[0x0018, 0x1151].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0018, 0x1151].value]
            else:
                return self._pydicom_obj[0x0018, 0x1151].value
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
    def series_date(self):
        if (0x0008, 0x0021) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0021].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0021].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0021].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0021].value]
            else:
                return self._pydicom_obj[0x0008, 0x0021].value
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
    def columns(self):
        if (0x0028, 0x0011) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0028, 0x0011].value, BaseTag):
                return self._pydicom_obj[0x0028, 0x0011].value
            elif isinstance(self._pydicom_obj[0x0028, 0x0011].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0028, 0x0011].value]
            else:
                return self._pydicom_obj[0x0028, 0x0011].value
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
    def position_reference_indicator(self):
        if (0x0020, 0x1040) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0020, 0x1040].value, BaseTag):
                return self._pydicom_obj[0x0020, 0x1040].value
            elif isinstance(self._pydicom_obj[0x0020, 0x1040].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0020, 0x1040].value]
            else:
                return self._pydicom_obj[0x0020, 0x1040].value
        else:
            return None

    @property
    def focal_spots(self):
        if (0x0018, 0x1190) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0018, 0x1190].value, BaseTag):
                return self._pydicom_obj[0x0018, 0x1190].value
            elif isinstance(self._pydicom_obj[0x0018, 0x1190].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x0018, 0x1190].value]
            else:
                return float(self._pydicom_obj[0x0018, 0x1190].value)
        else:
            return None

    @property
    def pixel_spacing(self):
        if (0x0028, 0x0030) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0028, 0x0030].value, BaseTag):
                return self._pydicom_obj[0x0028, 0x0030].value
            elif isinstance(self._pydicom_obj[0x0028, 0x0030].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x0028, 0x0030].value]
            else:
                return float(self._pydicom_obj[0x0028, 0x0030].value)
        else:
            return None

    @property
    def pixel_representation(self):
        if (0x0028, 0x0103) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0028, 0x0103].value, BaseTag):
                return self._pydicom_obj[0x0028, 0x0103].value
            elif isinstance(self._pydicom_obj[0x0028, 0x0103].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0028, 0x0103].value]
            else:
                return self._pydicom_obj[0x0028, 0x0103].value
        else:
            return None

    @property
    def kvp(self):
        if (0x0018, 0x0060) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0018, 0x0060].value, BaseTag):
                return self._pydicom_obj[0x0018, 0x0060].value
            elif isinstance(self._pydicom_obj[0x0018, 0x0060].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x0018, 0x0060].value]
            else:
                return float(self._pydicom_obj[0x0018, 0x0060].value)
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
    def table_height(self):
        if (0x0018, 0x1130) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0018, 0x1130].value, BaseTag):
                return self._pydicom_obj[0x0018, 0x1130].value
            elif isinstance(self._pydicom_obj[0x0018, 0x1130].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x0018, 0x1130].value]
            else:
                return float(self._pydicom_obj[0x0018, 0x1130].value)
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
    def window_center(self):
        if (0x0028, 0x1050) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0028, 0x1050].value, BaseTag):
                return self._pydicom_obj[0x0028, 0x1050].value
            elif isinstance(self._pydicom_obj[0x0028, 0x1050].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x0028, 0x1050].value]
            else:
                return float(self._pydicom_obj[0x0028, 0x1050].value)
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
    def high_bit(self):
        if (0x0028, 0x0102) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0028, 0x0102].value, BaseTag):
                return self._pydicom_obj[0x0028, 0x0102].value
            elif isinstance(self._pydicom_obj[0x0028, 0x0102].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0028, 0x0102].value]
            else:
                return self._pydicom_obj[0x0028, 0x0102].value
        else:
            return None

    @property
    def samples_per_pixel(self):
        if (0x0028, 0x0002) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0028, 0x0002].value, BaseTag):
                return self._pydicom_obj[0x0028, 0x0002].value
            elif isinstance(self._pydicom_obj[0x0028, 0x0002].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0028, 0x0002].value]
            else:
                return self._pydicom_obj[0x0028, 0x0002].value
        else:
            return None

    @property
    def exposure_time(self):
        if (0x0018, 0x1150) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0018, 0x1150].value, BaseTag):
                return self._pydicom_obj[0x0018, 0x1150].value
            elif isinstance(self._pydicom_obj[0x0018, 0x1150].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0018, 0x1150].value]
            else:
                return self._pydicom_obj[0x0018, 0x1150].value
        else:
            return None

    @property
    def rescale_intercept(self):
        if (0x0028, 0x1052) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0028, 0x1052].value, BaseTag):
                return self._pydicom_obj[0x0028, 0x1052].value
            elif isinstance(self._pydicom_obj[0x0028, 0x1052].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x0028, 0x1052].value]
            else:
                return float(self._pydicom_obj[0x0028, 0x1052].value)
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

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "image_position_patient: %s\n" % (self.image_position_patient)
        to_ret_str += "window_width: %s\n" % (self.window_width)
        to_ret_str += "study_time: %s\n" % (self.study_time)
        to_ret_str += "bits_allocated: %s\n" % (self.bits_allocated)
        to_ret_str += "slice_thickness: %s\n" % (self.slice_thickness)
        to_ret_str += "filter_type: %s\n" % (self.filter_type)
        to_ret_str += "slice_location: %s\n" % (self.slice_location)
        to_ret_str += "rescale_slope: %s\n" % (self.rescale_slope)
        to_ret_str += "series_instance_uid: %s\n" % (self.series_instance_uid)
        to_ret_str += "modality: %s\n" % (self.modality)
        to_ret_str += "content_date: %s\n" % (self.content_date)
        to_ret_str += "rescale_type: %s\n" % (self.rescale_type)
        to_ret_str += "irradiation_event_uid: %s\n" % (self.irradiation_event_uid)
        to_ret_str += "reconstruction_diameter: %s\n" % (self.reconstruction_diameter)
        to_ret_str += "photometric_interpretation: %s\n" % (
            self.photometric_interpretation
        )
        to_ret_str += "generator_power: %s\n" % (self.generator_power)
        to_ret_str += "accession_number: %s\n" % (self.accession_number)
        to_ret_str += "scan_options: %s\n" % (self.scan_options)
        to_ret_str += "image_orientation_patient: %s\n" % (
            self.image_orientation_patient
        )
        to_ret_str += "instance_creation_date: %s\n" % (self.instance_creation_date)
        to_ret_str += "frame_of_reference_uid: %s\n" % (self.frame_of_reference_uid)
        to_ret_str += "manufacturers_model_name: %s\n" % (self.manufacturers_model_name)
        to_ret_str += "instance_number: %s\n" % (self.instance_number)
        to_ret_str += "gantrydetector_tilt: %s\n" % (self.gantrydetector_tilt)
        to_ret_str += "exposure: %s\n" % (self.exposure)
        to_ret_str += "distance_source_to_patient: %s\n" % (
            self.distance_source_to_patient
        )
        to_ret_str += "data_collection_diameter: %s\n" % (self.data_collection_diameter)
        to_ret_str += "rotation_direction: %s\n" % (self.rotation_direction)
        to_ret_str += "study_id: %s\n" % (self.study_id)
        to_ret_str += "software_versions: %s\n" % (self.software_versions)
        to_ret_str += "series_time: %s\n" % (self.series_time)
        to_ret_str += "referring_physicians_name: %s\n" % (
            self.referring_physicians_name
        )
        to_ret_str += "patients_sex: %s\n" % (self.patients_sex)
        to_ret_str += "patients_name: %s\n" % (self.patients_name)
        to_ret_str += "acquisition_number: %s\n" % (self.acquisition_number)
        to_ret_str += "patient_position: %s\n" % (self.patient_position)
        to_ret_str += "patients_birth_date: %s\n" % (self.patients_birth_date)
        to_ret_str += "content_time: %s\n" % (self.content_time)
        to_ret_str += "convolution_kernel: %s\n" % (self.convolution_kernel)
        to_ret_str += "rows: %s\n" % (self.rows)
        to_ret_str += "patients_birth_time: %s\n" % (self.patients_birth_time)
        to_ret_str += "bits_stored: %s\n" % (self.bits_stored)
        to_ret_str += "specific_character_set: %s\n" % (self.specific_character_set)
        to_ret_str += "image_type: %s\n" % (self.image_type)
        to_ret_str += "study_date: %s\n" % (self.study_date)
        to_ret_str += "distance_source_to_detector: %s\n" % (
            self.distance_source_to_detector
        )
        to_ret_str += "xray_tube_current: %s\n" % (self.xray_tube_current)
        to_ret_str += "study_instance_uid: %s\n" % (self.study_instance_uid)
        to_ret_str += "series_date: %s\n" % (self.series_date)
        to_ret_str += "manufacturer: %s\n" % (self.manufacturer)
        to_ret_str += "columns: %s\n" % (self.columns)
        to_ret_str += "sop_class_uid: %s\n" % (self.sop_class_uid)
        to_ret_str += "position_reference_indicator: %s\n" % (
            self.position_reference_indicator
        )
        to_ret_str += "focal_spots: %s\n" % (self.focal_spots)
        to_ret_str += "pixel_spacing: %s\n" % (self.pixel_spacing)
        to_ret_str += "pixel_representation: %s\n" % (self.pixel_representation)
        to_ret_str += "kvp: %s\n" % (self.kvp)
        to_ret_str += "operators_name: %s\n" % (self.operators_name)
        to_ret_str += "table_height: %s\n" % (self.table_height)
        to_ret_str += "series_number: %s\n" % (self.series_number)
        to_ret_str += "window_center: %s\n" % (self.window_center)
        to_ret_str += "sop_instance_uid: %s\n" % (self.sop_instance_uid)
        to_ret_str += "high_bit: %s\n" % (self.high_bit)
        to_ret_str += "samples_per_pixel: %s\n" % (self.samples_per_pixel)
        to_ret_str += "exposure_time: %s\n" % (self.exposure_time)
        to_ret_str += "rescale_intercept: %s\n" % (self.rescale_intercept)
        to_ret_str += "instance_creation_time: %s\n" % (self.instance_creation_time)
        to_ret_str += "patient_id: %s\n" % (self.patient_id)
        return to_ret_str

    @classmethod
    def from_dicom_file(cls, path, stop_before_pixels=False):
        """
        :rtype: VICCTImageSliceAutoDicom
        """
        try:
            import dicom as pydicom
        except ImportError:
            import pydicom
        dcm_hand = pydicom.read_file(path, stop_before_pixels=stop_before_pixels)
        to_ret = cls(dcm_hand, path)
        return to_ret
