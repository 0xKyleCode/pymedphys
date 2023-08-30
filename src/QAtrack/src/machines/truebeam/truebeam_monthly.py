import os
import re
from test_lists.machines import BCCALinac
from machines.machine_template import BCCABaseQA
from qa_tpk.testpack import BCCATestpack
import xlwings as xw

PHYS_MONTHLY_FILE_RE = r"VI(\D+)_TB\d_(\D\D\D)_(\d\d\d\d)(.*)\.xlsm"


class BCCAMonthlyTruebeamQA(BCCABaseQA):
    def __init__(self, filename: str):
        """
        Constructor for the BCCAMonthlyTruebeamQA class.

        Args:
            filename (str): The file name for spreadsheet
        """

        self.filename = filename
        self.book = xw.Book(self.filename)

    def save(self):
        """
        Saves the spreadsheet.
        """
        self.book.save()

    def close(self):
        """
        Closes the spreadsheet.
        """
        self.book.close()

    def get_sheet(self, sheet_name: str):
        """
        Returns the sheet object.

        Args:
            sheet_name (str): The sheet name.

        Returns:
            sheet: The sheet object.
        """
        return self.book.sheets[sheet_name]

    def get_sheet_names(self):
        """
        Returns the sheet names.

        Returns:
            list: The sheet names.
        """
        return self.book.sheets.names

    def insert_into_sheet(self, sheet_name: str, data: list):
        """
        Inserts data into the sheet.

        Args:
            sheet_name (str): The sheet name.
            data (list): The data to insert.
        """
        sheet = self.book.sheets[sheet_name]
        last_row = sheet.range("A1").end("down").row
        headers = list(data[0].keys())
        for row_num, data_row in enumerate(data, start=last_row + 1):
            for col_num, header in enumerate(headers, start=1):
                sheet.range((row_num, col_num)).value = data_row[header]

    def make_testpack(self, result: str):
        """
        Makes a testpack.

        Args:
            result (str): The result of the testpack.
        """
        tpk = BCCATestpack().make_test_tpk(self.filename)
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
            tuple[str, ...]: The machine name, the month, and the year.
        """
        if self.is_qa_sheet():
            file_name = os.path.basename(self.filename)
            return re.match(PHYS_MONTHLY_FILE_RE, file_name).groups()
        else:
            raise RuntimeError(
                "File %s is not a truebeam monthly QA sheet." % file_name
            )
