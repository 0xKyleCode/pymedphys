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


monthly_EDW_6X_AVG = np.mean([monthly_EDW60IN_6X, monthly_EDW60OUT_6X])

monthly_EDWF_6X = monthly_EDW_6X_AVG / monthly_OC_6X_AVG
