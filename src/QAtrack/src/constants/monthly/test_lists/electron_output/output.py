from constants.testlists.general_electron import (
    MONTHLY_CTP_ELECTRON,
    MONTHLY_ND_ELECTRON,
)
from constants.monthly.test_lists.electron_output.oc import MONTHLY_OC_ELECTRON_DOSE


MONTHLY_ELECTRON_OUTPUTS = {
    "long name": "Monthly Electron Output",
    "slug": "monthly-electron-output",
    "description": "Monthly Electron Output",
    "tests": [],
    "test_lists": [],
    "sublists": [
        {"name": MONTHLY_CTP_ELECTRON},
        {"name": MONTHLY_ND_ELECTRON},
        {"name": MONTHLY_OC_ELECTRON_DOSE},
    ],
    "cycle": [],
}
