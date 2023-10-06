MONTHLY_REGISTRATION_HEAD = {
    "long name": "Monthly Registration using Varian Cube Phantom - Head CBCT",
    "slug": "monthly-registration-head",
    "description": r"""<font color="#0070c0">Plan: <b>9Registration.dcm</b></font>
    <br><b>SETUP:</b> Gantry 0°, Position indexed registration phantom at couch location H3 and move couch to VRT 10.0, LNG 82.0, LAT 1.0, ROT 0.0.
      <br><b>ACQUISITION:</b> Use <font color="red"><b>TREATMENT</b></font> mode, file directory: Shared drive\PHYSICS\MachineID\QA\Monthly QA.
      <br> Validate phantom setup using Thorax CBCT with 5 cm z-offset, 2D-2D KV- and MV-paired, and kV Marker Match protocols (DO NOT move couch).
      <br> Use 3D auto-registration for CBCT protocol and manual registrations for all KV and MV planar images. If auto-registration fails, use manual.
      <br> Write down Couch Coordinates AFTER Move (cm)
    """,
    "tests": [
        {"name": "monthly_registration_head_cbct_vrt"},
        {"name": "monthly_registration_head_cbct_lng"},
        {"name": "monthly_registration_head_cbct_lat"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_REGISTRATION_THORAX = {
    "long name": "Monthly Registration using Varian Cube Phantom - Thorax CBCT",
    "slug": "monthly-registration-thorax",
    "description": """<font color="#0070c0">Plan: <b>9Registration.dcm</b></font>
    <br><b>SETUP:</b> As above.
    <br><b>ACQUISITION:</b> As above, adjust with auto-registration, DO NOT move couch. Write down suggested couch moves.
    """,
    "tests": [
        {"name": "monthly_registration_thorax_cbct_vrt"},
        {"name": "monthly_registration_thorax_cbct_lng"},
        {"name": "monthly_registration_thorax_cbct_lat"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_REGISTRATION_KV_PLANAR_PAIR = {
    "long name": "Monthly Registration using Varian Cube Phantom - KV planar pair",
    "slug": "monthly-registration-kv-planar-pair",
    "description": """<font color="#0070c0">Plan: <b>9Registration.dcm</b></font>
    <br><b>SETUP:</b> As above.
      <br><b>ACQUISITION:</b> As above, adjust manually, DO NOT move couch. Write down suggested couch moves.
    """,
    "tests": [
        {"name": "monthly_registration_kv_planar_pair_vrt"},
        {"name": "monthly_registration_kv_planar_pair_lng"},
        {"name": "monthly_registration_kv_planar_pair_lat"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_REGISTRATION_MARKER_MATCH = {
    "long name": "Monthly Registration using Varian Cube Phantom - KV Marker Match",
    "slug": "monthly-registration-marker-match",
    "description": """<font color="#0070c0">Plan: <b>9Registration.dcm</b></font>
    <br><b>SETUP:</b> As above.
      <br><b>ACQUISITION:</b> As above, adjust manually, DO NOT move couch. Write down suggested couch moves.
    """,
    "tests": [
        {"name": "monthly_registration_kv_marker_match_vrt"},
        {"name": "monthly_registration_kv_marker_match_lng"},
        {"name": "monthly_registration_kv_marker_match_lat"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_REGISTRATION_PLANAR_90 = {
    "long name": "Monthly Registration using Varian Cube Phantom - MV Planar 90°",
    "slug": "monthly-registration-planar-90",
    "description": """<font color="#0070c0">Plan: <b>9Registration.dcm</b></font>
    <br><b>SETUP:</b> As above.
      <br><b>ACQUISITION:</b> As above, adjust manually, DO NOT move couch. Write down suggested couch moves.
    """,
    "tests": [
        {"name": "monthly_registration_mv_planar_90_vrt"},
        {"name": "monthly_registration_mv_planar_90_lng"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_REGISTRATION_PLANAR_0 = {
    "long name": "Monthly Registration using Varian Cube Phantom - MV Planar 0°",
    "slug": "monthly-registration-planar-0",
    "description": """<font color="#0070c0">Plan: <b>9Registration.dcm</b></font>
    <br><b>SETUP:</b> As above.
      <br><b>ACQUISITION:</b> As above, adjust manually, DO NOT move couch. Write down suggested couch moves.
    """,
    "tests": [
        {"name": "monthly_registration_mv_planar_0_lng"},
        {"name": "monthly_registration_mv_planar_0_lat"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_REGISTRATION_ALL = {
    "long name": "Monthly Registration using Varian Cube Phantom",
    "slug": "monthly-registration-cube",
    "description": r"""<font color="#0070c0">Plan: <b>9Registration.dcm</b></font>
    <br><b>SETUP:</b> Gantry 0°, Position indexed registration phantom at couch location H3 and move couch to VRT 10.0, LNG 82.0, LAT 1.0, ROT 0.0.
      <br><b>ACQUISITION:</b> Use <font color="red"><b>TREATMENT</b></font> mode, file directory: Shared drive\PHYSICS\MachineID\QA\Monthly QA.
      <br> Validate phantom setup using Thorax CBCT with 5 cm z-offset, 2D-2D KV- and MV-paired, and kV Marker Match protocols (DO NOT move couch).
      <br> Use 3D auto-registration for CBCT protocol and manual registrations for all KV and MV planar images. If auto-registration fails, use manual.
      <br> Write down Couch Coordinates AFTER Move for first test, then for the rest, write down SUGGESTED moves only.
    """,
    "tests": [],
    "test_lists": [
        {"name": MONTHLY_REGISTRATION_HEAD, "order": 0},
        {"name": MONTHLY_REGISTRATION_THORAX, "order": 1},
        {"name": MONTHLY_REGISTRATION_KV_PLANAR_PAIR, "order": 2},
        {"name": MONTHLY_REGISTRATION_MARKER_MATCH, "order": 3},
        {"name": MONTHLY_REGISTRATION_PLANAR_90, "order": 4},
        {"name": MONTHLY_REGISTRATION_PLANAR_0, "order": 5},
    ],
    "sublists": [],
    "cycle": [],
}

MONTHLY_REGISTRATION = {
    "long name": "Monthly Registration",
    "slug": "monthly-registration",
    "description": "Monthly Registration",
    "tests": [],
    "test_lists": [],
    "sublists": [
        {"name": MONTHLY_REGISTRATION_ALL},
    ],
    "cycle": [],
}
