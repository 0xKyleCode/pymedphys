import openpyxl

from excel.truebeam_monthly.constants.photon_factors import CONSTANTS_PHOTON_FC
from excel.truebeam_monthly.constants.markus import CONSTANTS_MARKUS
from excel.truebeam_monthly.constants.probes import CONSTANTS_PROBES
from excel.truebeam_monthly.constants.electron_factors import CONSTANTS_ELECTRON_FC
from excel.truebeam_monthly.constants.electrometer import CONSTANTS_ELEC


CONSTANTS = (
    CONSTANTS_ELEC
    + CONSTANTS_MARKUS
    + CONSTANTS_PROBES
    + CONSTANTS_PHOTON_FC
    + CONSTANTS_ELECTRON_FC
)


class BCCAReadTruebeamMonthlyQAData:
    @classmethod
    def read_constants(cls, file_name: str):
        """
        Reads the constants from the monthly QA sheet.

        Args:
            file_name (str): The file name.

        Returns:
            dict: The constants.
        """
        wb = openpyxl.load_workbook(file_name, data_only=True)
        ws_data = wb["Data"]
        ws_main = wb["Main"]

        print(CONSTANTS)
