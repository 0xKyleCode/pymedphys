from test_lists.monthly.test_lists.mvd.friction import MONTHLY_FRICTION
from test_lists.monthly.test_lists.mvd.lrjd import (
    MONTHLY_LIGHT_RADIATION_COINCIDENCE_JAW,
)
from test_lists.monthly.test_lists.mvd.lrmd import (
    MONTHLY_LIGHT_RADIATION_COINCIDENCE_MLC,
)
from test_lists.monthly.test_lists.mvd.mv_image_uniformity import (
    MONTHLY_MV_IMAGE_UNIFORMITY,
)
from test_lists.monthly.test_lists.mvd.picket_fence import MONTHLY_PICKET_FENCE
from test_lists.monthly.test_lists.mvd.pips_pro import MONTHLY_PIPS_PRO_MV
from test_lists.monthly.test_lists.mvd.rad_field_edge_alignment import (
    MONTHLY_RADIATION_FIELD_EDGE_ALIGNMENT,
)
from test_lists.monthly.test_lists.mvd.sliding_window import MONTHLY_SLIDING_WINDOW
from test_lists.monthly.test_lists.mvd.vmat import MONTHLY_VMAT_MECHANICAL


MONTHLY_MVD = {
    "long name": "Monthly MVD Measurements",
    "slug": "monthly-mvd",
    "description": "Monthly MVD Measurements",
    "tests": [],
    "sublists": [
        {"name": MONTHLY_LIGHT_RADIATION_COINCIDENCE_JAW},
        {"name": MONTHLY_LIGHT_RADIATION_COINCIDENCE_MLC},
        {"name": MONTHLY_RADIATION_FIELD_EDGE_ALIGNMENT},
        {"name": MONTHLY_MV_IMAGE_UNIFORMITY},
        {"name": MONTHLY_PICKET_FENCE},
        {"name": MONTHLY_SLIDING_WINDOW},
        {"name": MONTHLY_FRICTION},
        {"name": MONTHLY_PIPS_PRO_MV},
        {"name": MONTHLY_VMAT_MECHANICAL},
    ],
    "test_lists": [],
    "cycle": [],
}
