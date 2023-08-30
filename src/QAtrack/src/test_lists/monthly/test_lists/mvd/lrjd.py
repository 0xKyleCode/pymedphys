MONTHLY_LIGHT_RADIATION_COINCIDENCE_JAW_LIGHT = {
    "long name": "Monthly Light-Radiation Coincidence, Jaw Defined (Light)",
    "slug": "monthly-light-radiation-coincidence-jaw-light",
    "description": "Monthly Light-Radiation Coincidence, Jaw Defined (Light)",
    "tests": [
        {"name": "monthly_light_coincidence_jaw_x1"},
        {"name": "monthly_light_coincidence_jaw_x2"},
        {"name": "monthly_light_coincidence_jaw_y1"},
        {"name": "monthly_light_coincidence_jaw_y2"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}

MONTHLY_LIGHT_RADIATION_COINCIDENCE_JAW_6X = {
    "long name": "Monthly Light-Radiation Coincidence, Jaw Defined (6X)",
    "slug": "monthly-light-radiation-coincidence-jaw-6x",
    "description": "Monthly Light-Radiation Coincidence, Jaw Defined (6X)",
    "tests": [
        {"name": "monthly_6x_rad_coincidence_jaw_x1"},
        {"name": "monthly_6x_rad_coincidence_jaw_x1_result"},
        {"name": "monthly_6x_rad_coincidence_jaw_x2"},
        {"name": "monthly_6x_rad_coincidence_jaw_x2_result"},
        {"name": "monthly_6x_rad_coincidence_jaw_y1"},
        {"name": "monthly_6x_rad_coincidence_jaw_y1_result"},
        {"name": "monthly_6x_rad_coincidence_jaw_y2"},
        {"name": "monthly_6x_rad_coincidence_jaw_y2_result"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}

MONTHLY_LIGHT_RADIATION_COINCIDENCE_JAW_10X = {
    "long name": "Monthly Light-Radiation Coincidence, Jaw Defined (10X)",
    "slug": "monthly-light-radiation-coincidence-jaw-10x",
    "description": "Monthly Light-Radiation Coincidence, Jaw Defined (10X)",
    "tests": [
        {"name": "monthly_10x_rad_coincidence_jaw_x1"},
        {"name": "monthly_10x_rad_coincidence_jaw_x1_result"},
        {"name": "monthly_10x_rad_coincidence_jaw_x2"},
        {"name": "monthly_10x_rad_coincidence_jaw_x2_result"},
        {"name": "monthly_10x_rad_coincidence_jaw_y1"},
        {"name": "monthly_10x_rad_coincidence_jaw_y1_result"},
        {"name": "monthly_10x_rad_coincidence_jaw_y2"},
        {"name": "monthly_10x_rad_coincidence_jaw_y2_result"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}

MONTHLY_LIGHT_RADIATION_COINCIDENCE_JAW_15X = {
    "long name": "Monthly Light-Radiation Coincidence, Jaw Defined (15X)",
    "slug": "monthly-light-radiation-coincidence-jaw-15x",
    "description": "Monthly Light-Radiation Coincidence, Jaw Defined (15X)",
    "tests": [
        {"name": "monthly_15x_rad_coincidence_jaw_x1"},
        {"name": "monthly_15x_rad_coincidence_jaw_x1_result"},
        {"name": "monthly_15x_rad_coincidence_jaw_x2"},
        {"name": "monthly_15x_rad_coincidence_jaw_x2_result"},
        {"name": "monthly_15x_rad_coincidence_jaw_y1"},
        {"name": "monthly_15x_rad_coincidence_jaw_y1_result"},
        {"name": "monthly_15x_rad_coincidence_jaw_y2"},
        {"name": "monthly_15x_rad_coincidence_jaw_y2_result"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}

# Combines all the above into one list
MONTHLY_LIGHT_RADIATION_COINCIDENCE_JAW = {
    "long name": "Monthly Light-Radiation Coincidence, Jaw Defined",
    "slug": "monthly-light-radiation-coincidence-jaw",
    "description": r"""<font color="#0070c0">Plan if not Oak: <b>7A_LITERAD.dcm</b>
        <br>Plan if Oak: <b>7A_LITERADHD.dcm</b></font>
        <br><b>SETUP:</b> Gantry 0°, Collimator 0°, Couch 0° <font color="red">(LNG ~ 100 cm)</font>, grid on couch and aligned with mechanical crosshairs @100SSD (use frontpointer), FS 20x20 cm
        <br><b>ACQUISITION:</b> Use <font color="red"><b>MACHINE QA or TREATMENT mode</b></font>, Shared drive\PHYSICS\MachineID\QA\Monthly QA, Acquire EPIs (high quality, single)
        <br><b>ANALYSIS:</b> Use in-house software "PortalQA_TB"; Result status is either PASS or FAIL.
    """,
    "tests": [],
    "sublists": [],
    "test_lists": [
        {"name": MONTHLY_LIGHT_RADIATION_COINCIDENCE_JAW_LIGHT, "order": 0},
        {"name": MONTHLY_LIGHT_RADIATION_COINCIDENCE_JAW_6X, "order": 1},
        {"name": MONTHLY_LIGHT_RADIATION_COINCIDENCE_JAW_10X, "order": 2},
        {"name": MONTHLY_LIGHT_RADIATION_COINCIDENCE_JAW_15X, "order": 3},
    ],
    "cycle": [],
}
