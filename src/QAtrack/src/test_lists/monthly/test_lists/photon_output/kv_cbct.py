QUARTERLY_HEAD_KV_CBCT = {
    "long name": "Quarterly Head kV CBCT",
    "slug": "quarterly-head-kv-cbct",
    "description": "Quarterly Head kV CBCT",
    "tests": [
        {"name": "monthly_dose_index_HEAD"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

QUARTERLY_SPOTLIGHT_KV_CBCT = {
    "long name": "Quarterly Spotlight kV CBCT",
    "slug": "quarterly-spotlight-kv-cbct",
    "description": "Quarterly Spotlight kV CBCT",
    "tests": [
        {"name": "monthly_dose_index_SPOTLIGHT"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

QUARTERLY_THORAX_KV_CBCT = {
    "long name": "Quarterly Thorax kV CBCT",
    "slug": "quarterly-thorax-kv-cbct",
    "description": "Quarterly Thorax kV CBCT",
    "tests": [
        {"name": "monthly_dose_index_THORAX"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

QUARTERLY_PELVIS_KV_CBCT = {
    "long name": "Quarterly Pelvis kV CBCT",
    "slug": "quarterly-pelvis-kv-cbct",
    "description": "Quarterly Pelvis kV CBCT",
    "tests": [
        {"name": "monthly_dose_index_PELVIS"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}

QUARTERLY_KV_CBCT = {
    "long name": "Quarterly kV CBCT",
    "slug": "quarterly-kv-cbct",
    "description": r"""<font color="#0070c0">Plan: <b>12CBCT.dcm</b></font>
    <br><b>SETUP:</b>  As per above except Farmer chamber axis <font color="red"><b>parallel</b></font> to couch LNG;  100 cm SAD, depth <font color="red"><b>1 cm</b></font>, backscatter 5 cm, Unidos electrometer (-300V, med); CTP correction; Nd-ratio correction; rotate gantry to 180° CW.
      <br><b>ACQUISITION:</b> Use <font color="red"><b>MACHINE QA or TREATMENT</b></font> mode, Acquire CBCT image sets for specified protocols using SPECIFIED mAs. Shared drive\PHYSICS\MachineID\QA\Monthly QA.
    <br><b>NOTE:</b> <font size=2 color="red">* For the Head protocol, position Gantry at GA180° CW prior to image acquisition.</font>
    """,
    "tests": [
        {"name": "monthly_dose_index_HEAD_corr"},
        {"name": "monthly_dose_index_SPOTLIGHT_corr"},
        {"name": "monthly_dose_index_THORAX_corr"},
        {"name": "monthly_dose_index_PELVIS_corr"},
    ],
    "test_lists": [
        {"name": QUARTERLY_HEAD_KV_CBCT, "order": 0},
        {"name": QUARTERLY_SPOTLIGHT_KV_CBCT, "order": 2},
        {"name": QUARTERLY_THORAX_KV_CBCT, "order": 4},
        {"name": QUARTERLY_PELVIS_KV_CBCT, "order": 6},
    ],
    "sublists": [],
    "cycle": [],
}
