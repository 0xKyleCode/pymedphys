MONTHLY_OC_6X = {
    "long name": "Monthly Output Constancy - 6X",
    "slug": "monthly-oc-6x",
    "description": "Monthly Output Constancy for 6X",
    "tests": [
        {"name": "monthly_OC_6X_10x10_1"},
        {"name": "monthly_OC_6X_10x10_2"},
        {"name": "monthly_OC_6X_10x10_3"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}

MONTHLY_OC_10X = {
    "long name": "Monthly Output Constancy - 10X",
    "slug": "monthly-oc-10x",
    "description": "Monthly Output Constancy for 10X",
    "tests": [
        {"name": "monthly_OC_10X_10x10_1"},
        {"name": "monthly_OC_10X_10x10_2"},
        {"name": "monthly_OC_10X_10x10_3"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_OC_10XFFF = {
    "long name": "Monthly Output Constancy - 10XFFF",
    "slug": "monthly-oc-10xfff",
    "description": "Monthly Output Constancy for 10XFFF",
    "tests": [
        {"name": "monthly_OC_10Xfff_10x10_1"},
        {"name": "monthly_OC_10Xfff_10x10_2"},
        {"name": "monthly_OC_10Xfff_10x10_3"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_OC_15X = {
    "long name": "Monthly Output Constancy - 15X",
    "slug": "monthly-oc-15X",
    "description": "Monthly Output Constancy for 15X",
    "tests": [
        {"name": "monthly_OC_15X_10x10_1"},
        {"name": "monthly_OC_15X_10x10_2"},
        {"name": "monthly_OC_15X_10x10_3"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_OC_DOSE = {
    "long name": "Monthly Output Constancy",
    "slug": "monthly-oc",
    "description": "Monthly Output Constancy",
    "tests": [
        {"name": "monthly_OC_6X_10x10_DOSE"},
        {"name": "monthly_OC_10X_10x10_DOSE"},
        {"name": "monthly_OC_10Xfff_10x10_DOSE"},
        {"name": "monthly_OC_15X_10x10_DOSE"},
        {"name": "vifir_tb1_photon_6x_fc"},
        {"name": "viarbutus_tb2_photon_6x_fc"},
        {"name": "vibirch_tb3_photon_6x_fc"},
        {"name": "vicedar_tb4_photon_6x_fc"},
        {"name": "vispruce_tb5_photon_6x_fc"},
        {"name": "vioak_tb6_photon_6x_fc"},
        {"name": "vifir_tb1_photon_10x_fc"},
        {"name": "viarbutus_tb2_photon_10x_fc"},
        {"name": "vibirch_tb3_photon_10x_fc"},
        {"name": "vicedar_tb4_photon_10x_fc"},
        {"name": "vispruce_tb5_photon_10x_fc"},
        {"name": "vioak_tb6_photon_10x_fc"},
        {"name": "vifir_tb1_photon_10xfff_fc"},
        {"name": "viarbutus_tb2_photon_10xfff_fc"},
        {"name": "vibirch_tb3_photon_10xfff_fc"},
        {"name": "vicedar_tb4_photon_10xfff_fc"},
        {"name": "vispruce_tb5_photon_10xfff_fc"},
        {"name": "vioak_tb6_photon_10xfff_fc"},
        {"name": "vifir_tb1_photon_15x_fc"},
        {"name": "viarbutus_tb2_photon_15x_fc"},
        {"name": "vibirch_tb3_photon_15x_fc"},
        {"name": "vicedar_tb4_photon_15x_fc"},
        {"name": "vispruce_tb5_photon_15x_fc"},
        {"name": "vioak_tb6_photon_15x_fc"},
    ],
    "test_lists": [
        {"name": MONTHLY_OC_6X, "order": 0},
        {"name": MONTHLY_OC_10X, "order": 2},
        {"name": MONTHLY_OC_10XFFF, "order": 4},
        {"name": MONTHLY_OC_15X, "order": 6},
    ],
    "sublists": [],
    "cycle": [],
}


MONTHLY_OC = [
    MONTHLY_OC_DOSE,
    MONTHLY_OC_6X,
    MONTHLY_OC_10X,
    MONTHLY_OC_10XFFF,
    MONTHLY_OC_15X,
]
