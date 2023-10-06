MONTHLY_VMAT = {
    "long name": "6X - VMAT Factor",
    "slug": "6x-vmat-factor-cw",
    "description": """<font color="#0070c0">Plan if not Oak: <b>3VMAT_H&N.dcm</b>
    <br>Plan if Oak: <b>3VMAT_HD.dcm</b></font>
    <br><b>Electrometer:</b> med range, nC, -300V
    <br><b>SETUP:</b> as above
      <br><b>ACQUISITION:</b> as above
      <br><b>NOTE:</b> Note: field VMAT_cw is a mirror of VMAT_ccw for Rdg2
    """,
    "tests": [
        {"name": "monthly_VMAT_factor_ccw"},
        {"name": "monthly_VMAT_factor_cw"},
        {"name": "monthly_VMAT_6X_factor"},
    ],
    "test_lists": [],
    "sublists": [],
    "cycle": [],
}
