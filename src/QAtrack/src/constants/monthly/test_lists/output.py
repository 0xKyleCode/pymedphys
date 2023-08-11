from constants.monthly.test_lists.general import MONTHLY_CTP_PHOTON, MONTHLY_ND_PHOTON

MONTHLY_OC_6X = {
    "long name": "Monthly Output Constancy - 6X",
    "slug": "monthly-oc-6x",
    "description": "Monthly Output Constancy for 6X",
    "tests": [
        {"name": "OC_6X_10x10_1", "order": 0},
        {"name": "OC_6X_10x10_2", "order": 1},
        {"name": "OC_6X_10x10_3", "order": 2},
    ],
    "test_lists": [],
}

MONTHLY_OC_10X = {
    "long name": "Monthly Output Constancy - 10X",
    "slug": "monthly-oc-10x",
    "description": "Monthly Output Constancy for 10X",
    "tests": [
        {"name": "OC_10X_10x10_1", "order": 0},
        {"name": "OC_10X_10x10_2", "order": 1},
        {"name": "OC_10X_10x10_3", "order": 2},
    ],
    "test_lists": [],
}

MONTHLY_OC_10XFFF = {
    "long name": "Monthly Output Constancy - 10XFFF",
    "slug": "monthly-oc-10xfff",
    "description": "Monthly Output Constancy for 10XFFF",
    "tests": [
        {"name": "OC_10Xfff_10x10_1", "order": 0},
        {"name": "OC_10Xfff_10x10_2", "order": 1},
        {"name": "OC_10Xfff_10x10_3", "order": 2},
    ],
    "test_lists": [],
}

MONTHLY_OC_15X = {
    "long name": "Monthly Output Constancy - 15X",
    "slug": "monthly-oc-15X",
    "description": "Monthly Output Constancy for 15X",
    "tests": [
        {"name": "OC_15X_10x10_1", "order": 0},
        {"name": "OC_15X_10x10_2", "order": 1},
        {"name": "OC_15X_10x10_3", "order": 2},
    ],
    "test_lists": [],
}

MONTHLY_OC_DOSE = {
    "long name": "Monthly Output Constancy",
    "slug": "monthly-oc",
    "description": "Monthly Output Constancy",
    "tests": [
        {"name": "OC_6X_10x10_DOSE", "order": 3},
        {"name": "OC_10X_10x10_DOSE", "order": 5},
        {"name": "OC_10Xfff_10x10_DOSE", "order": 7},
        {"name": "OC_15X_10x10_DOSE", "order": 9},
        {"name": "vifir_tb1_photon_6x_fc", "order": 10},
        {"name": "viarbutus_tb2_photon_6x_fc", "order": 11},
        {"name": "vibirch_tb3_photon_6x_fc", "order": 12},
        {"name": "vicedar_tb4_photon_6x_fc", "order": 13},
        {"name": "vispruce_tb5_photon_6x_fc", "order": 14},
        {"name": "vioak_tb6_photon_6x_fc", "order": 15},
        {"name": "vifir_tb1_photon_10x_fc", "order": 16},
        {"name": "viarbutus_tb2_photon_10x_fc", "order": 17},
        {"name": "vibirch_tb3_photon_10x_fc", "order": 18},
        {"name": "vicedar_tb4_photon_10x_fc", "order": 19},
        {"name": "vispruce_tb5_photon_10x_fc", "order": 20},
        {"name": "vioak_tb6_photon_10x_fc", "order": 21},
        {"name": "vifir_tb1_photon_10xfff_fc", "order": 22},
        {"name": "viarbutus_tb2_photon_10xfff_fc", "order": 23},
        {"name": "vibirch_tb3_photon_10xfff_fc", "order": 24},
        {"name": "vicedar_tb4_photon_10xfff_fc", "order": 25},
        {"name": "vispruce_tb5_photon_10xfff_fc", "order": 26},
        {"name": "vioak_tb6_photon_10xfff_fc", "order": 27},
        {"name": "vifir_tb1_photon_15x_fc", "order": 28},
        {"name": "viarbutus_tb2_photon_15x_fc", "order": 29},
        {"name": "vibirch_tb3_photon_15x_fc", "order": 30},
        {"name": "vicedar_tb4_photon_15x_fc", "order": 31},
        {"name": "vispruce_tb5_photon_15x_fc", "order": 32},
        {"name": "vioak_tb6_photon_15x_fc", "order": 33},
    ],
    "test_lists": [
        {"list": MONTHLY_CTP_PHOTON, "order": 0},
        {"list": MONTHLY_ND_PHOTON, "order": 1},
        {"list": MONTHLY_OC_6X, "order": 2},
        {"list": MONTHLY_OC_10X, "order": 4},
        {"list": MONTHLY_OC_10XFFF, "order": 6},
        {"list": MONTHLY_OC_15X, "order": 8},
    ],
}


MONTHLY_OC = [
    MONTHLY_OC_DOSE,
    MONTHLY_OC_6X,
    MONTHLY_OC_10X,
    MONTHLY_OC_10XFFF,
    MONTHLY_OC_15X,
]
