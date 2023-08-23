import numpy as np

OC_16E_AVG = 0
try:
    OC_16E_AVG = np.mean([OC_16E_1, OC_16E_2, OC_16E_3])
except:
    try:
        OC_16E_AVG = np.mean([OC_16E_1, OC_16E_2])
    except:
        OC_16E_AVG = OC_16E_1


machine = {
    1: vifir_tb1_electron_16e_fc,
    2: viarbutus_tb2_electron_16e_fc,
    3: vibirch_tb3_electron_16e_fc,
}

OC_6X_10x10_DOSE = (
    machine[META["unit_number"]] * OC_16E_AVG * nd_electron * ctp_electron
)
