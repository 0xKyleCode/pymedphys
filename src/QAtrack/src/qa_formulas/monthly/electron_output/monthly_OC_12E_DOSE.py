import numpy as np

monthly_OC_12E_AVG = 0
try:
    monthly_OC_12E_AVG = np.mean([monthly_OC_12E_1, monthly_OC_12E_2, monthly_OC_12E_3])
except:
    try:
        monthly_OC_12E_AVG = np.mean([monthly_OC_12E_1, monthly_OC_12E_2])
    except:
        monthly_OC_12E_AVG = monthly_OC_12E_1


machine = {
    1: vifir_tb1_electron_12e_fc,
    2: viarbutus_tb2_electron_12e_fc,
    3: vibirch_tb3_electron_12e_fc,
}

monthly_OC_12E_DOSE = (
    machine[META["unit_number"]] * monthly_OC_12E_AVG * nd_electron * ctp_electron
)
