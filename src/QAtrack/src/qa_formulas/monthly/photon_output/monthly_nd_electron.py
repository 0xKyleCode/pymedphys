markus_vals = {
    "MKS1": markus_1_nd,
    "MKS2": markus_2_nd,
    "MKS4": markus_4_nd,
    "MKSavd": markus_savd_nd,
}

nd_electron = markus_vals[markus_probe_id] / markus_vals["MKS1"]
