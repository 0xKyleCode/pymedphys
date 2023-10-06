import os
import re
from qa_machines.linacs import BCCALinac
from qa_machines.machine_template import BCCABaseQA
from qa_tpk.testpack import BCCATestpack

from test_lists.truebeam.test_list_definitions import MONTHLY_TEST_LISTS

PHYS_MONTHLY_FILE_RE = r"VI(\D+)_TB\d_(\D\D\D)_(\d\d\d\d)(.*)\.xlsm"


class BCCAMonthlyTruebeamQA(BCCABaseQA):
    def __init__(self, filename: str, plan_filename: str):
        """
        Constructor for the BCCAMonthlyTruebeamQA class.

        Args:
            filename (str): The file name for spreadsheet / template
            plan_filename (str): The file name for the plan / definitions spreadsheet
        """
        super().__init__(filename, plan_filename)

    def is_electron(self) -> bool:
        """
        Returns True if the QA sheet is for electron.

        Returns:
            bool: True if the QA sheet is for electron.
        """
        info = self.get_machine()
        if info["electron"]:
            return True

        return False

    def make_testpack(self, result: str):
        """
        Makes a testpack.

        Args:
            result (str): The result of the testpack.
        """
        tpk = BCCATestpack().make_test_tpk(self.plans, MONTHLY_TEST_LISTS)
        BCCATestpack().write_test_tpk(tpk, result)

    def get_machine(self) -> dict:
        """
        Returns the machine info.

        Returns:
            dict: The machine info.
        """
        if self.is_qa_sheet():
            machine_info = self.get_sheet_info()
            return BCCALinac.get_machine_info(machine_info[0].lower())

    def is_qa_sheet(self) -> bool:
        """
        Returns True if the file is a monthly QA sheet for truebeam.

        Args:
            file_name (str): The file name.

        Returns:
            bool: True if the file is a monthly QA sheet for truebeam.
        """
        file_name = os.path.basename(self.filename)
        if re.match(PHYS_MONTHLY_FILE_RE, file_name):
            return True
        else:
            return False

    def get_sheet_info(self) -> tuple[str, ...]:
        """_summary_

        Args:
            file_name (str): The file name

        Raises:
            RuntimeError: If the file is not a truebeam monthly QA sheet.

        Returns:
            tuple[str, ...]: The machine name, the month, and the year, and date.
        """
        if self.is_qa_sheet():
            file_name = os.path.basename(self.filename)
            groups = re.match(PHYS_MONTHLY_FILE_RE, file_name).groups()
            date = self.get_date(groups[1], groups[2])
            return (*groups, date)
        else:
            raise RuntimeError(
                "File %s is not a truebeam monthly QA sheet." % file_name
            )
