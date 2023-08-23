import numpy as np

OC_20E_AVG = 0
try:
    OC_20E_AVG = np.mean([OC_20E_1, OC_20E_2, OC_20E_3])
except:
    try:
        OC_20E_AVG = np.mean([OC_20E_1, OC_20E_2])
    except:
        OC_20E_AVG = OC_20E_1


machine = {
    1: vifir_tb1_electron_20e_fc,
    2: viarbutus_tb2_electron_20e_fc,
    3: vibirch_tb3_electron_20e_fc,
}

OC_6X_10x10_DOSE = (
    machine[META["unit_number"]] * OC_20E_AVG * nd_electron * ctp_electron
)
