MONTHLY_PLANAR_KV_IMAGE_QUALITY = {
    "long name": "Monthly Planar KV - Image Quality - PipsPro KV",
    "slug": "monthly-planar-kv-image-quality",
    "description": """<font color="#0070c0">Plan: <b>11KVPlanar.dcm</b></font>
        <br><b>SETUP:</b>  As per above except position <b>PipsPro KV phantom</b> on KVD cover aligned ~ isocentre
        <br> <b>ACQUISITION:</b> Physics QA Template (60 kVp or 60 kVp Sm FS, Ti filter), KV blades X1=X2=Y1=Y2=10.0cm
    """,
    "tests": [
        {"name": "monthly_image_quality_large_f30"},
        {"name": "monthly_image_quality_large_f10"},
        {"name": "monthly_image_quality_large_CNR"},
        {"name": "monthly_image_quality_small_f30"},
        {"name": "monthly_image_quality_small_f10"},
        {"name": "monthly_image_quality_small_CNR"},
    ],
    "sublists": [],
    "test_lists": [],
    "cycle": [],
}
