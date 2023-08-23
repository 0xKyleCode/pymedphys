MONTHLY_EDW_6X = {
    "long name": "Monthly EDW - 6X",
    "slug": "monthly-edw-6x",
    "description": "Monthly EDW for 6X",
    "tests": [
        {"name": "monthly_EDW60IN_6X"},
        {"name": "monthly_EDW60OUT_6X"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_EDW_10X = {
    "long name": "Monthly EDW - 10X",
    "slug": "monthly-edw-10x",
    "description": "Monthly EDW for 10X",
    "tests": [
        {"name": "monthly_EDW60IN_10X"},
        {"name": "monthly_EDW60OUT_10X"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_EDW_15X = {
    "long name": "Monthly EDW - 15X",
    "slug": "monthly-edw-15x",
    "description": "Monthly EDW for 15X",
    "tests": [
        {"name": "monthly_EDW60IN_15X"},
        {"name": "monthly_EDW60OUT_15X"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}


MONTHLY_EDW = {
    "long name": "Monthly EDW",
    "slug": "monthly-edw",
    "description": "Monthly EDW",
    "tests": [
        {"name": "monthly_EDWF_6X"},
        {"name": "monthly_EDWF_10X"},
        {"name": "monthly_EDWF_15X"},
    ],
    "test_lists": [
        {"name": MONTHLY_EDW_6X, "order": 0},
        {"name": MONTHLY_EDW_10X, "order": 2},
        {"name": MONTHLY_EDW_15X, "order": 4},
    ],
    "sublists": [],
    "cycle": [],
}
