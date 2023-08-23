MONTHLY_TMR_6X = {
    "long name": "6X - TMR",
    "slug": "6x-tmr",
    "description": "6X - TMR",
    "tests": [
        {"name": "monthly_TMR_6X_1"},
        {"name": "monthly_TMR_6X_2"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_TMR_10X = {
    "long name": "10X - TMR",
    "slug": "10x-tmr",
    "description": "10X - TMR",
    "tests": [
        {"name": "monthly_TMR_10X_1"},
        {"name": "monthly_TMR_10X_2"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}
MONTHLY_TMR_10XFFF = {
    "long name": "10XFFF - TMR",
    "slug": "10xfff-tmr",
    "description": "10XFFF - TMR",
    "tests": [
        {"name": "monthly_TMR_10fff_1"},
        {"name": "monthly_TMR_10fff_2"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_TMR_15X = {
    "long name": "15X - TMR",
    "slug": "15x-tmr",
    "description": "15X - TMR",
    "tests": [
        {"name": "monthly_TMR_15X_1"},
        {"name": "monthly_TMR_15X_2"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_TMR = {
    "long name": "Monthly TMR",
    "slug": "monthly-tmr",
    "description": "Monthly TMR",
    "tests": [
        {"name": "monthly_TMR_6X"},
        {"name": "monthly_TMR_10X"},
        {"name": "monthly_TMR_10fff"},
        {"name": "monthly_TMR_15X"},
    ],
    "test_lists": [
        {"name": MONTHLY_TMR_6X, "order": 0},
        {"name": MONTHLY_TMR_10X, "order": 2},
        {"name": MONTHLY_TMR_10XFFF, "order": 4},
        {"name": MONTHLY_TMR_15X, "order": 6},
    ],
    "sublists": [],
    "cycle": [],
}
