from abc import ABC, abstractmethod


class BCCABaseQA(ABC):
    @abstractmethod
    def default_qa_name(cls, machine: str) -> str:
        """
        Returns the default name for a QA sheet.

        Args:
            machine (str): The machine name

        Returns:
            str: The default name for a QA sheet.
        """
        pass

    @abstractmethod
    def is_qa_sheet(cls, file_name: str) -> bool:
        """
        Returns True if the file is a QA sheet.

        Args:
            file_name (str): The file name

        Returns:
            bool: True if the file is a QA sheet.
        """
        pass

    @abstractmethod
    def get_sheet_info(cls, file_name: str) -> tuple[str, ...]:
        """
        Returns the sheet info.

        Args:
            file_name (str): The file name

        Returns:
            tuple[str, ...]: The sheet info.
        """
        pass
