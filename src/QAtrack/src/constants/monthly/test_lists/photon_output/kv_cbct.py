QUARTERLY_HEAD_KV_CBCT = {
    "long name": "Quarterly Head kV CBCT",
    "slug": "quarterly-head-kv-cbct",
    "description": "Quarterly Head kV CBCT",
    "tests": [
        {"name": "dose_index_HEAD"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

QUARTERLY_SPOTLIGHT_KV_CBCT = {
    "long name": "Quarterly Spotlight kV CBCT",
    "slug": "quarterly-spotlight-kv-cbct",
    "description": "Quarterly Spotlight kV CBCT",
    "tests": [
        {"name": "dose_index_SPOTLIGHT"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

QUARTERLY_THORAX_KV_CBCT = {
    "long name": "Quarterly Thorax kV CBCT",
    "slug": "quarterly-thorax-kv-cbct",
    "description": "Quarterly Thorax kV CBCT",
    "tests": [
        {"name": "dose_index_THORAX"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

QUARTERLY_PELVIS_KV_CBCT = {
    "long name": "Quarterly Pelvis kV CBCT",
    "slug": "quarterly-pelvis-kv-cbct",
    "description": "Quarterly Pelvis kV CBCT",
    "tests": [
        {"name": "dose_index_PELVIS"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

QUARTERLY_KV_CBCT = {
    "long name": "Quarterly kV CBCT",
    "slug": "quarterly-kv-cbct",
    "description": "Quarterly kV CBCT",
    "tests": [
        {"name": "dose_index_HEAD_corr"},
        {"name": "dose_index_SPOTLIGHT_corr"},
        {"name": "dose_index_THORAX_corr"},
        {"name": "dose_index_PELVIS_corr"},
    ],
    "test_lists": [
        {"name": QUARTERLY_HEAD_KV_CBCT, "order": 0},
        {"name": QUARTERLY_SPOTLIGHT_KV_CBCT, "order": 2},
        {"name": QUARTERLY_THORAX_KV_CBCT, "order": 4},
        {"name": QUARTERLY_PELVIS_KV_CBCT, "order": 6},
    ],
    "sublists": [],
    "cycle": [],
}
