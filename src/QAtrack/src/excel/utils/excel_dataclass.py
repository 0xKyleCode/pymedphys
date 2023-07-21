from dataclasses import dataclass
from typing import Union


@dataclass
class ExcelData:
    long: str
    short: str
    description: str
    track: bool
    sheet: str
    cell: str
    type: str
    format: str
    calc: str
    repeats: int
    value: Union[float, str, int, bool]

    def __post_init__(self):
        valid_sheets = {"Main", "Data", "Info"}
        if self.sheet not in valid_sheets:
            raise ValueError(
                f"Invalid sheet {self.sheet}. Valid sheets are {valid_sheets}"
            )

        valid_types = {"measurement", "selection", "calculation", "constant"}
        if self.type not in valid_types:
            raise ValueError(f"Invalid type {self.type}. Valid types are {valid_types}")
