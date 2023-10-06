MONTHLY_PICKET_FENCE = {
    "long name": "Monthly Picket Fence",
    "slug": "monthly-picket-fence",
    "description": """<font color="#0070c0">Plan if not Oak: <b>7B_EPI.dcm</b>
    <br>Plan if Oak: <b>7B_EPI_HD.dcm</b></font>
    <br><b>SETUP/ACQUISITION/ANALYSIS*:</b>   As per above
      <br><font size=2>* Current tolerance values are tentative; If picket fence fails, append details from Portal QA to report</font>
    """,
    "tests": [
        {"name": "monthly_picket_fence_distance"},
        {"name": "monthly_picket_fence_delta_peak_size"},
        {"name": "monthly_picket_fence_individual_peak_size"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}
