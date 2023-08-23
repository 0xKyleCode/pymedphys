import numpy as np

OC_12E_AVG = 0
try:
    OC_12E_AVG = np.mean([OC_12E_1, OC_12E_2, OC_12E_3])
except:
    try:
        OC_12E_AVG = np.mean([OC_12E_1, OC_12E_2])
    except:
        OC_12E_AVG = OC_12E_1


machine = {
    1: vifir_tb1_electron_12e_fc,
    2: viarbutus_tb2_electron_12e_fc,
    3: vibirch_tb3_electron_12e_fc,
}

OC_6X_10x10_DOSE = (
    machine[META["unit_number"]] * OC_12E_AVG * nd_electron * ctp_electron
)
