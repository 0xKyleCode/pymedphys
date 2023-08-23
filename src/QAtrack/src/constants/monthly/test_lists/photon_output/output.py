from constants.monthly.test_lists.photon_output.dmlc import (
    MONTHLY_DMLC,
    MONTHLY_INVALID_DMLC,
)
from constants.monthly.test_lists.photon_output.edw import MONTHLY_EDW
from constants.testlists.general_photon import (
    MONTHLY_CTP_PHOTON,
    MONTHLY_ND_PHOTON,
)
from constants.monthly.test_lists.photon_output.kv_cbct import QUARTERLY_KV_CBCT
from constants.monthly.test_lists.photon_output.oc import MONTHLY_OC_DOSE
from constants.monthly.test_lists.photon_output.tmr import MONTHLY_TMR
from constants.monthly.test_lists.photon_output.vmat import MONTHLY_VMAT


MONTHLY_PHOTON_OUTPUTS = {
    "long name": "Monthly X-ray Output",
    "slug": "monthly-photon-output",
    "description": "Monthly X-ray Output",
    "tests": [],
    "test_lists": [],
    "sublists": [
        {"name": MONTHLY_CTP_PHOTON},
        {"name": MONTHLY_ND_PHOTON},
        {"name": MONTHLY_OC_DOSE},
        {"name": MONTHLY_EDW},
        {"name": MONTHLY_DMLC},
        {"name": MONTHLY_VMAT},
        {"name": MONTHLY_INVALID_DMLC},
        {"name": MONTHLY_TMR},
    ],
    "cycle": [],
}

QUARTERLY_PHOTON_OUTPUTS = {
    "long name": "Monthly X-ray Output (with kV CBCT)",
    "slug": "quarterly-photon-output",
    "description": "Monthly X-ray Output (with kV CBCT)",
    "tests": [],
    "test_lists": [],
    "sublists": [
        *MONTHLY_PHOTON_OUTPUTS["sublists"],
        {"name": QUARTERLY_KV_CBCT},
    ],
    "cycle": [],
}

MONTHLY_PHOTON_OUTPUT_CYCLE = {
    "long name": "Monthly X-ray Output",
    "slug": "monthly-photon-output",
    "description": "Monthly X-ray Output",
    "tests": [],
    "test_lists": [],
    "sublists": [],
    "cycle": [
        {"name": MONTHLY_PHOTON_OUTPUTS},
        {"name": MONTHLY_PHOTON_OUTPUTS},
        {"name": QUARTERLY_PHOTON_OUTPUTS},
    ],
}
