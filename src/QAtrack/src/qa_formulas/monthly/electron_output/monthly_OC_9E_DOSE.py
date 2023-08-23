import numpy as np

OC_9E_AVG = 0
try:
    OC_9E_AVG = np.mean([OC_9E_1, OC_9E_2, OC_9E_3])
except:
    try:
        OC_9E_AVG = np.mean([OC_9E_1, OC_9E_2])
    except:
        OC_9E_AVG = OC_9E_1


machine = {
    1: vifir_tb1_electron_9e_fc,
    2: viarbutus_tb2_electron_9e_fc,
    3: vibirch_tb3_electron_9e_fc,
}

OC_6X_10x10_DOSE = machine[META["unit_number"]] * OC_9E_AVG * nd_electron * ctp_electron
