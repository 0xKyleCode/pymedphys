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

monthly_VMAT_avg = np.mean([monthly_VMAT_factor_ccw, monthly_VMAT_factor_cw])

monthly_VMAT_6X_factor = monthly_VMAT_avg / monthly_OC_6X_AVG
