MONTHLY_DMLC_5MM = {
    "long name": "6X - dMLC Factor - 5mm",
    "slug": "6x-dmlc-factor-5mm",
    "description": "6X - dMLC Factor - 5mm",
    "tests": [
        {"name": "monthly_dmlc_5mm_1"},
        {"name": "monthly_dmlc_5mm_2"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_DMLC_5MM_INT = {
    "long name": "6X - dMLC Factor - 5mm - Interuption",
    "slug": "6x-dmlc-factor-5mm-int",
    "description": "6X - dMLC Factor - 5mm - Interuption",
    "tests": [
        {"name": "monthly_dmlc_5mm_Int_1"},
        {"name": "monthly_dmlc_5mm_Int_2"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}
MONTHLY_DMLC_HOLD = {
    "long name": "6X - dMLC Factor - Hold",
    "slug": "6x-dmlc-factor-hold",
    "description": "6X - dMLC Factor - Hold.\n* Half way through leaf sequence delivery press Beam OFF button on console, then complete delivery",
    "tests": [
        {"name": "monthly_dmlc_Hold_1"},
        {"name": "monthly_dmlc_Hold_2"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_DMLC_PROSTATE = {
    "long name": "6X - dMLC Factor - Prostate",
    "slug": "6x-dmlc-factor-prostate",
    "description": "6X - dMLC Factor - Prostate",
    "tests": [
        {"name": "monthly_dmlc_Prostate_6X_1"},
        {"name": "monthly_dmlc_Prostate_6X_2"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_DMLC_HN = {
    "long name": "6X - dMLC Factor - H&N (Hi Mod)",
    "slug": "6x-dmlc-hn-factor",
    "description": "6X - dMLC Factor - H&N (Hi Mod)",
    "tests": [
        {"name": "monthly_dmlc_HN_1"},
        {"name": "monthly_dmlc_HN_2"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_DMLC = {
    "long name": "6X - dMLC Factor",
    "slug": "6x-dmlc-factor",
    "description": "6X - dMLC Factor",
    "tests": [
        {"name": "monthly_dmlc_5mm_ratio"},
        {"name": "monthly_dmlc_5mm_Int_ratio"},
        {"name": "monthly_dmlc_Hold_ratio"},
        {"name": "monthly_dmlc_Prostate_6X_ratio"},
        {"name": "monthly_dmlc_HN_ratio"},
    ],
    "test_lists": [
        {"name": MONTHLY_DMLC_5MM, "order": 0},
        {"name": MONTHLY_DMLC_5MM_INT, "order": 2},
        {"name": MONTHLY_DMLC_HOLD, "order": 4},
        {"name": MONTHLY_DMLC_PROSTATE, "order": 6},
        {"name": MONTHLY_DMLC_HN, "order": 8},
    ],
    "sublists": [],
    "cycle": [],
}

MONTHLY_INVALID_DMLC = {
    "long name": "6X - Invalid dMLC Sequence",
    "slug": "6x-invalid-dmlc-sequence",
    "description": "6X - Invalid dMLC Sequence",
    "tests": [{"name": "monthly_dmlc_error"}],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}
