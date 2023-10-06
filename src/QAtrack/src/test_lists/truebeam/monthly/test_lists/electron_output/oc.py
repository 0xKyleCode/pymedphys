MONTHLY_OC_6E = {
    "long name": "Monthly Output Constancy - 6E",
    "slug": "monthly-oc-6e",
    "description": "Monthly Output Constancy for 6E",
    "tests": [
        {"name": "monthly_OC_6E_1"},
        {"name": "monthly_OC_6E_2"},
        {"name": "monthly_OC_6E_3"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}

MONTHLY_OC_9E = {
    "long name": "Monthly Output Constancy - 9E",
    "slug": "monthly-oc-9e",
    "description": "Monthly Output Constancy for 9E",
    "tests": [
        {"name": "monthly_OC_9E_1"},
        {"name": "monthly_OC_9E_2"},
        {"name": "monthly_OC_9E_3"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}

MONTHLY_OC_12E = {
    "long name": "Monthly Output Constancy - 12E",
    "slug": "monthly-oc-12e",
    "description": "Monthly Output Constancy for 12E",
    "tests": [
        {"name": "monthly_OC_12E_1"},
        {"name": "monthly_OC_12E_2"},
        {"name": "monthly_OC_12E_3"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}

# For 16 E
MONTHLY_OC_16E = {
    "long name": "Monthly Output Constancy - 16E",
    "slug": "monthly-oc-16e",
    "description": "Monthly Output Constancy for 16E",
    "tests": [
        {"name": "monthly_OC_16E_1"},
        {"name": "monthly_OC_16E_2"},
        {"name": "monthly_OC_16E_3"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}

# For 20E
MONTHLY_OC_20E = {
    "long name": "Monthly Output Constancy - 20E",
    "slug": "monthly-oc-20e",
    "description": "Monthly Output Constancy for 20E",
    "tests": [
        {"name": "monthly_OC_20E_1"},
        {"name": "monthly_OC_20E_2"},
        {"name": "monthly_OC_20E_3"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}

# For Electron Doses
MONTHLY_OC_ELECTRON_DOSE = {
    "long name": "Monthly Output Constancy - Electron Dose",
    "slug": "monthly-oc-electron-dose",
    "description": r"""<font color="#0070c0">Plan: <b>6Electron_OP.dcm</b></font>
    <br><b>Probe/Electrometer:</b> med range, nC, -300V. 1mm cap on probe.
    <br><b>SETUP:</b>  Gantry 0°, Collimator 0°, Couch 0°, SSD100 in solid water, <b>Depth (6E, <font color="red">1.5cm</font>; 9-20E, <font color="red">2.5cm</font>)</b>, Backscatter 5cm, Applicator A10 w/std insert
      <br><b>ACQUISITION:</b> Use <font color="red"><b>MACHINE QA</b></font> mode, file directory: Shared drive\PHYSICS\MachineID\QA\Monthly QA.
    """,
    "tests": [
        {"name": "monthly_OC_6E_DOSE"},
        {"name": "monthly_OC_9E_DOSE"},
        {"name": "monthly_OC_12E_DOSE"},
        {"name": "monthly_OC_16E_DOSE"},
        {"name": "monthly_OC_20E_DOSE"},
        {"name": "viarbutus_tb2_electron_6e_fc"},
        {"name": "vifir_tb1_electron_6e_fc"},
        {"name": "vibirch_tb3_electron_6e_fc"},
        {"name": "viarbutus_tb2_electron_9e_fc"},
        {"name": "vifir_tb1_electron_9e_fc"},
        {"name": "vibirch_tb3_electron_9e_fc"},
        {"name": "viarbutus_tb2_electron_12e_fc"},
        {"name": "vifir_tb1_electron_12e_fc"},
        {"name": "vibirch_tb3_electron_12e_fc"},
        {"name": "viarbutus_tb2_electron_16e_fc"},
        {"name": "vifir_tb1_electron_16e_fc"},
        {"name": "vibirch_tb3_electron_16e_fc"},
        {"name": "viarbutus_tb2_electron_20e_fc"},
        {"name": "vifir_tb1_electron_20e_fc"},
        {"name": "vibirch_tb3_electron_20e_fc"},
    ],
    "test_lists": [
        {"name": MONTHLY_OC_6E, "order": 0},
        {"name": MONTHLY_OC_9E, "order": 2},
        {"name": MONTHLY_OC_12E, "order": 4},
        {"name": MONTHLY_OC_16E, "order": 6},
        {"name": MONTHLY_OC_20E, "order": 8},
    ],
    "sublists": [],
    "cycle": [],
}
