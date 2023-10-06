from test_lists.truebeam.monthly.test_lists.cbct.cnr import MONTHLY_CBCT_CNR
from test_lists.truebeam.monthly.test_lists.cbct.geometry import MONTHLY_CBCT_GEOMETRY
from test_lists.truebeam.monthly.test_lists.cbct.image_quality import (
    MONTHLY_CBCT_IMAGE_QUALITY,
)
from test_lists.truebeam.monthly.test_lists.cbct.resolution import (
    MONTHLY_CBCT_RESOLUTION,
)
from test_lists.truebeam.monthly.test_lists.cbct.sensitometry import (
    MONTHLY_CBCT_SENSITOMETRY,
)
from test_lists.truebeam.monthly.test_lists.cbct.uniformity import (
    MONTHLY_CBCT_UNIFORMITY,
)


MONTHLY_CBCT = {
    "long name": "Monthly CBCT",
    "slug": "monthly-cbct",
    "description": "Monthly CBCT",
    "tests": [],
    "sublists": [
        {"name": MONTHLY_CBCT_IMAGE_QUALITY},
        {"name": MONTHLY_CBCT_GEOMETRY},
        {"name": MONTHLY_CBCT_SENSITOMETRY},
        {"name": MONTHLY_CBCT_RESOLUTION},
        {"name": MONTHLY_CBCT_UNIFORMITY},
        {"name": MONTHLY_CBCT_CNR},
    ],
    "test_lists": [],
    "cycle": [],
}
