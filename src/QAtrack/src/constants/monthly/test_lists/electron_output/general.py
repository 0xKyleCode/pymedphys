MONTHLY_CTP_ELECTRON = {
    "long name": "CTP Electron",
    "slug": "ctp-electron",
    "description": "CTP for Monthly Electron QA",
    "tests": [
        {"name": "p_corr_electron"},
        {"name": "t_probe_electron"},
        {"name": "ctp_electron"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_ND_ELECTRON = {
    "long name": "ND Electron",
    "slug": "nd-electron",
    "description": "ND for Monthly Electron QA",
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
        {"name": "nd_electron"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

MONTHLY_GENERAL = [MONTHLY_CTP_ELECTRON, MONTHLY_ND_ELECTRON]
