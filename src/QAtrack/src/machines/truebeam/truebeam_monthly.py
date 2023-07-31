import os
import re
import datetime
from constants.machines import BCCALinac
from machines.machine_template import BCCABaseQA

PHYS_MONTHLY_FILE_RE = r"VI(\D+)_TB\d_(\D\D\D)_(\d\d\d\d)(.*)\.xlsm"


class BCCAMonthlyTruebeamQA(BCCABaseQA):
    @classmethod
    def default_qa_name(cls, machine: str) -> str:
        """
        Returns the default name for a monthly QA sheet for truebeam.

        Args:
            machine (str): The machine name.

        Returns:
            str: The default name for a monthly QA sheet for truebeam.
        """
        return "{}_{}_{}_P.xlsm".format(
            BCCALinac.get_machine_name(machine),
            datetime.datetime.now().strftime("%b").upper(),
            datetime.datetime.now().strftime("%Y"),
        )

    @classmethod
    def is_qa_sheet(cls, file_name: str) -> bool:
        """
        Returns True if the file is a monthly QA sheet for truebeam.

        Args:
            file_name (str): The file name.

        Returns:
            bool: True if the file is a monthly QA sheet for truebeam.
        """
        file_name = os.path.basename(file_name)
        if re.match(PHYS_MONTHLY_FILE_RE, file_name):
            return True
        else:
            return False

    @classmethod
    def get_sheet_info(cls, file_name: str) -> tuple[str, ...]:
        """_summary_

        Args:
            file_name (str): The file name

        Raises:
            RuntimeError: If the file is not a truebeam monthly QA sheet.

        Returns:
            tuple[str, ...]: The machine name, the month, and the year.
        """
        if cls.is_qa_sheet(file_name):
            file_name = os.path.basename(file_name)
            return re.match(PHYS_MONTHLY_FILE_RE, file_name).groups()
        else:
            raise RuntimeError(
                "File %s is not a truebeam monthly QA sheet." % file_name
            )

    @classmethod
    def read_main_sheet(cls, file_name: str):
        """
        Reads the excel sheet and returns a dataframe of main.

        Args:
            file_name (str): The file name.

        Returns:
            dataframe: The dataframe.
        """
        return BCCAReadTruebeamMonthlyQAData().read_all(file_name)
