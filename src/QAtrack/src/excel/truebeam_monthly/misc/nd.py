from excel.utils.excel_dataclass import ExcelData

MISC_ND = [
    ExcelData(
        "ND Ratio (Photon)",
        "nd_photon",
        "ND Ratio (photon)",
        False,
        "Main",
        "J37",
        "calculation",
        "%0.3f",
        """
        probe_vals = {
            "ptw_7_nd": ptw_7_nd,
            "ptw_2_nd": ptw_2_nd,
            "ptw_3_nd": ptw_3_nd,
            "ptw_4_nd": ptw_4_nd,
            "ptw_5_nd": ptw_5_nd,
            "ptw_6_nd": ptw_6_nd,
        }
        nd_photon=probe_vals[ptw_probe_id]
        """,
        1,
        "",
    ),
    ExcelData(
        "ND Ratio (Electron)",
        "nd_electron",
        "ND Ratio (electron)",
        False,
        "Main",
        "J37",
        "calculation",
        "%0.3f",
        """
        markus_vals = {
            "markus_1_nd": markus_1_nd,
            "markus_2_nd": markus_2_nd,
            "markus_4_nd": markus_4_nd,
            "markus_savd_nd": markus_savd_nd,
        }
        nd_electron=markus_vals[markus_probe_id]
        """,
        1,
        "",
    ),
]
