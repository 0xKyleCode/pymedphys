from matplotlib.dates import MONTHLY
from test_lists.monthly.test_lists.cbct.cbct import MONTHLY_CBCT
from test_lists.monthly.test_lists.electron_output.output import (
    MONTHLY_ELECTRON_OUTPUTS,
)
from test_lists.monthly.test_lists.motion.motion import MONTHLY_MOTION
from test_lists.monthly.test_lists.mvd.mvd import MONTHLY_MVD
from test_lists.monthly.test_lists.photon_output.output import (
    MONTHLY_PHOTON_OUTPUTS,
    QUARTERLY_PHOTON_OUTPUTS,
)
from test_lists.monthly.test_lists.planar_kv.planar_kv import MONTHLY_PLANAR_KV
from test_lists.monthly.test_lists.registration.registration import MONTHLY_REGISTRATION


MONTHLY_W_ELECTRON = {
    "long name": "Monthly QA (w/ electron)",
    "slug": "monthly-with-electron",
    "description": "Monthly QA",
    "tests": [],
    "test_lists": [],
    "sublists": [
        *MONTHLY_PHOTON_OUTPUTS["sublists"],
        *MONTHLY_ELECTRON_OUTPUTS["sublists"],
        *MONTHLY_MVD["sublists"],
        *MONTHLY_REGISTRATION["sublists"],
        *MONTHLY_MOTION["sublists"],
    ],
    "cycle": [],
}

MONTHLY_NO_ELECTRON = {
    "long name": "Monthly QA (No electron)",
    "slug": "monthly-with-no-electron",
    "description": "Monthly QA",
    "tests": [],
    "test_lists": [],
    "sublists": [
        *MONTHLY_PHOTON_OUTPUTS["sublists"],
        *MONTHLY_MVD["sublists"],
        *MONTHLY_REGISTRATION["sublists"],
        *MONTHLY_MOTION["sublists"],
    ],
    "cycle": [],
}

QUARTERLY_W_ELECTRON = {
    "long name": "Monthly X-ray Output (with kV CBCT, electrons)",
    "slug": "quarterly-photon-output-w-electron",
    "description": "Monthly X-ray Output (with kV CBCT)",
    "tests": [],
    "test_lists": [],
    "sublists": [
        *QUARTERLY_PHOTON_OUTPUTS["sublists"],
        *MONTHLY_ELECTRON_OUTPUTS["sublists"],
        *MONTHLY_MVD["sublists"],
        *MONTHLY_REGISTRATION["sublists"],
        *MONTHLY_MOTION["sublists"],
        *MONTHLY_PLANAR_KV["sublists"],
        *MONTHLY_CBCT["sublists"],
    ],
    "cycle": [],
}

QUARTERLY_NO_ELECTRON = {
    "long name": "Monthly X-ray Output (with kV CBCT, no electrons)",
    "slug": "quarterly-photon-output-no-electron",
    "description": "Monthly X-ray Output (with kV CBCT)",
    "tests": [],
    "test_lists": [],
    "sublists": [
        *QUARTERLY_PHOTON_OUTPUTS["sublists"],
        *MONTHLY_MVD["sublists"],
        *MONTHLY_REGISTRATION["sublists"],
        *MONTHLY_MOTION["sublists"],
        *MONTHLY_PLANAR_KV["sublists"],
        *MONTHLY_CBCT["sublists"],
    ],
    "cycle": [],
}


MONTHLY_CYCLE_W_ELECTRON = {
    "long name": "Monthly QA (with electrons)",
    "slug": "monthly-w-electron",
    "description": "Monthly QA (with electrons)",
    "tests": [],
    "test_lists": [],
    "sublists": [],
    "cycle": [
        {"name": MONTHLY_W_ELECTRON},
        {"name": MONTHLY_W_ELECTRON},
        {"name": QUARTERLY_W_ELECTRON},
    ],
}

MONTHLY_CYCLE_NO_ELECTRON = {
    "long name": "Monthly QA (no electrons)",
    "slug": "monthly-no-electron",
    "description": "Monthly QA (no electrons)",
    "tests": [],
    "test_lists": [],
    "sublists": [],
    "cycle": [
        {"name": MONTHLY_NO_ELECTRON},
        {"name": MONTHLY_NO_ELECTRON},
        {"name": QUARTERLY_NO_ELECTRON},
    ],
}
