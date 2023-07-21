from excel.truebeam_monthly.constants.electrons.arbutus import (
    CONSTANTS_ELECTRON_FC_ARBUTUS,
)
from excel.truebeam_monthly.constants.electrons.fir import CONSTANTS_ELECTRON_FC_FIR
from excel.truebeam_monthly.constants.electrons.birch import CONSTANTS_ELECTRON_FC_BIRCH

CONSTANTS_ELECTRON_FC: list = (
    CONSTANTS_ELECTRON_FC_ARBUTUS
    + CONSTANTS_ELECTRON_FC_FIR
    + CONSTANTS_ELECTRON_FC_BIRCH
)
