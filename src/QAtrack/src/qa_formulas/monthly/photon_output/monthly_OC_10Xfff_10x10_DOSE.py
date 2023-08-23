import numpy as np

monthly_OC_10Xfff_AVG = 0
try:
    monthly_OC_10Xfff_AVG = np.mean(
        [
            monthly_OC_10Xfff_10x10_1,
            monthly_OC_10Xfff_10x10_2,
            monthly_OC_10Xfff_10x10_3,
        ]
    )
except:
    try:
        monthly_OC_10Xfff_AVG = np.mean(
            [monthly_OC_10Xfff_10x10_1, monthly_OC_10Xfff_10x10_2]
        )
    except:
        monthly_OC_10Xfff_AVG = monthly_OC_10Xfff_10x10_1


machine = {
    1: vifir_tb1_photon_10xfff_fc,
    2: viarbutus_tb2_photon_10xfff_fc,
    3: vibirch_tb3_photon_10xfff_fc,
    4: vicedar_tb4_photon_10xfff_fc,
    5: vispruce_tb5_photon_10xfff_fc,
    6: vioak_tb6_photon_10xfff_fc,
}

monthly_OC_10Xfff_10x10_DOSE = (
    machine[META["unit_number"]] * monthly_OC_10Xfff_AVG * nd_photon * ctp_photon
)
