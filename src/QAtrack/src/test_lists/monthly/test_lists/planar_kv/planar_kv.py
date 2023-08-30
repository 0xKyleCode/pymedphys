from test_lists.monthly.test_lists.planar_kv.blade_tracking import (
    MONTHLY_PLANAR_KV_BLADE_TRACKING,
)
from test_lists.monthly.test_lists.planar_kv.field_size import (
    MONTHLY_PLANAR_KV_FIELD_SIZE,
)
from test_lists.monthly.test_lists.planar_kv.image_quality import (
    MONTHLY_PLANAR_KV_IMAGE_QUALITY,
)
from test_lists.monthly.test_lists.planar_kv.kvp_accuracy import (
    MONTHLY_PLANAR_KV_ACCURACY_DOSE,
)


MONTHLY_PLANAR_KV = {
    "long name": "Monthly Planar KV",
    "slug": "monthly-planar-kv",
    "description": "Monthly Planar KV",
    "tests": [],
    "sublists": [
        {"name": MONTHLY_PLANAR_KV_BLADE_TRACKING},
        {"name": MONTHLY_PLANAR_KV_FIELD_SIZE},
        {"name": MONTHLY_PLANAR_KV_IMAGE_QUALITY},
        {"name": MONTHLY_PLANAR_KV_ACCURACY_DOSE},
    ],
    "test_lists": [],
    "cycle": [],
}
