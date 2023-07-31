photon_probe_vals = {
    "ptw_7_nd": ptw_7_nd,
    "ptw_2_nd": ptw_2_nd,
    "ptw_3_nd": ptw_3_nd,
    "ptw_4_nd": ptw_4_nd,
    "ptw_5_nd": ptw_5_nd,
    "ptw_6_nd": ptw_6_nd,
}

markus_vals = {
    "markus_1_nd": markus_1_nd,
    "markus_2_nd": markus_2_nd,
    "markus_4_nd": markus_4_nd,
    "markus_savd_nd": markus_savd_nd,
}


def get_electron_markus(markus_probe_id: str) -> float:
    """
    Gets the correct electron markus value based on the probe id

    Args:
        markus_probe_id (str):  The probe id

    Returns:
        float: The markus value
    """
    return markus_vals[markus_probe_id]


def get_photon_probe(ptw_probe_id: str) -> float:
    """
    Gets the correct photon ptw value based on the probe id

    Args:
        ptw_probe_id (str): The probe id

    Returns:
        float: The ptw value
    """
    return photon_probe_vals[ptw_probe_id]
