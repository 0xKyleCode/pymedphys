from abc import ABC, abstractmethod
import pandas as pd
import xlwings as xw
from datetime import datetime
from openpyxl.utils import column_index_from_string


class BCCABaseQA(ABC):
    def __init__(self, filename: str, plan_filename: str):
        """
        Constructor for the BCCABaseQA class.

        Args:
            filename (str): The file name for spreadsheet
            plan_filename (str): The plan spreadsheet file name.
        """

        self.filename = filename
        self.plans = self.extract_plan_definitions(plan_filename)
        self.extact_plan_values()

    @abstractmethod
    def is_qa_sheet(self) -> bool:
        """
        Returns True if the file is a QA sheet.


        Returns:
            bool: True if the file is a QA sheet.
        """
        pass

    @abstractmethod
    def get_sheet_info(self) -> tuple[str, ...]:
        """
        Returns the sheet info.



        Returns:
            tuple[str, ...]: The sheet info.
        """
        pass

    def get_date(self, input_month: str, input_year: str) -> datetime:
        """
        Returns the date.

        Args:
            input_month (str): Input shorten month name.
            input_year (str): Input year.

        Returns:
            datetime: The date.
        """

        # Mapping of abbreviated month names to numeric values
        month_mapping = {
            "JAN": 1,
            "FEB": 2,
            "MAR": 3,
            "APR": 4,
            "MAY": 5,
            "JUN": 6,
            "JUL": 7,
            "AUG": 8,
            "SEP": 9,
            "OCT": 10,
            "NOV": 11,
            "DEC": 12,
        }

        # Get the numeric month value from the mapping
        numeric_month = month_mapping[input_month]

        # Create a datetime object using the parsed values
        return datetime(int(input_year), numeric_month, 1).strftime("%B, %Y")

    def extract_plan_definitions(self, plan_filename: str) -> pd.DataFrame:
        """
        Extracts the plan definitions from the plan spreadsheet.

        Args:
            plan_filename (str): The plan spreadsheet file name.

        Returns:
            pd.DataFrame: The plan definitions.
        """
        # Read all sheets into a dictionary of DataFrames
        sheet_dict = pd.read_excel(plan_filename, sheet_name=None)

        # Combine all DataFrames into one
        combined_df = pd.concat(sheet_dict.values(), ignore_index=True)
        return combined_df

    def extact_plan_values(self) -> pd.DataFrame:
        lookup_df = pd.read_excel(self.filename, sheet_name="Data", header=None)
        for index, row in self.plans.iterrows():
            if row["type"] == "constant":
                # Convert cell coordinates to row index and column name
                column_letter = "".join(filter(str.isalpha, row["cell"]))
                row_number = int("".join(filter(str.isdigit, row["cell"])))

                column_name = lookup_df.columns[
                    column_index_from_string(column_letter) - 1
                ]
                # Get the value from the specified cell
                cell_value = lookup_df.loc[row_number - 1, column_name]
                self.plans.at[index, "value"] = cell_value

    def save(self):
        """
        Saves the spreadsheet.
        """
        self.book.save()

    def open(self):
        """
        Opens the spreadsheet.
        """
        self.book = xw.Book(self.filename)

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

    def add_tests_to_main(self):
        """
        Adds the tests to the main spreadsheet.
        """
        self.open()
        sheet_main = self.get_sheet("QATrack_Main")
        sheet_data = self.get_sheet("QATrack_Data")
        for index, plan in self.plans.iterrows():
            if plan["sheet"] == "Main":
                sheet_main.range(plan["cell"]).value = "#!" + plan["short"]
            else:
                sheet_data.range(plan["cell"]).value = "#!" + plan["short"]
        self.save()
        self.close()
