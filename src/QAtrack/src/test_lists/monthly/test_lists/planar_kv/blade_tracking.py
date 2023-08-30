MONTHLY_PLANAR_KV_BLADE_TRACKING = {
    "long name": "Monthly Planar KV - Blade Tracking/Flood Field Artefacts",
    "slug": "monthly-planar-kv-blade-tracking",
    "description": r"""<font color="#0070c0">Plan: <b>11KVPlanar.dcm</b></font>
        <br><b>SETUP:</b> Gantry 90°, Couch LNG 25cm, KVD VRT=LAT=LNG=0.0cm
        <br> <b>ACQUISITION:</b> Use <b><font color="red">TREATMENT mode</font></b>, file directory: Shared drive\PHYSICS\MachineID\QA\Monthly QA.
        <br> Select <b>Physics QA Template (60 kVp - large focal spot, no filter) , with Blade Tracking ON</b>
        <br> <b>ANALYSIS:</b> Record blade settings, evaluate radiation coverage of detector array using console display tools, check for any artifacts
        <br> <b>NOTE:</b> Note: This flood field image should be used in PipsPro analysis. Result Status: Pass or Fail.
    """,
    "tests": [
        {"name": "monthly_planar_blade_tracking_x_1"},
        {"name": "monthly_planar_blade_tracking_x_2"},
        {"name": "monthly_planar_blade_tracking_y_1"},
        {"name": "monthly_planar_blade_tracking_y_2"},
        {"name": "monthly_planar_blade_tracking_coverage"},
        {"name": "monthly_planar_blade_tracking_artefacts"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}
