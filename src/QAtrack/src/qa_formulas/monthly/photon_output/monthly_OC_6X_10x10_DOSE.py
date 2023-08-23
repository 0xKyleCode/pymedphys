import numpy as np

monthly_OC_6X_AVG = 0
try:
    monthly_OC_6X_AVG = np.mean(
        [monthly_OC_6X_10x10_1, monthly_OC_6X_10x10_2, monthly_OC_6X_10x10_3]
    )
except:
    try:
        monthly_OC_6X_AVG = np.mean([monthly_OC_6X_10x10_1, monthly_OC_6X_10x10_2])
    except:
        monthly_OC_6X_AVG = monthly_OC_6X_10x10_1


machine = {
    1: vifir_tb1_photon_6x_fc,
    2: viarbutus_tb2_photon_6x_fc,
    3: vibirch_tb3_photon_6x_fc,
    4: vicedar_tb4_photon_6x_fc,
    5: vispruce_tb5_photon_6x_fc,
    6: vioak_tb6_photon_6x_fc,
}

monthly_OC_6X_10x10_DOSE = (
    machine[META["unit_number"]] * monthly_OC_6X_AVG * nd_photon * ctp_photon
)
