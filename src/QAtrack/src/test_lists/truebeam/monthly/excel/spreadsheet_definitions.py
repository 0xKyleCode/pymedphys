delta_symbol = "\u0394"


QA_OUTPUT = {
    "name": "Output Constancy (100MU) Reading",
    "data": [
        ("monthly_OC_6X_10x10_1", "6x Rdg 1 (nC)", "E47"),
        ("monthly_OC_6X_10x10_2", "6x Rdg 2 (nC)", "F47"),
        ("monthly_OC_6X_10x10_3", "6x Rdg 3 (nC)", "G47"),
        ("monthly_OC_10X_10x10_1", "10x Rdg 1 (nC)", "E48"),
        ("monthly_OC_10X_10x10_2", "10x Rdg 2 (nC)", "F48"),
        ("monthly_OC_10X_10x10_3", "10x Rdg 3 (nC)", "G48"),
        ("monthly_OC_10Xfff_10x10_1", "10fff Rdg 1 (nC)", "E49"),
        ("monthly_OC_10Xfff_10x10_2", "10fff Rdg 2 (nC)", "F49"),
        ("monthly_OC_10Xfff_10x10_3", "10fff Rdg 3 (nC)", "G49"),
        ("monthly_OC_15X_10x10_1", "15x Rdg 1 (nC)", "E50"),
        ("monthly_OC_15X_10x10_2", "15x Rdg 2 (nC)", "F50"),
        ("monthly_OC_15X_10x10_3", "15x Rdg 3 (nC)", "G50"),
    ],
}
QA_OUTPUT_RESULTS = {
    "name": "Output Constancy (100MU) Dose",
    "data": [
        ("monthly_OC_6X_10x10_DOSE", "6x Dose (cGy)", "I47"),
        ("monthly_OC_10X_10x10_DOSE", "10x Dose (cGy)", "I48"),
        ("monthly_OC_10Xfff_10x10_DOSE", "10fff Dose (cGy)", "I49"),
        ("monthly_OC_15X_10x10_DOSE", "15x Dose (cGy)", "I50"),
    ],
}

QA_EDW = {
    "name": "EDW Factor (100MU) Reading",
    "data": [
        ("monthly_EDW60IN_6X", "6x Rdg 60IN (nC)", "E55"),
        ("monthly_EDW60OUT_6X", "6x Rdg 60OUT (nC)", "F55"),
        ("monthly_EDW60IN_10X", "10x Rdg 60IN (nC)", "E56"),
        ("monthly_EDW60OUT_10X", "10x Rdg 60OUT (nC)", "F56"),
        ("monthly_EDW60IN_15X", "15x Rdg 60IN (nC)", "E57"),
        ("monthly_EDW60OUT_15X", "15x Rdg 60OUT (nC)", "F57"),
    ],
}

QA_EDW_RESULTS = {
    "name": "EDW Factor (100MU) Result",
    "data": [
        ("monthly_EDWF_6X", "6x EDWf", "H55"),
        ("monthly_EDWF_10X", "10x EDWf", "H56"),
        ("monthly_EDWF_15X", "15x EDWf", "H57"),
    ],
}

QA_MLC = {
    "name": "dMLC Factor",
    "data": [
        ("monthly_dmlc_5mm_1", "6x - 5mm - Rdg1 (nC)", "F62"),
        ("monthly_dmlc_5mm_2", "6x - 5mm - Rdg2 (nC)", "G62"),
        ("monthly_dmlc_5mm_Int_1", "6x - 5mm interrupt - Rdg1 (nC)", "F63"),
        ("monthly_dmlc_5mm_Int_2", "6x - 5mm interrupt - Rdg2 (nC)", "G63"),
        ("monthly_dmlc_Hold_1", "6x - Beam Hold - Rdg1 (nC)", "F64"),
        ("monthly_dmlc_Hold_2", "6x - Beam Hold - Rdg2 (nC)", "G64"),
        ("monthly_dmlc_Prostate_6X_1", "6x - Prostate - Rdg1 (nC)", "F65"),
        ("monthly_dmlc_Prostate_6X_2", "6x - Prostate - Rdg2 (nC)", "G65"),
        ("monthly_dmlc_HN_1", "6x - H&N (Hi Mod) - Rdg1 (nC)", "F66"),
        ("monthly_dmlc_HN_2", "6x - H&N (Hi Mod) - Rdg2 (nC)", "G66"),
    ],
}

QA_MLC_RESULTS = {
    "name": "dMLC Factor Result",
    "data": [
        ("monthly_dmlc_5mm_ratio", "6x - 5mm Ratio", "I62"),
        ("monthly_dmlc_5mm_Int_ratio", "6x - 5mm interrupt Ratio", "I63"),
        ("monthly_dmlc_Hold_ratio", "6x - Beam Hold Ratio", "I64"),
        ("monthly_dmlc_Prostate_6X_ratio", "6x - Prostate Ratio", "I65"),
        ("monthly_dmlc_HN_ratio", "6x - H&N (Hi Mod) Ratio", "I66"),
    ],
}

QA_VMAT = {
    "name": "VMAT Factor",
    "data": [
        ("monthly_VMAT_factor_ccw", "6x Rdg1 - CCW (nC)", "F72"),
        ("monthly_VMAT_factor_cw", "6x Rdg2 - CW (nC)", "G72"),
    ],
}

QA_VMAT_RESULT = {
    "name": "VMAT Factor Ratio",
    "data": [("monthly_VMAT_6X_factor", "6x Ratio", "I72")],
}

QA_dMLC_SEQUENCE = {
    "name": "dMLC Invalid Sequence",
    "data": [("monthly_dmlc_error", "Result", "E77")],
}

QA_TMR_PHOTON = {
    "name": "TMR (100MU)",
    "data": [
        ("monthly_TMR_6X_1", "6x - Rdg1 @ dmax (nC)", "F85"),
        ("monthly_TMR_6X_2", "6x - Rdg2 @ dmax (nC)", "G85"),
        ("monthly_TMR_10X_1", "10x - Rdg1 @ dmax (nC)", "F86"),
        ("monthly_TMR_10X_2", "10x - Rdg2 @ dmax (nC)", "G86"),
        ("monthly_TMR_10fff_1", "10fff - Rdg1 @ dmax (nC)", "F87"),
        ("monthly_TMR_10fff_2", "10fff - Rdg2 @ dmax (nC)", "G87"),
        ("monthly_TMR_15X_1", "15x - Rdg1 @ dmax (nC)", "F88"),
        ("monthly_TMR_15X_2", "15x - Rdg2 @ dmax (nC)", "G88"),
    ],
}

QA_TMR_PHOTON_RESULT = {
    "name": "TMR (100MU) Result",
    "data": [
        ("monthly_TMR_6X", "6x - TMR(10)", "I85"),
        ("monthly_TMR_10X", "10x - TMR(10)", "I86"),
        ("monthly_TMR_10fff", "10fff - TMR(10)", "I87"),
        ("monthly_TMR_15X", "15x - TMR(10)", "I88"),
    ],
}

QA_CBCT = {
    "name": "KV CBCT Dose Index",
    "data": [
        (
            "monthly_dose_index_HEAD",
            "Head - Full Fan - Half Trajectory - Rdg (nC)",
            "G98",
        ),
        (
            "monthly_dose_index_SPOTLIGHT",
            "Spotlight - Full Fan - Half Trajectory - Rdg (nC)",
            "G99",
        ),
        (
            "monthly_dose_index_THORAX",
            "Thorax - Half Fan - Full Trajectory - Rdg (nC)",
            "G100",
        ),
        (
            "monthly_dose_index_PELVIS",
            "Pelvis Obese - Half Fan - Full Trajectory - Rdg (nC)",
            "G101",
        ),
    ],
}
QA_CBCT_RESULT = {
    "name": "KV CBCT Dose Index Result",
    "data": [
        (
            "monthly_dose_index_HEAD_corr",
            "Head - Full Fan - Half Trajectory - Rdg Corrected (nC)",
            "H98",
        ),
        (
            "monthly_dose_index_SPOTLIGHT_corr",
            "Spotlight - Full Fan - Half Trajectory - Rdg Corrected (nC)",
            "H99",
        ),
        (
            "monthly_dose_index_THORAX_corr",
            "Thorax - Half Fan - Full Trajectory - Rdg Corrected (nC)",
            "H100",
        ),
        (
            "monthly_dose_index_PELVIS_corr",
            "Pelvis Obese - Half Fan - Full Trajectory - Rdg Corrected (nC)",
            "H101",
        ),
    ],
}


QA_ELECTRON = {
    "name": "Electron Output Constancy (100MU) Reading",
    "data": [
        ("monthly_OC_6E_1", "6E Rdg1 (nC)", "E116"),
        ("monthly_OC_6E_2", "6E Rdg2 (nC)", "F116"),
        ("monthly_OC_6E_3", "6E Rdg3 (nC)", "G116"),
        ("monthly_OC_9E_1", "9E Rdg1 (nC)", "E117"),
        ("monthly_OC_9E_2", "9E Rdg2 (nC)", "F117"),
        ("monthly_OC_9E_3", "9E Rdg3 (nC)", "G117"),
        ("monthly_OC_12E_1", "12E Rdg1 (nC)", "E118"),
        ("monthly_OC_12E_2", "12E Rdg2 (nC)", "F118"),
        ("monthly_OC_12E_3", "12E Rdg3 (nC)", "G118"),
        ("monthly_OC_16E_1", "16E Rdg1 (nC)", "E119"),
        ("monthly_OC_16E_2", "16E Rdg2 (nC)", "F119"),
        ("monthly_OC_16E_3", "16E Rdg3 (nC)", "G119"),
        ("monthly_OC_20E_1", "20E Rdg1 (nC)", "E120"),
        ("monthly_OC_20E_2", "20E Rdg2 (nC)", "F120"),
        ("monthly_OC_20E_3", "20E Rdg3 (nC)", "G120"),
    ],
}

QA_ELECTRON_DOSE = {
    "name": "Electron Output Constancy (100MU) Dose",
    "data": [
        ("monthly_OC_6E_DOSE", "6E Dose (cGy)", "I116"),
        ("monthly_OC_9E_DOSE", "9E Dose (cGy)", "I117"),
        ("monthly_OC_12E_DOSE", "12E Dose (cGy)", "I118"),
        ("monthly_OC_16E_DOSE", "16E Dose (cGy)", "I119"),
        ("monthly_OC_20E_DOSE", "20E Dose (cGy)", "I120"),
    ],
}

QA_LIGHT_RADIATION_COINCIDENCE_JAWS = {
    "name": "Light-Radiation Coincidence, Jaws-defined",
    "data": [
        (
            "monthly_light_coincidence_jaw_x1",
            f"Light-Dig - {delta_symbol}X1 (mm)",
            "E131",
        ),
        (
            "monthly_light_coincidence_jaw_x2",
            f"Light-Dig - {delta_symbol}X2 (mm)",
            "F131",
        ),
        (
            "monthly_light_coincidence_jaw_y1",
            f"Light-Dig - {delta_symbol}Y1 (mm)",
            "G131",
        ),
        (
            "monthly_light_coincidence_jaw_y2",
            f"Light-Dig - {delta_symbol}Y2 (mm)",
            "H131",
        ),
        (
            "monthly_6x_rad_coincidence_jaw_x1",
            f"6x Rad-Dig - {delta_symbol}X1 (mm)",
            "E132",
        ),
        (
            "monthly_6x_rad_coincidence_jaw_x2",
            f"6x Rad-Dig - {delta_symbol}X2 (mm)",
            "F132",
        ),
        (
            "monthly_6x_rad_coincidence_jaw_y1",
            f"6x Rad-Dig - {delta_symbol}Y1 (mm)",
            "G132",
        ),
        (
            "monthly_6x_rad_coincidence_jaw_y2",
            f"6x Rad-Dig - {delta_symbol}Y2 (mm)",
            "H132",
        ),
        (
            "monthly_10x_rad_coincidence_jaw_x1",
            f"10x Rad-Dig - {delta_symbol}X1 (mm)",
            "E133",
        ),
        (
            "monthly_10x_rad_coincidence_jaw_x2",
            f"10x Rad-Dig - {delta_symbol}X2 (mm)",
            "F133",
        ),
        (
            "monthly_10x_rad_coincidence_jaw_y1",
            f"10x Rad-Dig - {delta_symbol}Y1 (mm)",
            "G133",
        ),
        (
            "monthly_10x_rad_coincidence_jaw_y2",
            f"10x Rad-Dig - {delta_symbol}Y2 (mm)",
            "H133",
        ),
        (
            "monthly_15x_rad_coincidence_jaw_x1",
            f"15x Rad-Dig - {delta_symbol}X1 (mm)",
            "E134",
        ),
        (
            "monthly_15x_rad_coincidence_jaw_x2",
            f"15x Rad-Dig - {delta_symbol}X2 (mm)",
            "F134",
        ),
        (
            "monthly_15x_rad_coincidence_jaw_y1",
            f"15x Rad-Dig - {delta_symbol}Y1 (mm)",
            "G134",
        ),
        (
            "monthly_15x_rad_coincidence_jaw_y2",
            f"15x Rad-Dig - {delta_symbol}Y2 (mm)",
            "H134",
        ),
    ],
}

QA_LIGHT_RADIATION_COINCIDENCE_JAWS_RESULT = {
    "name": "Light-Radiation Coincidence, Jaws-defined, Rad-Light",
    "data": [
        ("monthly_6x_rad_coincidence_jaw_x1_result", f"{delta_symbol}X1 (mm)", "E135"),
        ("monthly_6x_rad_coincidence_jaw_x2_result", f"{delta_symbol}X2 (mm)", "F135"),
        ("monthly_6x_rad_coincidence_jaw_y1_result", f"{delta_symbol}Y1 (mm)", "G135"),
        ("monthly_6x_rad_coincidence_jaw_y2_result", f"{delta_symbol}Y2 (mm)", "H135"),
        ("monthly_10x_rad_coincidence_jaw_x1_result", f"{delta_symbol}X1 (mm)", "E136"),
        ("monthly_10x_rad_coincidence_jaw_x2_result", f"{delta_symbol}X2 (mm)", "F136"),
        ("monthly_10x_rad_coincidence_jaw_y1_result", f"{delta_symbol}Y1 (mm)", "G136"),
        ("monthly_10x_rad_coincidence_jaw_y2_result", f"{delta_symbol}Y2 (mm)", "H136"),
        ("monthly_15x_rad_coincidence_jaw_x1_result", f"{delta_symbol}X1 (mm)", "E137"),
        ("monthly_15x_rad_coincidence_jaw_x2_result", f"{delta_symbol}X2 (mm)", "F137"),
        ("monthly_15x_rad_coincidence_jaw_y1_result", f"{delta_symbol}Y1 (mm)", "G137"),
        ("monthly_15x_rad_coincidence_jaw_y2_result", f"{delta_symbol}Y2 (mm)", "H137"),
    ],
}

QA_LIGHT_RADIATION_COINCIDENCE_MLC = {
    "name": "Light-Radiation Coincidence, MLC-defined",
    "data": [
        (
            "monthly_light_coincidence_mlc_x1",
            f"Light-Dig - {delta_symbol}X1 (mm)",
            "E145",
        ),
        (
            "monthly_light_coincidence_mlc_x2",
            f"Light-Dig - {delta_symbol}X (mm)",
            "F145",
        ),
        (
            "monthly_light_coincidence_mlc_y1",
            f"Light-Dig - {delta_symbol}Y1 (mm)",
            "G145",
        ),
        (
            "monthly_light_coincidence_mlc_y2",
            f"Light-Dig - {delta_symbol}Y2 (mm)",
            "H145",
        ),
        (
            "monthly_6x_rad_coincidence_mlc_x1",
            f"6x Rad-Dig - {delta_symbol}X1 (mm)",
            "E146",
        ),
        (
            "monthly_6x_rad_coincidence_mlc_x2",
            f"6x Rad-Dig - {delta_symbol}X2 (mm)",
            "F146",
        ),
        (
            "monthly_6x_rad_coincidence_mlc_y1",
            f"6x Rad-Dig - {delta_symbol}Y1 (mm)",
            "G146",
        ),
        (
            "monthly_6x_rad_coincidence_mlc_y2",
            f"6x Rad-Dig - {delta_symbol}Y2 (mm)",
            "H146",
        ),
    ],
}

QA_LIGHT_RADIATION_COINCIDENCE_MLC_RESULT = {
    "name": "Light-Radiation Coincidence, MLC-defined, Rad-Light",
    "data": [
        ("monthly_6x_rad_coincidence_mlc_x1_result", f"{delta_symbol}X1 (mm)", "E147"),
        ("monthly_6x_rad_coincidence_mlc_x2_result", f"{delta_symbol}X2 (mm)", "F147"),
        ("monthly_6x_rad_coincidence_mlc_y1_result", f"{delta_symbol}Y1 (mm)", "G147"),
        ("monthly_6x_rad_coincidence_mlc_y2_result", f"{delta_symbol}X2 (mm)", "H147"),
    ],
}

QA_RADIATION_FIELD_EDGE_ALIGNMENT = {
    "name": "Radiation Field Edge Alignment @CAX",
    "data": [
        ("monthly_light_field_edge_alignment_x1", "6X - X1 (mm)", "D161"),
        ("monthly_light_field_edge_alignment_x2", "6X - X2 (mm)", "E161"),
        ("monthly_light_field_edge_alignment_y1", "6X - Y1 (mm)", "F161"),
        ("monthly_light_field_edge_alignment_y2", "6X - Y2 (mm)", "G161"),
        ("monthly_light_field_edge_alignment_x1_y2_jxn", "6X - X1/Y2 Jxn (%)", "H161"),
        ("monthly_light_field_edge_alignment_x2_y1_jxn", "6X - X2/Y1 Jxn (%)", "I161"),
    ],
}

QA_MV_IMAGE_UNIFORMITY = {
    "name": "MV Image Uniformity",
    "data": [
        ("monthly_MV_image_uniformity_x_flatness", "X-Flatness (%)", "D170"),
        ("monthly_MV_image_uniformity_y_flatness", "Y-Flatness (%)", "F170"),
        ("monthly_MV_image_uniformity_x_symmetry", "X-Symmetry (%)", "E170"),
        ("monthly_MV_image_uniformity_y_symmetry", "Y-Symmetry (%)", "G170"),
        (
            "monthly_MV_image_signal_roi_delta",
            f"Signal - ROI {delta_symbol}max (%)",
            "H170",
        ),
        (
            "monthly_MV_image_noise_roi_delta",
            f"Noise - ROI {delta_symbol}max (%)",
            "I170",
        ),
        ("monthly_MV_image_artefacts", "Artefacts", "J170"),
    ],
}

QA_PICKET_FENCE = {
    "name": "Picket Fence",
    "data": [
        ("monthly_picket_fence_distance", "Distance (cm)", "C186"),
        (
            "monthly_picket_fence_delta_peak_size",
            f"{delta_symbol}Peak Size (%)",
            "G186",
        ),
        ("monthly_picket_fence_individual_peak_size", "Individual Peak", "J186"),
    ],
}

QA_EPI = {
    "name": "EPI",
    "data": [
        ("monthly_sliding_window", "5mm Sliding Window", "D198"),
        ("monthly_friction_max_leaf_speed", "Friction @ Maximum Leaf Speed", "D206"),
        ("monthly_pips_pro_mv_f30", "PipsPro MV - f30 (lp/mm)", "D214"),
        ("monthly_pips_pro_mv_f10", "PipsPro MV - f10 (lp/mm)", "F214"),
        ("monthly_pips_pro_mv_CNR", "PipsPro MV - CNR", "H214"),
    ],
}

QA_VMAT_MECHANICAL = {
    "name": "VMAT Mechanical",
    "data": [
        (
            "monthly_vmat_mechanical_picket_fence_grid_offset_x_0",
            "GA: 0 - Grid Offset X (mm)",
            "E223",
        ),
        (
            "monthly_vmat_mechanical_picket_fence_grid_offset_x_90",
            "GA: 90 - Grid Offset X (mm)",
            "F223",
        ),
        (
            "monthly_vmat_mechanical_picket_fence_grid_offset_x_180",
            "GA: 180 - Grid Offset X (mm)",
            "H223",
        ),
        (
            "monthly_vmat_mechanical_picket_fence_grid_offset_x_270",
            "GA: 270 - Grid Offset X (mm)",
            "G223",
        ),
        (
            "monthly_vmat_mechanical_picket_fence_grid_offset_x_vmat",
            "VMAT - Grid Offset X (mm)",
            "I223",
        ),
        (
            "monthly_vmat_mechanical_picket_fence_grid_offset_y_0",
            "GA: 0 - Grid Offset Y (mm)",
            "E224",
        ),
        (
            "monthly_vmat_mechanical_picket_fence_grid_offset_y_90",
            "GA: 90 - Grid Offset Y (mm)",
            "F224",
        ),
        (
            "monthly_vmat_mechanical_picket_fence_grid_offset_y_180",
            "GA: 180 - Grid Offset Y (mm)",
            "H224",
        ),
        (
            "monthly_vmat_mechanical_picket_fence_grid_offset_y_270",
            "GA: 270 - Grid Offset Y (mm)",
            "G224",
        ),
        (
            "monthly_vmat_mechanical_picket_fence_grid_offset_y_vmat",
            "VMAT - Grid Offset Y (mm)",
            "I224",
        ),
        (
            "monthly_vmat_mechanical_picket_fence_grid_offset_distance_0",
            "GA: 0 - Junction Distance (mm)",
            "E225",
        ),
        (
            "monthly_vmat_mechanical_picket_fence_grid_offset_distance_90",
            "GA: 90 - Junction Distance (mm)",
            "F225",
        ),
        (
            "monthly_vmat_mechanical_picket_fence_grid_offset_distance_180",
            "GA: 180 - Junction Distance (mm)",
            "H225",
        ),
        (
            "monthly_vmat_mechanical_picket_fence_grid_offset_distance_270",
            "GA: 270 - Junction Distance (mm)",
            "G225",
        ),
        (
            "monthly_vmat_mechanical_picket_fence_grid_offset_distance_vmat",
            "VMAT - Junction Distance (mm)",
            "I225",
        ),
        (
            "monthly_vmat_mechanical_picket_fence_grid_offset_peak_0",
            "GA: 0 - Junction Peaks",
            "E226",
        ),
        (
            "monthly_vmat_mechanical_picket_fence_grid_offset_peak_90",
            "GA: 90 - Junction Peaks",
            "F226",
        ),
        (
            "monthly_vmat_mechanical_picket_fence_grid_offset_peak_180",
            "GA: 180 - Junction Peaks",
            "H226",
        ),
        (
            "monthly_vmat_mechanical_picket_fence_grid_offset_peak_270",
            "GA: 270 - Junction Peaks",
            "G226",
        ),
        (
            "monthly_vmat_mechanical_picket_fence_grid_offset_peak_vmat",
            "VMAT - Junction Peaks",
            "I226",
        ),
        ("monthly_vmat_mechanical_6x_dr_ga_speed", "VMAT 6X DR/GA Speed", "E230"),
        ("monthly_vmat_mechanical_6x_dr_mlc_speed", "VMAT 6X DR/MLC Speed", "E231"),
        ("monthly_vmat_mechanical_10x_dr_ga_speed", "VMAT 10Xfff DR/GA Speed", "E232"),
        (
            "monthly_vmat_mechanical_10xfff_open_flatness_x",
            "10XFFF Open Field Flatness - X (%)",
            "E235",
        ),
        (
            "monthly_vmat_mechanical_10xfff_open_flatness_y",
            "10XFFF Open Field Flatness - Y (%)",
            "F235",
        ),
    ],
}

QA_REGISTRATION = {
    "name": "Registration using Varian Cube Phantom",
    "data": [
        ("monthly_registration_head_cbct_vrt", "Head CBCT - VRT (cm)", "F251"),
        ("monthly_registration_head_cbct_lng", "Head CBCT - LNG (cm)", "H251"),
        ("monthly_registration_head_cbct_lat", "Head CBCT - LAT (cm)", "J251"),
        ("monthly_registration_thorax_cbct_vrt", "Thorax CBCT - VRT (cm)", "F255"),
        ("monthly_registration_thorax_cbct_lng", "Thorax CBCT - LNG (cm)", "G255"),
        ("monthly_registration_thorax_cbct_lat", "Thorax CBCT - LAT (cm)", "H255"),
        (
            "monthly_registration_kv_planar_pair_vrt",
            "KV Planar Pair - VRT (cm)",
            "F259",
        ),
        (
            "monthly_registration_kv_planar_pair_lng",
            "KV Planar Pair - LNG (cm)",
            "G259",
        ),
        (
            "monthly_registration_kv_planar_pair_lat",
            "KV Planar Pair - LAT (cm)",
            "H259",
        ),
        (
            "monthly_registration_kv_marker_match_vrt",
            "KV Marker Match - VRT (cm)",
            "F263",
        ),
        (
            "monthly_registration_kv_marker_match_lng",
            "KV Marker Match - LNG (cm)",
            "G263",
        ),
        (
            "monthly_registration_kv_marker_match_lat",
            "KV Marker Match - LAT (cm)",
            "H263",
        ),
        (
            "monthly_registration_mv_planar_90_vrt",
            "MV Planar GA 90° - VRT (cm)",
            "F267",
        ),
        (
            "monthly_registration_mv_planar_90_lng",
            "MV Planar GA 90° - LNG (cm)",
            "G267",
        ),
        ("monthly_registration_mv_planar_0_lng", "MV Planar GA 0° - LNG (cm)", "G271"),
        ("monthly_registration_mv_planar_0_lat", "MV Planar GA 0° - LNG (cm)", "H271"),
    ],
}


QA_MOTION_MANAGEMENT = {
    "name": "RPM System",
    "data": [
        (
            "monthly_motion_management_rpm_total_patient_motion",
            "Total Patient Motion (cm)",
            "E282",
        ),
        (
            "monthly_motion_management_rpm_gated_residual_motion",
            "Gated Residual Motion (cm)",
            "E283",
        ),
        (
            "monthly_motion_management_rpm_total_cycle_period",
            "Total Cycle Period (s)",
            "E284",
        ),
        (
            "monthly_motion_management_rpm_total_beam_on",
            "Total Beam On Time (min)",
            "E285",
        ),
        ("monthly_motion_management_rpm_time_delay", "Time Delay", "E287"),
        ("monthly_motion_management_rpm_beam_on", "Beam On", "E288"),
    ],
}

QA_PLANAR_BLADE_TRACKING = {
    "name": "Blade Tracking/Flood Field Artefacts",
    "data": [
        ("monthly_planar_blade_tracking_x_1", "X1 (cm)", "D305"),
        ("monthly_planar_blade_tracking_x_2", "X2 (cm)", "E305"),
        ("monthly_planar_blade_tracking_y_1", "Y1 (cm)", "F305"),
        ("monthly_planar_blade_tracking_y_2", "Y2 (cm)", "G305"),
        ("monthly_planar_blade_tracking_coverage", "Coverage", "H305"),
        ("monthly_planar_blade_tracking_artefacts", "Artefacts", "I305"),
    ],
}

QA_FIELD_SIZE_ACCURACY = {
    "name": "Field Size Accuracy",
    "data": [
        ("monthly_field_size_accuracy_x1", f"Rad-Dig - {delta_symbol}X1 (mm)", "E319"),
        ("monthly_field_size_accuracy_x2", f"Rad-Dig - {delta_symbol}X2 (mm)", "F319"),
        ("monthly_field_size_accuracy_y1", f"Rad-Dig - {delta_symbol}Y1 (mm)", "G319"),
        ("monthly_field_size_accuracy_y2", f"Rad-Dig - {delta_symbol}Y2 (mm)", "H319"),
    ],
}

QA_IMAGE_QUALITY = {
    "name": "Image Quality - PipsPro KV",
    "data": [
        ("monthly_image_quality_large_f30", "Large Focal Spot - f30 (lp/mm)", "F328"),
        ("monthly_image_quality_large_f10", "Large Focal Spot - f10 (lp/mm)", "H328"),
        ("monthly_image_quality_large_CNR", "Large Focal Spot - CNR", "J328"),
        (
            "monthly_image_quality_small_f30",
            "Small Focal Spot - Titanium Filter - f30 (lp/mm)",
            "F329",
        ),
        (
            "monthly_image_quality_small_f10",
            "Small Focal Spot - Titanium Filter - f10 (lp/mm)",
            "H329",
        ),
        (
            "monthly_image_quality_small_CNR",
            "Small Focal Spot - Titanium Filter - CNR",
            "J329",
        ),
    ],
}

QA_KVP_DOSE = {
    "name": "kVp Accuracy/Dose",
    "data": [
        ("monthly_kvp_dose_75_reading", "75 kVp - Reading", "D337"),
        ("monthly_kvp_dose_75_dose", "75 kVp - Dose", "G337"),
        ("monthly_kvp_dose_125_reading", "125 kVp - Reading", "D338"),
        ("monthly_kvp_dose_125_dose", "125 kVp - Dose", "G338"),
    ],
}

QA_CBCT_12 = {
    "name": "CBCT Measurements",
    "data": [
        ("monthly_cbct_8_1_IQ", "kv CBCT Image Quality (Overall)", "G351"),
        ("monthly_cbct_8_2_avg", "Geometry - avg Slice Width (mm)", "E355"),
        ("monthly_cbct_8_2_min", "Geometry - min Distance (mm)", "E356"),
        ("monthly_cbct_8_2_max", "Geometry - max Distance (mm)", "E357"),
        ("monthly_cbct_8_3_delrin", "CT Number Accuracy - Delrin CT#", "E361"),
        ("monthly_cbct_8_3_air", "CT Number Accuracy - Air CT#", "E362"),
        ("monthly_cbct_8_3_ldpe", "CT Number Accuracy - LDPE CT#", "E363"),
        ("monthly_cbct_8_3_teflon", "CT Number Accuracy - Teflon CT#", "E364"),
        ("monthly_cbct_8_4_mtf", "High Contrast Resolution (rel. MTF)", "E368"),
        (
            "monthly_cbct_8_5_signal_min",
            "Uniformity - min Signal (CT#) in 5 Regions",
            "E372",
        ),
        (
            "monthly_cbct_8_5_signal_max",
            "Uniformity - max Signal (CT#) in 5 Regions",
            "F372",
        ),
        (
            "monthly_cbct_8_5_noise_min",
            "Uniformity - min Noise (SD) in 5 Regions",
            "E373",
        ),
        (
            "monthly_cbct_8_5_noise_max",
            "Uniformity - max Noise (SD) in 5 Regions",
            "F373",
        ),
        (
            "monthly_cbct_8_6_delrin_ldpe",
            "CNR - Delrin-LDPE",
            "E377",
        ),
        (
            "monthly_cbct_8_6_noise",
            "CNR - Noise (SD)",
            "E378",
        ),
        ("monthly_cbct_8_6_cnr", "CNR - CNR", "E379"),
    ],
}

ALL_MONTHLY_QA = [
    QA_OUTPUT,
    QA_OUTPUT_RESULTS,
    QA_EDW,
    QA_EDW_RESULTS,
    QA_MLC,
    QA_MLC_RESULTS,
    QA_VMAT,
    QA_VMAT_RESULT,
    QA_dMLC_SEQUENCE,
    QA_TMR_PHOTON,
    QA_TMR_PHOTON_RESULT,
    QA_CBCT,
    QA_CBCT_RESULT,
    QA_ELECTRON,
    QA_ELECTRON_DOSE,
    QA_LIGHT_RADIATION_COINCIDENCE_JAWS,
    QA_LIGHT_RADIATION_COINCIDENCE_JAWS_RESULT,
    QA_LIGHT_RADIATION_COINCIDENCE_MLC,
    QA_LIGHT_RADIATION_COINCIDENCE_MLC_RESULT,
    QA_RADIATION_FIELD_EDGE_ALIGNMENT,
    QA_MV_IMAGE_UNIFORMITY,
    QA_PICKET_FENCE,
    QA_EPI,
    QA_VMAT_MECHANICAL,
    QA_REGISTRATION,
    QA_MOTION_MANAGEMENT,
    QA_PLANAR_BLADE_TRACKING,
    QA_FIELD_SIZE_ACCURACY,
    QA_IMAGE_QUALITY,
    QA_KVP_DOSE,
    QA_CBCT_12,
]
