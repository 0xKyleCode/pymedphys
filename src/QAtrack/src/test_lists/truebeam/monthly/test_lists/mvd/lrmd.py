MONTHLY_LIGHT_RADIATION_COINCIDENCE_MLC_LIGHT = {
    "long name": "Monthly Light-Radiation Coincidence, MLC Defined (Light)",
    "slug": "monthly-light-radiation-coincidence-mlc-light",
    "description": "Monthly Light-Radiation Coincidence, MLC Defined (Light)",
    "tests": [
        {"name": "monthly_light_coincidence_mlc_x1"},
        {"name": "monthly_light_coincidence_mlc_x2"},
        {"name": "monthly_light_coincidence_mlc_y1"},
        {"name": "monthly_light_coincidence_mlc_y2"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}

MONTHLY_LIGHT_RADIATION_COINCIDENCE_MLC_6X = {
    "long name": "Monthly Light-Radiation Coincidence, MLC Defined (6X)",
    "slug": "monthly-light-radiation-coincidence-mlc-6x",
    "description": "Monthly Light-Radiation Coincidence, MLC Defined (6X)",
    "tests": [
        {"name": "monthly_6x_rad_coincidence_mlc_x1"},
        {"name": "monthly_6x_rad_coincidence_mlc_x1_result"},
        {"name": "monthly_6x_rad_coincidence_mlc_x2"},
        {"name": "monthly_6x_rad_coincidence_mlc_x2_result"},
        {"name": "monthly_6x_rad_coincidence_mlc_y1"},
        {"name": "monthly_6x_rad_coincidence_mlc_y1_result"},
        {"name": "monthly_6x_rad_coincidence_mlc_y2"},
        {"name": "monthly_6x_rad_coincidence_mlc_y2_result"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}

# Combines all the above into one list
MONTHLY_LIGHT_RADIATION_COINCIDENCE_MLC = {
    "long name": "Monthly Light-Radiation Coincidence, MLC Defined",
    "slug": "monthly-light-radiation-coincidence-mlc",
    "description": """<font color="#0070c0">Plan if not Oak: <b>7A_LITERAD.dcm</b>
        <br>Plan if Oak: <b>7A_LITERADHD.dcm</b></font>
        <br><b>SETUP:</b> As per above except MLC-defined field size 20x20cm
        <br> <b>ACQUISITION:</b> as per above
        <br> <b>ANALYSIS:</b> as per above
    """,
    "tests": [],
    "sublists": [],
    "test_lists": [
        {"name": MONTHLY_LIGHT_RADIATION_COINCIDENCE_MLC_LIGHT, "order": 0},
        {"name": MONTHLY_LIGHT_RADIATION_COINCIDENCE_MLC_6X, "order": 1},
    ],
    "cycle": [],
}
