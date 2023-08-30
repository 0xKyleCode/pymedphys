photon_probe_vals = {
    "PTW7": ptw_7_nd,
    "PTW2": ptw_2_nd,
    "PTW3": ptw_3_nd,
    "PTW4": ptw_4_nd,
    "PTW5": ptw_5_nd,
    "PTW6": ptw_6_nd,
}

nd_photon = photon_probe_vals[ptw_probe_id] / photon_probe_vals["PTW7"]
