MONTHLY_PLANAR_KV_FIELD_SIZE = {
    "long name": "Monthly Planar KV - Field Size Accuracy",
    "slug": "monthly-planar-kv-field-size",
    "description": """<font color="#0070c0">Plan: <b>11KVPlanar.dcm</b></font>
        <br><b>SETUP:</b> As per above.
        <br> <b>ACQUISITION:</b> as per above
        <br> Select Beam Preview button on console, turn <b>Blade Tracking OFF</b>, adjust blade positions to: x1=x2=y1=y2=10.0cm. Acquire KV planar image
        <br> <b>ANALYSIS:</b> Measure distances from digital field edge to radiation field edge using console display tools. Checks blade and detector positioning accuracy.
    """,
    "tests": [
        {"name": "monthly_field_size_accuracy_x1"},
        {"name": "monthly_field_size_accuracy_x2"},
        {"name": "monthly_field_size_accuracy_y1"},
        {"name": "monthly_field_size_accuracy_y2"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}
