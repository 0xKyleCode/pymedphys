MONTHLY_VMAT_MECHANICAL_GA_0 = {
    "long name": "Monthly VMAT Mechanical (Gantry Angle: 0)",
    "slug": "monthly-vmat-mechanical-ga-0",
    "description": "Monthly VMAT Mechanical (Gantry Angle: 0)",
    "tests": [
        {"name": "monthly_vmat_mechanical_picket_fence_grid_offset_x_0"},
        {"name": "monthly_vmat_mechanical_picket_fence_grid_offset_y_0"},
        {"name": "monthly_vmat_mechanical_picket_fence_grid_offset_distance_0"},
        {"name": "monthly_vmat_mechanical_picket_fence_grid_offset_peak_0"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}

MONTHLY_VMAT_MECHANICAL_GA_90 = {
    "long name": "Monthly VMAT Mechanical (Gantry Angle: 90)",
    "slug": "monthly-vmat-mechanical-ga-90",
    "description": "Monthly VMAT Mechanical (Gantry Angle: 90)",
    "tests": [
        {"name": "monthly_vmat_mechanical_picket_fence_grid_offset_x_90"},
        {"name": "monthly_vmat_mechanical_picket_fence_grid_offset_y_90"},
        {"name": "monthly_vmat_mechanical_picket_fence_grid_offset_distance_90"},
        {"name": "monthly_vmat_mechanical_picket_fence_grid_offset_peak_90"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}

MONTHLY_VMAT_MECHANICAL_GA_270 = {
    "long name": "Monthly VMAT Mechanical (Gantry Angle: 270)",
    "slug": "monthly-vmat-mechanical-ga-270",
    "description": "Monthly VMAT Mechanical (Gantry Angle: 270)",
    "tests": [
        {"name": "monthly_vmat_mechanical_picket_fence_grid_offset_x_270"},
        {"name": "monthly_vmat_mechanical_picket_fence_grid_offset_y_270"},
        {"name": "monthly_vmat_mechanical_picket_fence_grid_offset_distance_270"},
        {"name": "monthly_vmat_mechanical_picket_fence_grid_offset_peak_270"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}

MONTHLY_VMAT_MECHANICAL_GA_180 = {
    "long name": "Monthly VMAT Mechanical (Gantry Angle: 180)",
    "slug": "monthly-vmat-mechanical-ga-180",
    "description": "Monthly VMAT Mechanical (Gantry Angle: 180)",
    "tests": [
        {"name": "monthly_vmat_mechanical_picket_fence_grid_offset_x_180"},
        {"name": "monthly_vmat_mechanical_picket_fence_grid_offset_y_180"},
        {"name": "monthly_vmat_mechanical_picket_fence_grid_offset_distance_180"},
        {"name": "monthly_vmat_mechanical_picket_fence_grid_offset_peak_180"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}

MONTHLY_VMAT_MECHANICAL_GA_VMAT = {
    "long name": "Monthly VMAT Mechanical (Gantry Angle: VMAT)",
    "slug": "monthly-vmat-mechanical-ga-vmat",
    "description": "Monthly VMAT Mechanical (Gantry Angle: VMAT)",
    "tests": [
        {"name": "monthly_vmat_mechanical_picket_fence_grid_offset_x_vmat"},
        {"name": "monthly_vmat_mechanical_picket_fence_grid_offset_y_vmat"},
        {"name": "monthly_vmat_mechanical_picket_fence_grid_offset_distance_vmat"},
        {"name": "monthly_vmat_mechanical_picket_fence_grid_offset_peak_vmat"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}

MONTHLY_VMAT_MECHANICAL_SPEED = {
    "long name": "Monthly VMAT Mechanical Speed",
    "slug": "monthly-vmat-mechanical-speed",
    "description": "Monthly VMAT Mechanical Speed",
    "tests": [
        {"name": "monthly_vmat_mechanical_6x_dr_ga_speed"},
        {"name": "monthly_vmat_mechanical_6x_dr_mlc_speed"},
        {"name": "monthly_vmat_mechanical_10x_dr_ga_speed"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}

MONTHLY_VMAT_MECHANICAL_FLATNESS = {
    "long name": "Monthly VMAT Mechanical Flatness",
    "slug": "monthly-vmat-mechanical-flatness",
    "description": "Monthly VMAT Mechanical Flatness",
    "tests": [
        {"name": "monthly_vmat_mechanical_10xfff_open_flatness_x"},
        {"name": "monthly_vmat_mechanical_10xfff_open_flatness_y"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}

# Combine all the above test lists into one list
MONTHLY_VMAT_MECHANICAL = {
    "long name": "Monthly VMAT Mechanical",
    "slug": "monthly-vmat-mechanical",
    "description": """
<font color="#0070c0">Plan if not Oak: <b>8RA_Mech.dcm</b>
    <br>Plan if Oak: <b>8RA_MechHD.dcm</b></font>
    <br><b>SETUP:</b>  as per above EXCEPT remove Las Vegas phantom
      <br><b>ACQUISITION:</b> Perform all tests for specified DICOMRT file.
      <br><b>ANALYSIS:</b> For Picket fence tests, select field and use WKS tools (ruler, grid for evaluation); otherwise, use PortalQA
    """,
    "tests": [],
    "sublists": [],
    "test_lists": [
        {"name": MONTHLY_VMAT_MECHANICAL_GA_0, "order": 0},
        {"name": MONTHLY_VMAT_MECHANICAL_GA_90, "order": 1},
        {"name": MONTHLY_VMAT_MECHANICAL_GA_270, "order": 2},
        {"name": MONTHLY_VMAT_MECHANICAL_GA_180, "order": 3},
        {"name": MONTHLY_VMAT_MECHANICAL_GA_VMAT, "order": 4},
        {"name": MONTHLY_VMAT_MECHANICAL_SPEED, "order": 5},
        {"name": MONTHLY_VMAT_MECHANICAL_FLATNESS, "order": 6},
    ],
    "cycle": [],
}
