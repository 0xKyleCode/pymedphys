import openpyxl
from dataclasses import replace
import pandas as pd

from excel.truebeam_monthly.constants.photon_factors import CONSTANTS_PHOTON_FC
from excel.truebeam_monthly.constants.markus import CONSTANTS_MARKUS
from excel.truebeam_monthly.constants.probes import CONSTANTS_PROBES
from excel.truebeam_monthly.constants.electron_factors import CONSTANTS_ELECTRON_FC
from excel.truebeam_monthly.constants.electrometer import CONSTANTS_ELEC
from excel.truebeam_monthly.misc.CTP import MISC_CTP
from excel.truebeam_monthly.misc.electrometer import MISC_ELEC
from excel.truebeam_monthly.misc.markus import MISC_MARKUS
from excel.truebeam_monthly.misc.nd import MISC_ND
from excel.truebeam_monthly.misc.pressure import MISC_PRESSURE
from excel.truebeam_monthly.misc.probes import MISC_PROBES
from excel.truebeam_monthly.misc.temperature import MISC_TEMPERATURE


CONSTANTS = (
    CONSTANTS_ELEC
    + CONSTANTS_MARKUS
    + CONSTANTS_PROBES
    + CONSTANTS_PHOTON_FC
    + CONSTANTS_ELECTRON_FC
)

MISC = (
    MISC_ELEC
    + MISC_MARKUS
    + MISC_CTP
    + MISC_ND
    + MISC_PRESSURE
    + MISC_PROBES
    + MISC_TEMPERATURE
)


class BCCAReadTruebeamMonthlyQAData:
    fields = (
        "long",
        "short",
        "description",
        "track",
        "sheet",
        "cell",
        "type",
        "format",
        "calc",
        "repeats",
        "value",
    )

    @classmethod
    def read_constants(cls, file_name: str) -> pd.DataFrame:
        """
        Reads the constants from the monthly QA sheet.

        Args:
            file_name (str): The file name.

        Returns:
            dict: The constants.
        """

        wb = openpyxl.load_workbook(file_name, data_only=True)
        ws_data = wb["Data"]

        constants_data = [
            replace(constant, value=ws_data[constant.cell].value)
            for constant in CONSTANTS
            if constant.sheet == "Data"
        ]

        excel_data_dict = [
            {field: getattr(obj, field) for field in cls.fields}
            for obj in constants_data
        ]

        return pd.DataFrame(excel_data_dict)

    @classmethod
    def read_misc(cls, file_name: str) -> pd.DataFrame:
        """
        Reads the misc from the monthly QA sheet.

        Args:
            file_name (str): The file name.

        Returns:
            dict: The misc.
        """

        wb = openpyxl.load_workbook(file_name, data_only=True)
        ws_main = wb["Main"]

        misc_data = [
            replace(misc, value=ws_main[misc.cell].value)
            for misc in MISC
            if misc.sheet == "Main"
        ]

        excel_data_dict = [
            {field: getattr(obj, field) for field in cls.fields} for obj in misc_data
        ]

        return pd.DataFrame(excel_data_dict)

    @classmethod
    def read_all(cls, file_name: str) -> pd.DataFrame:
        """
        Reads the constants and misc from the monthly QA sheet.

        Args:
            file_name (str): The file name.

        Returns:
            dict: The constants and misc.
        """

        constants = cls.read_constants(file_name)
        misc = cls.read_misc(file_name)

        return pd.concat([constants, misc])
