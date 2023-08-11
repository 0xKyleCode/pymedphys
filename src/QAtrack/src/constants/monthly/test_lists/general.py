MONTHLY_CTP_PHOTON = {
    "long name": "CTP Photon",
    "slug": "ctp-photon",
    "description": "CTP for Monthly Photon QA",
    "tests": [
        {"name": "p_corr_photon", "order": 0},
        {"name": "t_probe_photon", "order": 1},
        {"name": "ctp_photon", "order": 2},
    ],
    "test_lists": [],
}

MONTHLY_ND_PHOTON = {
    "long name": "ND Photon",
    "slug": "nd-photon",
    "description": "ND for Monthly Photon QA",
    "tests": [
        {"name": "ptw_probe_id", "order": 0},
        {"name": "ptw_6_nd", "order": 0},
        {"name": "ptw_5_nd", "order": 1},
        {"name": "ptw_4_nd", "order": 2},
        {"name": "ptw_3_nd", "order": 3},
        {"name": "ptw_2_nd", "order": 4},
        {"name": "ptw_7_nd", "order": 5},
        {"name": "nd_photon", "order": 6},
    ],
    "test_lists": [],
}

MONTHLY_GENERAL = [MONTHLY_CTP_PHOTON, MONTHLY_ND_PHOTON]
