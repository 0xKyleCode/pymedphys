MONTHLY_PLANAR_KV_ACCURACY_DOSE = {
    "long name": "Monthly Planar KV - kVp Accuracy/Dose",
    "slug": "monthly-planar-kv-accuracy-dose",
    "description": """<font color="#0070c0">Plan: <b>11KVPlanar.dcm</b></font>
        <br><b>SETUP:</b>  As per above except position <b>PTW Diavolt Multimeter</b> on KVD cover aligned ~ isocentre;
        <br> <b>ACQUISITION:</b> <b>Physics QA Template (75 kVp or 125 kVp)</b>; KV blades X1=X2=Y1=Y2=10.0cm; Diavolt settings: Application Rad/Flu, W 3.0 Al

    """,
    "tests": [
        {"name": "monthly_kvp_dose_75_reading"},
        {"name": "monthly_kvp_dose_75_dose"},
        {"name": "monthly_kvp_dose_125_reading"},
        {"name": "monthly_kvp_dose_125_dose"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}
