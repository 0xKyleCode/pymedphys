MONTHLY_CBCT_IMAGE_QUALITY = {
    "long name": "Monthly CBCT - kV CBCT Image Quality",
    "slug": "monthly-cbct-image-quality",
    "description": r"""<font color="#0070c0">Plan: <b>12CBCT.dcm</b></font>
        <br><b>SETUP:</b> Align front dots on CATPHAN504 phantom with laser isocentre then move couch LNG 7cm to align lasers with 3rd dot on top of phantom
        <br> <b>ACQUISITION:</b> Use <b><font color="red">TREATMENT mode</font></b>, file directory: Shared drive\PHYSICS\MachineID\QA\Monthly QA.
        <br> Acquire CBCT image set using the specified Head protocol.
        <br> <b>ANALYSIS:</b> Use PipsPro software or in-house MATLAB code for image quality analysis
    """,
    "tests": [
        {"name": "monthly_cbct_8_1_IQ"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}
