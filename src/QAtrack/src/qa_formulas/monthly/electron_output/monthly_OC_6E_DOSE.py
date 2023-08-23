import numpy as np

OC_6E_AVG = 0
try:
    OC_6E_AVG = np.mean([OC_6E_1, OC_6E_2, OC_6E_3])
except:
    try:
        OC_6E_AVG = np.mean([OC_6E_1, OC_6E_2])
    except:
        OC_6E_AVG = OC_6E_1


machine = {
    1: vifir_tb1_electron_6e_fc,
    2: viarbutus_tb2_electron_6e_fc,
    3: vibirch_tb3_electron_6e_fc,
}

OC_6X_10x10_DOSE = machine[META["unit_number"]] * OC_6E_AVG * nd_electron * ctp_electron
