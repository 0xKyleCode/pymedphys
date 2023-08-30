from abc import ABC, abstractmethod


class BCCABaseQA(ABC):
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
