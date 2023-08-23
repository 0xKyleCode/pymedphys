MONTHLY_CTP_PHOTON = {
    "long name": "CTP Photon",
    "slug": "ctp-photon",
    "description": "CTP for Monthly Photon QA",
    "tests": [
        {"name": "p_corr_photon"},
        {"name": "t_probe_photon"},
        {"name": "ctp_photon"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_ND_PHOTON = {
    "long name": "ND Photon",
    "slug": "nd-photon",
    "description": "ND for Monthly Photon QA",
    "tests": [
        {"name": "ptw_probe_id"},
        {"name": "ptw_6_nd"},
        {"name": "ptw_5_nd"},
        {"name": "ptw_4_nd"},
        {"name": "ptw_3_nd"},
        {"name": "ptw_2_nd"},
        {"name": "ptw_7_nd"},
        {"name": "electrometer_id"},
        {"name": "unidose_s1_p_elec"},
        {"name": "unidose_e2_p_elec"},
        {"name": "unidose_e3_p_elec"},
        {"name": "unidose_e4_p_elec"},
        {"name": "unidose_e5_p_elec"},
        {"name": "nd_photon"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_GENERAL = [MONTHLY_CTP_PHOTON, MONTHLY_ND_PHOTON]
