MONTHLY_MV_IMAGE_UNIFORMITY = {
    "long name": "Monthly MV Image Uniformity",
    "slug": "monthly-mv-image-uniformity",
    "description": """<font color="#0070c0">Plan if not Oak: <b>7B_EPI.dcm</b>
    <br>Plan if Oak: <b>7B_EPI_HD.dcm</b></font>
    <br><b>SETUP/ACQUISITION/ANALYSIS:</b>  As per above. For analysis, use second image (less ghosting artifact present)
    """,
    "tests": [
        {"name": "monthly_MV_image_uniformity_x_flatness"},
        {"name": "monthly_MV_image_uniformity_x_symmetry"},
        {"name": "monthly_MV_image_uniformity_y_flatness"},
        {"name": "monthly_MV_image_uniformity_y_symmetry"},
        {"name": "monthly_MV_image_signal_roi_delta"},
        {"name": "monthly_MV_image_noise_roi_delta"},
        {"name": "monthly_MV_image_artefacts"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}
