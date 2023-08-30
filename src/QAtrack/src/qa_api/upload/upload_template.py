from abc import ABC, abstractmethod
from collections import defaultdict
import os
import pandas as pd
import xlwings as xw


class QATrackUpload(ABC):
    def __init__(self, file_name: str, file_path: str, file_template: str):
        """

        Initialize QATrackUpload class

        Args:
            file_name (str): Name of the file
            file_path (str): Source root/directory of files (can find it if in deeper directory)
            file_template (str): Template of the file (for data grabbing)
        """
        self.file_name = file_name
        self.file_path = file_path
        self.file_template = file_template

    @abstractmethod
    def setup_machine_template(self):
        """
        Setup machine template for QATrack+ API
        """
        pass

    @abstractmethod
    def setup_machine(self):
        """
        Setup machine for QATrack+ API
        """
        pass

    @abstractmethod
    def setup_template_sheet_data(self):
        pass

    def read_excel_sheets(
        self, type: str, template_book: xw.Book, machine_book: xw.Book
    ) -> pd.DataFrame:
        sheet1 = template_book.sheets[f"QATrack_{type}"]
        sheet2 = machine_book.sheets[type]
        data = defaultdict(dict)
        # Iterate through all cells in sheet1
        for row in sheet1.range("A1").expand("table").rows:
            for cell in row:
                # Check if cell is not empty and contains a string
                if (
                    cell.value
                    and isinstance(cell.value, str)
                    and cell.value.startswith("#!")
                ):
                    # Get corresponding value from the same cell in sheet2
                    value = sheet2.range(cell.address).value
                    # Store name and value in the dictionary
                    data[cell.address]["name"] = cell.value[2:]
                    data[cell.address]["value"] = value

        # Turn data into a dataframe
        df = pd.DataFrame(data.values())
        return df

    def find_file_recursive(self, directory, target_filename) -> str:
        """
        Find file recursively in directory

        Args:
            directory (_type_): Target directory
            target_filename (_type_): Target filename

        Returns:
            str: Path to file if found
        """
        for root, dirs, files in os.walk(directory):
            if target_filename in files:
                return os.path.join(root, target_filename)

        # Throw error if not found
        raise FileNotFoundError(f"File {target_filename} not found in {directory}")
