import numpy as np

OC_10Xfff_AVG = 0
try:
    OC_10Xfff_AVG = np.mean([OC_10Xfff_10x10_1, OC_10Xfff_10x10_2, OC_10Xfff_10x10_3])
except:
    try:
        OC_10Xfff_AVG = np.mean([OC_10Xfff_10x10_1, OC_10Xfff_10x10_2])
    except:
        OC_10Xfff_AVG = OC_10Xfff_10x10_1


machine = {
    1: vifir_tb1_photon_10xfff_fc,
    2: viarbutus_tb2_photon_10xfff_fc,
    3: vibirch_tb3_photon_10xfff_fc,
    4: vicedar_tb4_photon_10xfff_fc,
    5: vispruce_tb5_photon_10xfff_fc,
    6: vioak_tb6_photon_10xfff_fc,
}

OC_10Xfff_10x10_DOSE = (
    machine[META["unit_number"]] * OC_10Xfff_AVG * nd_photon * ctp_photon
)
