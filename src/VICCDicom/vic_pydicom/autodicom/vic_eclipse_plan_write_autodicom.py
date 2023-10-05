from __future__ import annotations
from typing import List
from pydicom.tag import BaseTag
from pydicom.multival import MultiValue
from pyvic.util.dicom import (
    PythonAutoDicom,
    PythonImageFileAutoDicom,
    AutoDicomSequence,
)


class VICRTPlanAutoDicom(PythonImageFileAutoDicom):
    description = "VIC Eclipse plan format"

    @property
    def rt_plan_time(self):
        if (0x300A, 0x0007) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0007].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0007].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0007].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0007].value]
            else:
                return self._pydicom_obj[0x300A, 0x0007].value
        else:
            return None

    @rt_plan_time.setter
    def rt_plan_time(self, value):
        self._pydicom_obj[0x300A, 0x0007].value = value

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

    @patients_birth_date.setter
    def patients_birth_date(self, value):
        self._pydicom_obj[0x0010, 0x0030].value = value

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

    @study_instance_uid.setter
    def study_instance_uid(self, value):
        self._pydicom_obj[0x0020, 0x000D].value = value

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

    @patient_id.setter
    def patient_id(self, value):
        self._pydicom_obj[0x0010, 0x0020].value = value

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

    @referring_physicians_name.setter
    def referring_physicians_name(self, value):
        self._pydicom_obj[0x0008, 0x0090].value = value

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

    @patients_name.setter
    def patients_name(self, value):
        self._pydicom_obj[0x0010, 0x0010].value = value

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

    @approval_status.setter
    def approval_status(self, value):
        self._pydicom_obj[0x300E, 0x0002].value = value

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

    @operators_name.setter
    def operators_name(self, value):
        self._pydicom_obj[0x0008, 0x1070].value = value

    @property
    def plan_intent(self):
        if (0x300A, 0x000A) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x000A].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x000A].value
            elif isinstance(self._pydicom_obj[0x300A, 0x000A].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x000A].value]
            else:
                return self._pydicom_obj[0x300A, 0x000A].value
        else:
            return None

    @plan_intent.setter
    def plan_intent(self, value):
        self._pydicom_obj[0x300A, 0x000A].value = value

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

    @sop_instance_uid.setter
    def sop_instance_uid(self, value):
        self._pydicom_obj[0x0008, 0x0018].value = value

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

    @station_name.setter
    def station_name(self, value):
        self._pydicom_obj[0x0008, 0x1010].value = value

    @property
    def rt_plan_date(self):
        if (0x300A, 0x0006) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0006].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0006].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0006].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0006].value]
            else:
                return self._pydicom_obj[0x300A, 0x0006].value
        else:
            return None

    @rt_plan_date.setter
    def rt_plan_date(self, value):
        self._pydicom_obj[0x300A, 0x0006].value = value

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

    @instance_creation_date.setter
    def instance_creation_date(self, value):
        self._pydicom_obj[0x0008, 0x0012].value = value

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

    @patients_sex.setter
    def patients_sex(self, value):
        self._pydicom_obj[0x0010, 0x0040].value = value

    @property
    def private_creator(self):
        if (0x3253, 0x0010) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3253, 0x0010].value, BaseTag):
                return self._pydicom_obj[0x3253, 0x0010].value
            elif isinstance(self._pydicom_obj[0x3253, 0x0010].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3253, 0x0010].value]
            else:
                return self._pydicom_obj[0x3253, 0x0010].value
        else:
            return None

    @private_creator.setter
    def private_creator(self, value):
        self._pydicom_obj[0x3253, 0x0010].value = value

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

    @series_instance_uid.setter
    def series_instance_uid(self, value):
        self._pydicom_obj[0x0020, 0x000E].value = value

    @property
    def rt_plan_label(self):
        if (0x300A, 0x0002) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0002].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0002].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0002].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0002].value]
            else:
                return self._pydicom_obj[0x300A, 0x0002].value
        else:
            return None

    @rt_plan_label.setter
    def rt_plan_label(self, value):
        self._pydicom_obj[0x300A, 0x0002].value = value

    @property
    def data_length_of_the_xml_stream(self):
        if (0x3253, 0x1001) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3253, 0x1001].value, BaseTag):
                return self._pydicom_obj[0x3253, 0x1001].value
            elif isinstance(self._pydicom_obj[0x3253, 0x1001].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3253, 0x1001].value]
            else:
                return self._pydicom_obj[0x3253, 0x1001].value
        else:
            return None

    @data_length_of_the_xml_stream.setter
    def data_length_of_the_xml_stream(self, value):
        self._pydicom_obj[0x3253, 0x1001].value = value

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

    @frame_of_reference_uid.setter
    def frame_of_reference_uid(self, value):
        self._pydicom_obj[0x0020, 0x0052].value = value

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

    @software_versions.setter
    def software_versions(self, value):
        self._pydicom_obj[0x0018, 0x1020].value = value

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

    @manufacturer.setter
    def manufacturer(self, value):
        self._pydicom_obj[0x0008, 0x0070].value = value

    @property
    def xml_stream(self):
        if (0x3253, 0x1000) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3253, 0x1000].value, BaseTag):
                return self._pydicom_obj[0x3253, 0x1000].value
            elif isinstance(self._pydicom_obj[0x3253, 0x1000].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3253, 0x1000].value]
            else:
                return self._pydicom_obj[0x3253, 0x1000].value
        else:
            return None

    @xml_stream.setter
    def xml_stream(self, value):
        self._pydicom_obj[0x3253, 0x1000].value = value

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

    @device_serial_number.setter
    def device_serial_number(self, value):
        self._pydicom_obj[0x0018, 0x1000].value = value

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

    @series_number.setter
    def series_number(self, value):
        self._pydicom_obj[0x0020, 0x0011].value = value

    @property
    def extended_interface_format_tag(self):
        if (0x3253, 0x1002) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3253, 0x1002].value, BaseTag):
                return self._pydicom_obj[0x3253, 0x1002].value
            elif isinstance(self._pydicom_obj[0x3253, 0x1002].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3253, 0x1002].value]
            else:
                return self._pydicom_obj[0x3253, 0x1002].value
        else:
            return None

    @extended_interface_format_tag.setter
    def extended_interface_format_tag(self, value):
        self._pydicom_obj[0x3253, 0x1002].value = value

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

    @sop_class_uid.setter
    def sop_class_uid(self, value):
        self._pydicom_obj[0x0008, 0x0016].value = value

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

    @manufacturers_model_name.setter
    def manufacturers_model_name(self, value):
        self._pydicom_obj[0x0008, 0x1090].value = value

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

    @instance_creation_time.setter
    def instance_creation_time(self, value):
        self._pydicom_obj[0x0008, 0x0013].value = value

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

    @specific_character_set.setter
    def specific_character_set(self, value):
        self._pydicom_obj[0x0008, 0x0005].value = value

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

    @position_reference_indicator.setter
    def position_reference_indicator(self, value):
        self._pydicom_obj[0x0020, 0x1040].value = value

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

    @study_time.setter
    def study_time(self, value):
        self._pydicom_obj[0x0008, 0x0030].value = value

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

    @patients_birth_time.setter
    def patients_birth_time(self, value):
        self._pydicom_obj[0x0010, 0x0032].value = value

    @property
    def rt_plan_geometry(self):
        if (0x300A, 0x000C) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x000C].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x000C].value
            elif isinstance(self._pydicom_obj[0x300A, 0x000C].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x000C].value]
            else:
                return self._pydicom_obj[0x300A, 0x000C].value
        else:
            return None

    @rt_plan_geometry.setter
    def rt_plan_geometry(self, value):
        self._pydicom_obj[0x300A, 0x000C].value = value

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

    @study_id.setter
    def study_id(self, value):
        self._pydicom_obj[0x0020, 0x0010].value = value

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

    @study_date.setter
    def study_date(self, value):
        self._pydicom_obj[0x0008, 0x0020].value = value

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

    @modality.setter
    def modality(self, value):
        self._pydicom_obj[0x0008, 0x0060].value = value

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

    @accession_number.setter
    def accession_number(self, value):
        self._pydicom_obj[0x0008, 0x0050].value = value

    @property
    def patient_setup_sequence(self) -> list[VICRTPlanPatientSetupAutoDicom]:
        val = self._pydicom_obj[0x300A, 0x0180].value
        if val == "None" or val is None:
            return None
        else:
            return AutoDicomSequence(val, VICRTPlanPatientSetupAutoDicom)

    @property
    def tolerance_table_sequence(self) -> list[VICRTPlanToleranceTableAutoDicom]:
        val = self._pydicom_obj[0x300A, 0x0040].value
        if val == "None" or val is None:
            return None
        else:
            return AutoDicomSequence(val, VICRTPlanToleranceTableAutoDicom)

    @property
    def beam_sequence(self) -> list[VICRTPlanBeamAutoDicom]:
        val = self._pydicom_obj[0x300A, 0x00B0].value
        if val == "None" or val is None:
            return None
        else:
            return AutoDicomSequence(val, VICRTPlanBeamAutoDicom)

    @property
    def referenced_structure_set_sequence(
        self,
    ) -> list[VICRTPlanReferencedStructureSetAutoDicom]:
        val = self._pydicom_obj[0x300C, 0x0060].value
        if val == "None" or val is None:
            return None
        else:
            return AutoDicomSequence(val, VICRTPlanReferencedStructureSetAutoDicom)

    @property
    def dose_reference_sequence(self) -> list[VICRTPlanDoseReferenceAutoDicom]:
        val = self._pydicom_obj[0x300A, 0x0010].value
        if val == "None" or val is None:
            return None
        else:
            return AutoDicomSequence(val, VICRTPlanDoseReferenceAutoDicom)

    @property
    def fraction_group_sequence(self) -> list[VICRTPlanFractionGroupAutoDicom]:
        val = self._pydicom_obj[0x300A, 0x0070].value
        if val == "None" or val is None:
            return None
        else:
            return AutoDicomSequence(val, VICRTPlanFractionGroupAutoDicom)

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "rt_plan_time: %s\n" % (self.rt_plan_time)
        to_ret_str += "patients_birth_date: %s\n" % (self.patients_birth_date)
        to_ret_str += "study_instance_uid: %s\n" % (self.study_instance_uid)
        to_ret_str += "patient_id: %s\n" % (self.patient_id)
        to_ret_str += "referring_physicians_name: %s\n" % (
            self.referring_physicians_name
        )
        to_ret_str += "patients_name: %s\n" % (self.patients_name)
        to_ret_str += "approval_status: %s\n" % (self.approval_status)
        to_ret_str += "operators_name: %s\n" % (self.operators_name)
        to_ret_str += "plan_intent: %s\n" % (self.plan_intent)
        to_ret_str += "sop_instance_uid: %s\n" % (self.sop_instance_uid)
        to_ret_str += "station_name: %s\n" % (self.station_name)
        to_ret_str += "rt_plan_date: %s\n" % (self.rt_plan_date)
        to_ret_str += "instance_creation_date: %s\n" % (self.instance_creation_date)
        to_ret_str += "patients_sex: %s\n" % (self.patients_sex)
        to_ret_str += "private_creator: %s\n" % (self.private_creator)
        to_ret_str += "series_instance_uid: %s\n" % (self.series_instance_uid)
        to_ret_str += "rt_plan_label: %s\n" % (self.rt_plan_label)
        to_ret_str += "data_length_of_the_xml_stream: %s\n" % (
            self.data_length_of_the_xml_stream
        )
        to_ret_str += "frame_of_reference_uid: %s\n" % (self.frame_of_reference_uid)
        to_ret_str += "software_versions: %s\n" % (self.software_versions)
        to_ret_str += "manufacturer: %s\n" % (self.manufacturer)
        to_ret_str += "xml_stream: %s\n" % (self.xml_stream)
        to_ret_str += "device_serial_number: %s\n" % (self.device_serial_number)
        to_ret_str += "series_number: %s\n" % (self.series_number)
        to_ret_str += "extended_interface_format_tag: %s\n" % (
            self.extended_interface_format_tag
        )
        to_ret_str += "sop_class_uid: %s\n" % (self.sop_class_uid)
        to_ret_str += "manufacturers_model_name: %s\n" % (self.manufacturers_model_name)
        to_ret_str += "instance_creation_time: %s\n" % (self.instance_creation_time)
        to_ret_str += "specific_character_set: %s\n" % (self.specific_character_set)
        to_ret_str += "position_reference_indicator: %s\n" % (
            self.position_reference_indicator
        )
        to_ret_str += "study_time: %s\n" % (self.study_time)
        to_ret_str += "patients_birth_time: %s\n" % (self.patients_birth_time)
        to_ret_str += "rt_plan_geometry: %s\n" % (self.rt_plan_geometry)
        to_ret_str += "study_id: %s\n" % (self.study_id)
        to_ret_str += "study_date: %s\n" % (self.study_date)
        to_ret_str += "modality: %s\n" % (self.modality)
        to_ret_str += "accession_number: %s\n" % (self.accession_number)
        to_ret_str += "patient_setup_sequence: %s\n" % (self.patient_setup_sequence)
        to_ret_str += "tolerance_table_sequence: %s\n" % (self.tolerance_table_sequence)
        to_ret_str += "beam_sequence: %s\n" % (self.beam_sequence)
        to_ret_str += "referenced_structure_set_sequence: %s\n" % (
            self.referenced_structure_set_sequence
        )
        to_ret_str += "dose_reference_sequence: %s\n" % (self.dose_reference_sequence)
        to_ret_str += "fraction_group_sequence: %s\n" % (self.fraction_group_sequence)
        return to_ret_str

    @classmethod
    def from_dicom_file(cls, path, stop_before_pixels=False):
        """
        :rtype: VICRTPlanAutoDicom
        """
        try:
            import dicom as pydicom
        except ImportError:
            import pydicom
        dcm_hand = pydicom.read_file(path, stop_before_pixels=stop_before_pixels)
        to_ret = cls(dcm_hand, path)
        return to_ret


class VICRTPlanPatientSetupAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTPlanAutoDicom"

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

    @patient_position.setter
    def patient_position(self, value):
        self._pydicom_obj[0x0018, 0x5100].value = value

    @property
    def setup_technique(self):
        if (0x300A, 0x01B0) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x01B0].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x01B0].value
            elif isinstance(self._pydicom_obj[0x300A, 0x01B0].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x01B0].value]
            else:
                return self._pydicom_obj[0x300A, 0x01B0].value
        else:
            return None

    @setup_technique.setter
    def setup_technique(self, value):
        self._pydicom_obj[0x300A, 0x01B0].value = value

    @property
    def patient_setup_number(self):
        if (0x300A, 0x0182) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0182].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0182].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0182].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0182].value]
            else:
                return self._pydicom_obj[0x300A, 0x0182].value
        else:
            return None

    @patient_setup_number.setter
    def patient_setup_number(self, value):
        self._pydicom_obj[0x300A, 0x0182].value = value

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "patient_position: %s\n" % (self.patient_position)
        to_ret_str += "setup_technique: %s\n" % (self.setup_technique)
        to_ret_str += "patient_setup_number: %s\n" % (self.patient_setup_number)
        return to_ret_str


class VICRTPlanToleranceTableAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTPlanAutoDicom"

    @property
    def table_top_longitudinal_position_tolerance(self):
        if (0x300A, 0x0052) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0052].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0052].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0052].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x0052].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x0052].value)
        else:
            return None

    @table_top_longitudinal_position_tolerance.setter
    def table_top_longitudinal_position_tolerance(self, value):
        self._pydicom_obj[0x300A, 0x0052].value = value

    @property
    def tolerance_table_label(self):
        if (0x300A, 0x0043) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0043].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0043].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0043].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0043].value]
            else:
                return self._pydicom_obj[0x300A, 0x0043].value
        else:
            return None

    @tolerance_table_label.setter
    def tolerance_table_label(self, value):
        self._pydicom_obj[0x300A, 0x0043].value = value

    @property
    def patient_support_angle_tolerance(self):
        if (0x300A, 0x004C) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x004C].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x004C].value
            elif isinstance(self._pydicom_obj[0x300A, 0x004C].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x004C].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x004C].value)
        else:
            return None

    @patient_support_angle_tolerance.setter
    def patient_support_angle_tolerance(self, value):
        self._pydicom_obj[0x300A, 0x004C].value = value

    @property
    def gantry_angle_tolerance(self):
        if (0x300A, 0x0044) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0044].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0044].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0044].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x0044].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x0044].value)
        else:
            return None

    @gantry_angle_tolerance.setter
    def gantry_angle_tolerance(self, value):
        self._pydicom_obj[0x300A, 0x0044].value = value

    @property
    def table_top_lateral_position_tolerance(self):
        if (0x300A, 0x0053) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0053].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0053].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0053].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x0053].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x0053].value)
        else:
            return None

    @table_top_lateral_position_tolerance.setter
    def table_top_lateral_position_tolerance(self, value):
        self._pydicom_obj[0x300A, 0x0053].value = value

    @property
    def table_top_vertical_position_tolerance(self):
        if (0x300A, 0x0051) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0051].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0051].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0051].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x0051].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x0051].value)
        else:
            return None

    @table_top_vertical_position_tolerance.setter
    def table_top_vertical_position_tolerance(self, value):
        self._pydicom_obj[0x300A, 0x0051].value = value

    @property
    def beam_limiting_device_angle_tolerance(self):
        if (0x300A, 0x0046) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0046].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0046].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0046].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x0046].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x0046].value)
        else:
            return None

    @beam_limiting_device_angle_tolerance.setter
    def beam_limiting_device_angle_tolerance(self, value):
        self._pydicom_obj[0x300A, 0x0046].value = value

    @property
    def tolerance_table_number(self):
        if (0x300A, 0x0042) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0042].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0042].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0042].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0042].value]
            else:
                return self._pydicom_obj[0x300A, 0x0042].value
        else:
            return None

    @tolerance_table_number.setter
    def tolerance_table_number(self, value):
        self._pydicom_obj[0x300A, 0x0042].value = value

    @property
    def beam_limiting_device_tolerance_sequence(
        self,
    ) -> list[VICRTPlanBeamLimitingDeviceToleranceAutoDicom]:
        val = self._pydicom_obj[0x300A, 0x0048].value
        if val == "None" or val is None:
            return None
        else:
            return AutoDicomSequence(val, VICRTPlanBeamLimitingDeviceToleranceAutoDicom)

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "table_top_longitudinal_position_tolerance: %s\n" % (
            self.table_top_longitudinal_position_tolerance
        )
        to_ret_str += "tolerance_table_label: %s\n" % (self.tolerance_table_label)
        to_ret_str += "patient_support_angle_tolerance: %s\n" % (
            self.patient_support_angle_tolerance
        )
        to_ret_str += "gantry_angle_tolerance: %s\n" % (self.gantry_angle_tolerance)
        to_ret_str += "table_top_lateral_position_tolerance: %s\n" % (
            self.table_top_lateral_position_tolerance
        )
        to_ret_str += "table_top_vertical_position_tolerance: %s\n" % (
            self.table_top_vertical_position_tolerance
        )
        to_ret_str += "beam_limiting_device_angle_tolerance: %s\n" % (
            self.beam_limiting_device_angle_tolerance
        )
        to_ret_str += "tolerance_table_number: %s\n" % (self.tolerance_table_number)
        to_ret_str += "beam_limiting_device_tolerance_sequence: %s\n" % (
            self.beam_limiting_device_tolerance_sequence
        )
        return to_ret_str


class VICRTPlanBeamLimitingDeviceToleranceAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTPlanToleranceTableAutoDicom"

    @property
    def beam_limiting_device_position_tolerance(self):
        if (0x300A, 0x004A) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x004A].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x004A].value
            elif isinstance(self._pydicom_obj[0x300A, 0x004A].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x004A].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x004A].value)
        else:
            return None

    @beam_limiting_device_position_tolerance.setter
    def beam_limiting_device_position_tolerance(self, value):
        self._pydicom_obj[0x300A, 0x004A].value = value

    @property
    def rt_beam_limiting_device_type(self):
        if (0x300A, 0x00B8) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x00B8].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x00B8].value
            elif isinstance(self._pydicom_obj[0x300A, 0x00B8].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x00B8].value]
            else:
                return self._pydicom_obj[0x300A, 0x00B8].value
        else:
            return None

    @rt_beam_limiting_device_type.setter
    def rt_beam_limiting_device_type(self, value):
        self._pydicom_obj[0x300A, 0x00B8].value = value

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "beam_limiting_device_position_tolerance: %s\n" % (
            self.beam_limiting_device_position_tolerance
        )
        to_ret_str += "rt_beam_limiting_device_type: %s\n" % (
            self.rt_beam_limiting_device_type
        )
        return to_ret_str


class VICRTPlanBeamAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTPlanAutoDicom"

    @property
    def number_of_wedges(self):
        if (0x300A, 0x00D0) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x00D0].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x00D0].value
            elif isinstance(self._pydicom_obj[0x300A, 0x00D0].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x00D0].value]
            else:
                return self._pydicom_obj[0x300A, 0x00D0].value
        else:
            return None

    @number_of_wedges.setter
    def number_of_wedges(self, value):
        self._pydicom_obj[0x300A, 0x00D0].value = value

    @property
    def institution_name(self):
        if (0x0008, 0x0080) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x0080].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x0080].value
            elif isinstance(self._pydicom_obj[0x0008, 0x0080].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x0080].value]
            else:
                return self._pydicom_obj[0x0008, 0x0080].value
        else:
            return None

    @institution_name.setter
    def institution_name(self, value):
        self._pydicom_obj[0x0008, 0x0080].value = value

    @property
    def treatment_machine_name(self):
        if (0x300A, 0x00B2) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x00B2].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x00B2].value
            elif isinstance(self._pydicom_obj[0x300A, 0x00B2].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x00B2].value]
            else:
                return self._pydicom_obj[0x300A, 0x00B2].value
        else:
            return None

    @treatment_machine_name.setter
    def treatment_machine_name(self, value):
        self._pydicom_obj[0x300A, 0x00B2].value = value

    @property
    def radiation_type(self):
        if (0x300A, 0x00C6) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x00C6].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x00C6].value
            elif isinstance(self._pydicom_obj[0x300A, 0x00C6].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x00C6].value]
            else:
                return self._pydicom_obj[0x300A, 0x00C6].value
        else:
            return None

    @radiation_type.setter
    def radiation_type(self, value):
        self._pydicom_obj[0x300A, 0x00C6].value = value

    @property
    def beam_number(self):
        if (0x300A, 0x00C0) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x00C0].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x00C0].value
            elif isinstance(self._pydicom_obj[0x300A, 0x00C0].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x00C0].value]
            else:
                return self._pydicom_obj[0x300A, 0x00C0].value
        else:
            return None

    @beam_number.setter
    def beam_number(self, value):
        self._pydicom_obj[0x300A, 0x00C0].value = value

    @property
    def referenced_patient_setup_number(self):
        if (0x300C, 0x006A) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300C, 0x006A].value, BaseTag):
                return self._pydicom_obj[0x300C, 0x006A].value
            elif isinstance(self._pydicom_obj[0x300C, 0x006A].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300C, 0x006A].value]
            else:
                return self._pydicom_obj[0x300C, 0x006A].value
        else:
            return None

    @referenced_patient_setup_number.setter
    def referenced_patient_setup_number(self, value):
        self._pydicom_obj[0x300C, 0x006A].value = value

    @property
    def private_tag_data(self):
        if (0x3285, 0x1000) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3285, 0x1000].value, BaseTag):
                return self._pydicom_obj[0x3285, 0x1000].value
            elif isinstance(self._pydicom_obj[0x3285, 0x1000].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3285, 0x1000].value]
            else:
                return self._pydicom_obj[0x3285, 0x1000].value
        else:
            return None

    @private_tag_data.setter
    def private_tag_data(self, value):
        self._pydicom_obj[0x3285, 0x1000].value = value

    @property
    def referenced_tolerance_table_number(self):
        if (0x300C, 0x00A0) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300C, 0x00A0].value, BaseTag):
                return self._pydicom_obj[0x300C, 0x00A0].value
            elif isinstance(self._pydicom_obj[0x300C, 0x00A0].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300C, 0x00A0].value]
            else:
                return self._pydicom_obj[0x300C, 0x00A0].value
        else:
            return None

    @referenced_tolerance_table_number.setter
    def referenced_tolerance_table_number(self, value):
        self._pydicom_obj[0x300C, 0x00A0].value = value

    @property
    def number_of_compensators(self):
        if (0x300A, 0x00E0) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x00E0].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x00E0].value
            elif isinstance(self._pydicom_obj[0x300A, 0x00E0].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x00E0].value]
            else:
                return self._pydicom_obj[0x300A, 0x00E0].value
        else:
            return None

    @number_of_compensators.setter
    def number_of_compensators(self, value):
        self._pydicom_obj[0x300A, 0x00E0].value = value

    @property
    def number_of_control_points(self):
        if (0x300A, 0x0110) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0110].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0110].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0110].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0110].value]
            else:
                return self._pydicom_obj[0x300A, 0x0110].value
        else:
            return None

    @number_of_control_points.setter
    def number_of_control_points(self, value):
        self._pydicom_obj[0x300A, 0x0110].value = value

    @property
    def beam_type(self):
        if (0x300A, 0x00C4) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x00C4].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x00C4].value
            elif isinstance(self._pydicom_obj[0x300A, 0x00C4].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x00C4].value]
            else:
                return self._pydicom_obj[0x300A, 0x00C4].value
        else:
            return None

    @beam_type.setter
    def beam_type(self, value):
        self._pydicom_obj[0x300A, 0x00C4].value = value

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

    @manufacturer.setter
    def manufacturer(self, value):
        self._pydicom_obj[0x0008, 0x0070].value = value

    @property
    def private_creator(self):
        if (0x3285, 0x0010) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3285, 0x0010].value, BaseTag):
                return self._pydicom_obj[0x3285, 0x0010].value
            elif isinstance(self._pydicom_obj[0x3285, 0x0010].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3285, 0x0010].value]
            else:
                return self._pydicom_obj[0x3285, 0x0010].value
        else:
            return None

    @private_creator.setter
    def private_creator(self, value):
        self._pydicom_obj[0x3285, 0x0010].value = value

    @property
    def number_of_boli(self):
        if (0x300A, 0x00ED) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x00ED].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x00ED].value
            elif isinstance(self._pydicom_obj[0x300A, 0x00ED].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x00ED].value]
            else:
                return self._pydicom_obj[0x300A, 0x00ED].value
        else:
            return None

    @number_of_boli.setter
    def number_of_boli(self, value):
        self._pydicom_obj[0x300A, 0x00ED].value = value

    @property
    def beam_name(self):
        if (0x300A, 0x00C2) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x00C2].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x00C2].value
            elif isinstance(self._pydicom_obj[0x300A, 0x00C2].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x00C2].value]
            else:
                return self._pydicom_obj[0x300A, 0x00C2].value
        else:
            return None

    @beam_name.setter
    def beam_name(self, value):
        self._pydicom_obj[0x300A, 0x00C2].value = value

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

    @device_serial_number.setter
    def device_serial_number(self, value):
        self._pydicom_obj[0x0018, 0x1000].value = value

    @property
    def institutional_department_name(self):
        if (0x0008, 0x1040) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x0008, 0x1040].value, BaseTag):
                return self._pydicom_obj[0x0008, 0x1040].value
            elif isinstance(self._pydicom_obj[0x0008, 0x1040].value, MultiValue):
                return [s for s in self._pydicom_obj[0x0008, 0x1040].value]
            else:
                return self._pydicom_obj[0x0008, 0x1040].value
        else:
            return None

    @institutional_department_name.setter
    def institutional_department_name(self, value):
        self._pydicom_obj[0x0008, 0x1040].value = value

    @property
    def primary_dosimeter_unit(self):
        if (0x300A, 0x00B3) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x00B3].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x00B3].value
            elif isinstance(self._pydicom_obj[0x300A, 0x00B3].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x00B3].value]
            else:
                return self._pydicom_obj[0x300A, 0x00B3].value
        else:
            return None

    @primary_dosimeter_unit.setter
    def primary_dosimeter_unit(self, value):
        self._pydicom_obj[0x300A, 0x00B3].value = value

    @property
    def treatment_delivery_type(self):
        if (0x300A, 0x00CE) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x00CE].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x00CE].value
            elif isinstance(self._pydicom_obj[0x300A, 0x00CE].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x00CE].value]
            else:
                return self._pydicom_obj[0x300A, 0x00CE].value
        else:
            return None

    @treatment_delivery_type.setter
    def treatment_delivery_type(self, value):
        self._pydicom_obj[0x300A, 0x00CE].value = value

    @property
    def final_cumulative_meterset_weight(self):
        if (0x300A, 0x010E) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x010E].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x010E].value
            elif isinstance(self._pydicom_obj[0x300A, 0x010E].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x010E].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x010E].value)
        else:
            return None

    @final_cumulative_meterset_weight.setter
    def final_cumulative_meterset_weight(self, value):
        self._pydicom_obj[0x300A, 0x010E].value = value

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

    @manufacturers_model_name.setter
    def manufacturers_model_name(self, value):
        self._pydicom_obj[0x0008, 0x1090].value = value

    @property
    def number_of_blocks(self):
        if (0x300A, 0x00F0) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x00F0].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x00F0].value
            elif isinstance(self._pydicom_obj[0x300A, 0x00F0].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x00F0].value]
            else:
                return self._pydicom_obj[0x300A, 0x00F0].value
        else:
            return None

    @number_of_blocks.setter
    def number_of_blocks(self, value):
        self._pydicom_obj[0x300A, 0x00F0].value = value

    @property
    def sourceaxis_distance(self):
        if (0x300A, 0x00B4) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x00B4].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x00B4].value
            elif isinstance(self._pydicom_obj[0x300A, 0x00B4].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x00B4].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x00B4].value)
        else:
            return None

    @sourceaxis_distance.setter
    def sourceaxis_distance(self, value):
        self._pydicom_obj[0x300A, 0x00B4].value = value

    @property
    def control_point_sequence(self) -> list[VICRTPlanControlPointAutoDicom]:
        val = self._pydicom_obj[0x300A, 0x0111].value
        if val == "None" or val is None:
            return None
        else:
            return AutoDicomSequence(val, VICRTPlanControlPointAutoDicom)

    @property
    def beam_limiting_device_sequence(
        self,
    ) -> list[VICRTPlanBeamLimitingDeviceAutoDicom]:
        val = self._pydicom_obj[0x300A, 0x00B6].value
        if val == "None" or val is None:
            return None
        else:
            return AutoDicomSequence(val, VICRTPlanBeamLimitingDeviceAutoDicom)

    @property
    def primary_fluence_mode_sequence(
        self,
    ) -> list[VICRTPlanPrimaryFluenceModeAutoDicom]:
        val = self._pydicom_obj[0x3002, 0x0050].value
        if val == "None" or val is None:
            return None
        else:
            return AutoDicomSequence(val, VICRTPlanPrimaryFluenceModeAutoDicom)

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "number_of_wedges: %s\n" % (self.number_of_wedges)
        to_ret_str += "institution_name: %s\n" % (self.institution_name)
        to_ret_str += "treatment_machine_name: %s\n" % (self.treatment_machine_name)
        to_ret_str += "radiation_type: %s\n" % (self.radiation_type)
        to_ret_str += "beam_number: %s\n" % (self.beam_number)
        to_ret_str += "referenced_patient_setup_number: %s\n" % (
            self.referenced_patient_setup_number
        )
        to_ret_str += "private_tag_data: %s\n" % (self.private_tag_data)
        to_ret_str += "referenced_tolerance_table_number: %s\n" % (
            self.referenced_tolerance_table_number
        )
        to_ret_str += "number_of_compensators: %s\n" % (self.number_of_compensators)
        to_ret_str += "number_of_control_points: %s\n" % (self.number_of_control_points)
        to_ret_str += "beam_type: %s\n" % (self.beam_type)
        to_ret_str += "manufacturer: %s\n" % (self.manufacturer)
        to_ret_str += "private_creator: %s\n" % (self.private_creator)
        to_ret_str += "number_of_boli: %s\n" % (self.number_of_boli)
        to_ret_str += "beam_name: %s\n" % (self.beam_name)
        to_ret_str += "device_serial_number: %s\n" % (self.device_serial_number)
        to_ret_str += "institutional_department_name: %s\n" % (
            self.institutional_department_name
        )
        to_ret_str += "primary_dosimeter_unit: %s\n" % (self.primary_dosimeter_unit)
        to_ret_str += "treatment_delivery_type: %s\n" % (self.treatment_delivery_type)
        to_ret_str += "final_cumulative_meterset_weight: %s\n" % (
            self.final_cumulative_meterset_weight
        )
        to_ret_str += "manufacturers_model_name: %s\n" % (self.manufacturers_model_name)
        to_ret_str += "number_of_blocks: %s\n" % (self.number_of_blocks)
        to_ret_str += "sourceaxis_distance: %s\n" % (self.sourceaxis_distance)
        to_ret_str += "control_point_sequence: %s\n" % (self.control_point_sequence)
        to_ret_str += "beam_limiting_device_sequence: %s\n" % (
            self.beam_limiting_device_sequence
        )
        to_ret_str += "primary_fluence_mode_sequence: %s\n" % (
            self.primary_fluence_mode_sequence
        )
        return to_ret_str


class VICRTPlanControlPointAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTPlanBeamAutoDicom"

    @property
    def table_top_vertical_position(self):
        if (0x300A, 0x0128) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0128].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0128].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0128].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x0128].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x0128].value)
        else:
            return None

    @table_top_vertical_position.setter
    def table_top_vertical_position(self, value):
        self._pydicom_obj[0x300A, 0x0128].value = value

    @property
    def table_top_lateral_position(self):
        if (0x300A, 0x012A) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x012A].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x012A].value
            elif isinstance(self._pydicom_obj[0x300A, 0x012A].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x012A].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x012A].value)
        else:
            return None

    @table_top_lateral_position.setter
    def table_top_lateral_position(self, value):
        self._pydicom_obj[0x300A, 0x012A].value = value

    @property
    def table_top_eccentric_rotation_direction(self):
        if (0x300A, 0x0126) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0126].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0126].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0126].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0126].value]
            else:
                return self._pydicom_obj[0x300A, 0x0126].value
        else:
            return None

    @table_top_eccentric_rotation_direction.setter
    def table_top_eccentric_rotation_direction(self, value):
        self._pydicom_obj[0x300A, 0x0126].value = value

    @property
    def beam_limiting_device_angle(self):
        if (0x300A, 0x0120) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0120].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0120].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0120].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x0120].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x0120].value)
        else:
            return None

    @beam_limiting_device_angle.setter
    def beam_limiting_device_angle(self, value):
        self._pydicom_obj[0x300A, 0x0120].value = value

    @property
    def dose_rate_set(self):
        if (0x300A, 0x0115) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0115].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0115].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0115].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x0115].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x0115].value)
        else:
            return None

    @dose_rate_set.setter
    def dose_rate_set(self, value):
        self._pydicom_obj[0x300A, 0x0115].value = value

    @property
    def control_point_index(self):
        if (0x300A, 0x0112) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0112].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0112].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0112].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0112].value]
            else:
                return self._pydicom_obj[0x300A, 0x0112].value
        else:
            return None

    @control_point_index.setter
    def control_point_index(self, value):
        self._pydicom_obj[0x300A, 0x0112].value = value

    @property
    def gantry_rotation_direction(self):
        if (0x300A, 0x011F) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x011F].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x011F].value
            elif isinstance(self._pydicom_obj[0x300A, 0x011F].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x011F].value]
            else:
                return self._pydicom_obj[0x300A, 0x011F].value
        else:
            return None

    @gantry_rotation_direction.setter
    def gantry_rotation_direction(self, value):
        self._pydicom_obj[0x300A, 0x011F].value = value

    @property
    def cumulative_meterset_weight(self):
        if (0x300A, 0x0134) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0134].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0134].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0134].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x0134].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x0134].value)
        else:
            return None

    @cumulative_meterset_weight.setter
    def cumulative_meterset_weight(self, value):
        self._pydicom_obj[0x300A, 0x0134].value = value

    @property
    def table_top_roll_angle(self):
        if (0x300A, 0x0144) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0144].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0144].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0144].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0144].value]
            else:
                return self._pydicom_obj[0x300A, 0x0144].value
        else:
            return None

    @table_top_roll_angle.setter
    def table_top_roll_angle(self, value):
        self._pydicom_obj[0x300A, 0x0144].value = value

    @property
    def isocenter_position(self):
        if (0x300A, 0x012C) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x012C].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x012C].value
            elif isinstance(self._pydicom_obj[0x300A, 0x012C].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x012C].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x012C].value)
        else:
            return None

    @isocenter_position.setter
    def isocenter_position(self, value):
        self._pydicom_obj[0x300A, 0x012C].value = value

    @property
    def patient_support_angle(self):
        if (0x300A, 0x0122) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0122].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0122].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0122].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x0122].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x0122].value)
        else:
            return None

    @patient_support_angle.setter
    def patient_support_angle(self, value):
        self._pydicom_obj[0x300A, 0x0122].value = value

    @property
    def table_top_pitch_angle(self):
        if (0x300A, 0x0140) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0140].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0140].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0140].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0140].value]
            else:
                return self._pydicom_obj[0x300A, 0x0140].value
        else:
            return None

    @table_top_pitch_angle.setter
    def table_top_pitch_angle(self, value):
        self._pydicom_obj[0x300A, 0x0140].value = value

    @property
    def table_top_pitch_rotation_direction(self):
        if (0x300A, 0x0142) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0142].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0142].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0142].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0142].value]
            else:
                return self._pydicom_obj[0x300A, 0x0142].value
        else:
            return None

    @table_top_pitch_rotation_direction.setter
    def table_top_pitch_rotation_direction(self, value):
        self._pydicom_obj[0x300A, 0x0142].value = value

    @property
    def nominal_beam_energy(self):
        if (0x300A, 0x0114) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0114].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0114].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0114].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x0114].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x0114].value)
        else:
            return None

    @nominal_beam_energy.setter
    def nominal_beam_energy(self, value):
        self._pydicom_obj[0x300A, 0x0114].value = value

    @property
    def table_top_eccentric_angle(self):
        if (0x300A, 0x0125) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0125].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0125].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0125].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x0125].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x0125].value)
        else:
            return None

    @table_top_eccentric_angle.setter
    def table_top_eccentric_angle(self, value):
        self._pydicom_obj[0x300A, 0x0125].value = value

    @property
    def beam_limiting_device_rotation_direction(self):
        if (0x300A, 0x0121) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0121].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0121].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0121].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0121].value]
            else:
                return self._pydicom_obj[0x300A, 0x0121].value
        else:
            return None

    @beam_limiting_device_rotation_direction.setter
    def beam_limiting_device_rotation_direction(self, value):
        self._pydicom_obj[0x300A, 0x0121].value = value

    @property
    def gantry_angle(self):
        if (0x300A, 0x011E) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x011E].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x011E].value
            elif isinstance(self._pydicom_obj[0x300A, 0x011E].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x011E].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x011E].value)
        else:
            return None

    @gantry_angle.setter
    def gantry_angle(self, value):
        self._pydicom_obj[0x300A, 0x011E].value = value

    @property
    def table_top_roll_rotation_direction(self):
        if (0x300A, 0x0146) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0146].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0146].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0146].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0146].value]
            else:
                return self._pydicom_obj[0x300A, 0x0146].value
        else:
            return None

    @table_top_roll_rotation_direction.setter
    def table_top_roll_rotation_direction(self, value):
        self._pydicom_obj[0x300A, 0x0146].value = value

    @property
    def patient_support_rotation_direction(self):
        if (0x300A, 0x0123) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0123].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0123].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0123].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0123].value]
            else:
                return self._pydicom_obj[0x300A, 0x0123].value
        else:
            return None

    @patient_support_rotation_direction.setter
    def patient_support_rotation_direction(self, value):
        self._pydicom_obj[0x300A, 0x0123].value = value

    @property
    def table_top_longitudinal_position(self):
        if (0x300A, 0x0129) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0129].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0129].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0129].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x0129].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x0129].value)
        else:
            return None

    @table_top_longitudinal_position.setter
    def table_top_longitudinal_position(self, value):
        self._pydicom_obj[0x300A, 0x0129].value = value

    @property
    def referenced_dose_reference_sequence(
        self,
    ) -> list[VICRTPlanReferencedDoseReferenceAutoDicom]:
        val = self._pydicom_obj[0x300C, 0x0050].value
        if val == "None" or val is None:
            return None
        else:
            return AutoDicomSequence(val, VICRTPlanReferencedDoseReferenceAutoDicom)

    @property
    def beam_limiting_device_position_sequence(
        self,
    ) -> list[VICRTPlanBeamLimitingDevicePositionAutoDicom]:
        val = self._pydicom_obj[0x300A, 0x011A].value
        if val == "None" or val is None:
            return None
        else:
            return AutoDicomSequence(val, VICRTPlanBeamLimitingDevicePositionAutoDicom)

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "table_top_vertical_position: %s\n" % (
            self.table_top_vertical_position
        )
        to_ret_str += "table_top_lateral_position: %s\n" % (
            self.table_top_lateral_position
        )
        to_ret_str += "table_top_eccentric_rotation_direction: %s\n" % (
            self.table_top_eccentric_rotation_direction
        )
        to_ret_str += "beam_limiting_device_angle: %s\n" % (
            self.beam_limiting_device_angle
        )
        to_ret_str += "dose_rate_set: %s\n" % (self.dose_rate_set)
        to_ret_str += "control_point_index: %s\n" % (self.control_point_index)
        to_ret_str += "gantry_rotation_direction: %s\n" % (
            self.gantry_rotation_direction
        )
        to_ret_str += "cumulative_meterset_weight: %s\n" % (
            self.cumulative_meterset_weight
        )
        to_ret_str += "table_top_roll_angle: %s\n" % (self.table_top_roll_angle)
        to_ret_str += "isocenter_position: %s\n" % (self.isocenter_position)
        to_ret_str += "patient_support_angle: %s\n" % (self.patient_support_angle)
        to_ret_str += "table_top_pitch_angle: %s\n" % (self.table_top_pitch_angle)
        to_ret_str += "table_top_pitch_rotation_direction: %s\n" % (
            self.table_top_pitch_rotation_direction
        )
        to_ret_str += "nominal_beam_energy: %s\n" % (self.nominal_beam_energy)
        to_ret_str += "table_top_eccentric_angle: %s\n" % (
            self.table_top_eccentric_angle
        )
        to_ret_str += "beam_limiting_device_rotation_direction: %s\n" % (
            self.beam_limiting_device_rotation_direction
        )
        to_ret_str += "gantry_angle: %s\n" % (self.gantry_angle)
        to_ret_str += "table_top_roll_rotation_direction: %s\n" % (
            self.table_top_roll_rotation_direction
        )
        to_ret_str += "patient_support_rotation_direction: %s\n" % (
            self.patient_support_rotation_direction
        )
        to_ret_str += "table_top_longitudinal_position: %s\n" % (
            self.table_top_longitudinal_position
        )
        to_ret_str += "referenced_dose_reference_sequence: %s\n" % (
            self.referenced_dose_reference_sequence
        )
        to_ret_str += "beam_limiting_device_position_sequence: %s\n" % (
            self.beam_limiting_device_position_sequence
        )
        return to_ret_str


class VICRTPlanReferencedDoseReferenceAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTPlanControlPointAutoDicom"

    @property
    def cumulative_dose_reference_coefficient(self):
        if (0x300A, 0x010C) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x010C].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x010C].value
            elif isinstance(self._pydicom_obj[0x300A, 0x010C].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x010C].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x010C].value)
        else:
            return None

    @cumulative_dose_reference_coefficient.setter
    def cumulative_dose_reference_coefficient(self, value):
        self._pydicom_obj[0x300A, 0x010C].value = value

    @property
    def referenced_dose_reference_number(self):
        if (0x300C, 0x0051) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300C, 0x0051].value, BaseTag):
                return self._pydicom_obj[0x300C, 0x0051].value
            elif isinstance(self._pydicom_obj[0x300C, 0x0051].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300C, 0x0051].value]
            else:
                return self._pydicom_obj[0x300C, 0x0051].value
        else:
            return None

    @referenced_dose_reference_number.setter
    def referenced_dose_reference_number(self, value):
        self._pydicom_obj[0x300C, 0x0051].value = value

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "cumulative_dose_reference_coefficient: %s\n" % (
            self.cumulative_dose_reference_coefficient
        )
        to_ret_str += "referenced_dose_reference_number: %s\n" % (
            self.referenced_dose_reference_number
        )
        return to_ret_str


class VICRTPlanBeamLimitingDevicePositionAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTPlanControlPointAutoDicom"

    @property
    def rt_beam_limiting_device_type(self):
        if (0x300A, 0x00B8) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x00B8].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x00B8].value
            elif isinstance(self._pydicom_obj[0x300A, 0x00B8].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x00B8].value]
            else:
                return self._pydicom_obj[0x300A, 0x00B8].value
        else:
            return None

    @rt_beam_limiting_device_type.setter
    def rt_beam_limiting_device_type(self, value):
        self._pydicom_obj[0x300A, 0x00B8].value = value

    @property
    def leafjaw_positions(self):
        if (0x300A, 0x011C) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x011C].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x011C].value
            elif isinstance(self._pydicom_obj[0x300A, 0x011C].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x011C].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x011C].value)
        else:
            return None

    @leafjaw_positions.setter
    def leafjaw_positions(self, value):
        self._pydicom_obj[0x300A, 0x011C].value = value

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "rt_beam_limiting_device_type: %s\n" % (
            self.rt_beam_limiting_device_type
        )
        to_ret_str += "leafjaw_positions: %s\n" % (self.leafjaw_positions)
        return to_ret_str


class VICRTPlanBeamLimitingDeviceAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTPlanBeamAutoDicom"

    @property
    def leaf_position_boundaries(self):
        if (0x300A, 0x00BE) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x00BE].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x00BE].value
            elif isinstance(self._pydicom_obj[0x300A, 0x00BE].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x00BE].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x00BE].value)
        else:
            return None

    @leaf_position_boundaries.setter
    def leaf_position_boundaries(self, value):
        self._pydicom_obj[0x300A, 0x00BE].value = value

    @property
    def rt_beam_limiting_device_type(self):
        if (0x300A, 0x00B8) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x00B8].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x00B8].value
            elif isinstance(self._pydicom_obj[0x300A, 0x00B8].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x00B8].value]
            else:
                return self._pydicom_obj[0x300A, 0x00B8].value
        else:
            return None

    @rt_beam_limiting_device_type.setter
    def rt_beam_limiting_device_type(self, value):
        self._pydicom_obj[0x300A, 0x00B8].value = value

    @property
    def number_of_leafjaw_pairs(self):
        if (0x300A, 0x00BC) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x00BC].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x00BC].value
            elif isinstance(self._pydicom_obj[0x300A, 0x00BC].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x00BC].value]
            else:
                return self._pydicom_obj[0x300A, 0x00BC].value
        else:
            return None

    @number_of_leafjaw_pairs.setter
    def number_of_leafjaw_pairs(self, value):
        self._pydicom_obj[0x300A, 0x00BC].value = value

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "leaf_position_boundaries: %s\n" % (self.leaf_position_boundaries)
        to_ret_str += "rt_beam_limiting_device_type: %s\n" % (
            self.rt_beam_limiting_device_type
        )
        to_ret_str += "number_of_leafjaw_pairs: %s\n" % (self.number_of_leafjaw_pairs)
        return to_ret_str


class VICRTPlanPrimaryFluenceModeAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTPlanBeamAutoDicom"

    @property
    def fluence_mode(self):
        if (0x3002, 0x0051) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3002, 0x0051].value, BaseTag):
                return self._pydicom_obj[0x3002, 0x0051].value
            elif isinstance(self._pydicom_obj[0x3002, 0x0051].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3002, 0x0051].value]
            else:
                return self._pydicom_obj[0x3002, 0x0051].value
        else:
            return None

    @fluence_mode.setter
    def fluence_mode(self, value):
        self._pydicom_obj[0x3002, 0x0051].value = value

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "fluence_mode: %s\n" % (self.fluence_mode)
        return to_ret_str


class VICRTPlanReferencedStructureSetAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTPlanAutoDicom"

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

    @referenced_sop_instance_uid.setter
    def referenced_sop_instance_uid(self, value):
        self._pydicom_obj[0x0008, 0x1155].value = value

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

    @referenced_sop_class_uid.setter
    def referenced_sop_class_uid(self, value):
        self._pydicom_obj[0x0008, 0x1150].value = value

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "referenced_sop_instance_uid: %s\n" % (
            self.referenced_sop_instance_uid
        )
        to_ret_str += "referenced_sop_class_uid: %s\n" % (self.referenced_sop_class_uid)
        return to_ret_str


class VICRTPlanDoseReferenceAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTPlanAutoDicom"

    @property
    def dose_reference_uid(self):
        if (0x300A, 0x0013) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0013].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0013].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0013].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0013].value]
            else:
                return self._pydicom_obj[0x300A, 0x0013].value
        else:
            return None

    @dose_reference_uid.setter
    def dose_reference_uid(self, value):
        self._pydicom_obj[0x300A, 0x0013].value = value

    @property
    def dose_reference_number(self):
        if (0x300A, 0x0012) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0012].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0012].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0012].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0012].value]
            else:
                return self._pydicom_obj[0x300A, 0x0012].value
        else:
            return None

    @dose_reference_number.setter
    def dose_reference_number(self, value):
        self._pydicom_obj[0x300A, 0x0012].value = value

    @property
    def private_creator(self):
        if (0x3267, 0x0010) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3267, 0x0010].value, BaseTag):
                return self._pydicom_obj[0x3267, 0x0010].value
            elif isinstance(self._pydicom_obj[0x3267, 0x0010].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3267, 0x0010].value]
            else:
                return self._pydicom_obj[0x3267, 0x0010].value
        else:
            return None

    @private_creator.setter
    def private_creator(self, value):
        self._pydicom_obj[0x3267, 0x0010].value = value

    @property
    def dose_reference_point_coordinates(self):
        if (0x300A, 0x0018) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0018].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0018].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0018].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x0018].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x0018].value)
        else:
            return None

    @dose_reference_point_coordinates.setter
    def dose_reference_point_coordinates(self, value):
        self._pydicom_obj[0x300A, 0x0018].value = value

    @property
    def private_tag_data(self):
        if (0x3267, 0x1000) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3267, 0x1000].value, BaseTag):
                return self._pydicom_obj[0x3267, 0x1000].value
            elif isinstance(self._pydicom_obj[0x3267, 0x1000].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3267, 0x1000].value]
            else:
                return self._pydicom_obj[0x3267, 0x1000].value
        else:
            return None

    @private_tag_data.setter
    def private_tag_data(self, value):
        self._pydicom_obj[0x3267, 0x1000].value = value

    @property
    def target_prescription_dose(self):
        if (0x300A, 0x0026) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0026].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0026].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0026].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x0026].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x0026].value)
        else:
            return None

    @target_prescription_dose.setter
    def target_prescription_dose(self, value):
        self._pydicom_obj[0x300A, 0x0026].value = value

    @property
    def dose_reference_type(self):
        if (0x300A, 0x0020) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0020].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0020].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0020].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0020].value]
            else:
                return self._pydicom_obj[0x300A, 0x0020].value
        else:
            return None

    @dose_reference_type.setter
    def dose_reference_type(self, value):
        self._pydicom_obj[0x300A, 0x0020].value = value

    @property
    def dose_reference_structure_type(self):
        if (0x300A, 0x0014) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0014].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0014].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0014].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0014].value]
            else:
                return self._pydicom_obj[0x300A, 0x0014].value
        else:
            return None

    @dose_reference_structure_type.setter
    def dose_reference_structure_type(self, value):
        self._pydicom_obj[0x300A, 0x0014].value = value

    @property
    def dose_reference_description(self):
        if (0x300A, 0x0016) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0016].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0016].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0016].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0016].value]
            else:
                return self._pydicom_obj[0x300A, 0x0016].value
        else:
            return None

    @dose_reference_description.setter
    def dose_reference_description(self, value):
        self._pydicom_obj[0x300A, 0x0016].value = value

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "dose_reference_uid: %s\n" % (self.dose_reference_uid)
        to_ret_str += "dose_reference_number: %s\n" % (self.dose_reference_number)
        to_ret_str += "private_creator: %s\n" % (self.private_creator)
        to_ret_str += "dose_reference_point_coordinates: %s\n" % (
            self.dose_reference_point_coordinates
        )
        to_ret_str += "private_tag_data: %s\n" % (self.private_tag_data)
        to_ret_str += "target_prescription_dose: %s\n" % (self.target_prescription_dose)
        to_ret_str += "dose_reference_type: %s\n" % (self.dose_reference_type)
        to_ret_str += "dose_reference_structure_type: %s\n" % (
            self.dose_reference_structure_type
        )
        to_ret_str += "dose_reference_description: %s\n" % (
            self.dose_reference_description
        )
        return to_ret_str


class VICRTPlanFractionGroupAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTPlanAutoDicom"

    @property
    def fraction_group_number(self):
        if (0x300A, 0x0071) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0071].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0071].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0071].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0071].value]
            else:
                return self._pydicom_obj[0x300A, 0x0071].value
        else:
            return None

    @fraction_group_number.setter
    def fraction_group_number(self, value):
        self._pydicom_obj[0x300A, 0x0071].value = value

    @property
    def number_of_brachy_application_setups(self):
        if (0x300A, 0x00A0) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x00A0].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x00A0].value
            elif isinstance(self._pydicom_obj[0x300A, 0x00A0].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x00A0].value]
            else:
                return self._pydicom_obj[0x300A, 0x00A0].value
        else:
            return None

    @number_of_brachy_application_setups.setter
    def number_of_brachy_application_setups(self, value):
        self._pydicom_obj[0x300A, 0x00A0].value = value

    @property
    def number_of_fractions_planned(self):
        if (0x300A, 0x0078) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0078].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0078].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0078].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0078].value]
            else:
                return self._pydicom_obj[0x300A, 0x0078].value
        else:
            return None

    @number_of_fractions_planned.setter
    def number_of_fractions_planned(self, value):
        self._pydicom_obj[0x300A, 0x0078].value = value

    @property
    def number_of_beams(self):
        if (0x300A, 0x0080) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0080].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0080].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0080].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300A, 0x0080].value]
            else:
                return self._pydicom_obj[0x300A, 0x0080].value
        else:
            return None

    @number_of_beams.setter
    def number_of_beams(self, value):
        self._pydicom_obj[0x300A, 0x0080].value = value

    @property
    def referenced_beam_sequence(self) -> list[VICRTPlanReferencedBeamAutoDicom]:
        val = self._pydicom_obj[0x300C, 0x0004].value
        if val == "None" or val is None:
            return None
        else:
            return AutoDicomSequence(val, VICRTPlanReferencedBeamAutoDicom)

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "fraction_group_number: %s\n" % (self.fraction_group_number)
        to_ret_str += "number_of_brachy_application_setups: %s\n" % (
            self.number_of_brachy_application_setups
        )
        to_ret_str += "number_of_fractions_planned: %s\n" % (
            self.number_of_fractions_planned
        )
        to_ret_str += "number_of_beams: %s\n" % (self.number_of_beams)
        to_ret_str += "referenced_beam_sequence: %s\n" % (self.referenced_beam_sequence)
        return to_ret_str


class VICRTPlanReferencedBeamAutoDicom(PythonAutoDicom):
    description = "AutoDicom inner class of VICRTPlanFractionGroupAutoDicom"

    @property
    def private_creator(self):
        if (0x3249, 0x0010) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3249, 0x0010].value, BaseTag):
                return self._pydicom_obj[0x3249, 0x0010].value
            elif isinstance(self._pydicom_obj[0x3249, 0x0010].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3249, 0x0010].value]
            else:
                return self._pydicom_obj[0x3249, 0x0010].value
        else:
            return None

    @private_creator.setter
    def private_creator(self, value):
        self._pydicom_obj[0x3249, 0x0010].value = value

    @property
    def beam_dose(self):
        if (0x300A, 0x0084) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0084].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0084].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0084].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x0084].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x0084].value)
        else:
            return None

    @beam_dose.setter
    def beam_dose(self, value):
        self._pydicom_obj[0x300A, 0x0084].value = value

    @property
    def beam_meterset(self):
        if (0x300A, 0x0086) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300A, 0x0086].value, BaseTag):
                return self._pydicom_obj[0x300A, 0x0086].value
            elif isinstance(self._pydicom_obj[0x300A, 0x0086].value, MultiValue):
                return [float(s) for s in self._pydicom_obj[0x300A, 0x0086].value]
            else:
                return float(self._pydicom_obj[0x300A, 0x0086].value)
        else:
            return None

    @beam_meterset.setter
    def beam_meterset(self, value):
        self._pydicom_obj[0x300A, 0x0086].value = value

    @property
    def referenced_beam_number(self):
        if (0x300C, 0x0006) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x300C, 0x0006].value, BaseTag):
                return self._pydicom_obj[0x300C, 0x0006].value
            elif isinstance(self._pydicom_obj[0x300C, 0x0006].value, MultiValue):
                return [s for s in self._pydicom_obj[0x300C, 0x0006].value]
            else:
                return self._pydicom_obj[0x300C, 0x0006].value
        else:
            return None

    @referenced_beam_number.setter
    def referenced_beam_number(self, value):
        self._pydicom_obj[0x300C, 0x0006].value = value

    @property
    def private_tag_data(self):
        if (0x3249, 0x1010) in self._pydicom_obj:
            if isinstance(self._pydicom_obj[0x3249, 0x1010].value, BaseTag):
                return self._pydicom_obj[0x3249, 0x1010].value
            elif isinstance(self._pydicom_obj[0x3249, 0x1010].value, MultiValue):
                return [s for s in self._pydicom_obj[0x3249, 0x1010].value]
            else:
                return self._pydicom_obj[0x3249, 0x1010].value
        else:
            return None

    @private_tag_data.setter
    def private_tag_data(self, value):
        self._pydicom_obj[0x3249, 0x1010].value = value

    def __str__(self):
        to_ret_str = ""
        to_ret_str += "private_creator: %s\n" % (self.private_creator)
        to_ret_str += "beam_dose: %s\n" % (self.beam_dose)
        to_ret_str += "beam_meterset: %s\n" % (self.beam_meterset)
        to_ret_str += "referenced_beam_number: %s\n" % (self.referenced_beam_number)
        to_ret_str += "private_tag_data: %s\n" % (self.private_tag_data)
        return to_ret_str
