import numpy as np

monthly_OC_10x_AVG = 0
try:
    monthly_OC_10x_AVG = np.mean(
        [monthly_OC_10X_10x10_1, monthly_OC_10X_10x10_2, monthly_OC_10X_10x10_3]
    )
except:
    try:
        monthly_OC_10x_AVG = np.mean([monthly_OC_10X_10x10_1, monthly_OC_10X_10x10_2])
    except:
        monthly_OC_10x_AVG = monthly_OC_10X_10x10_1


monthly_EDW_10x_AVG = np.mean([monthly_EDW60IN_10X, monthly_EDW60OUT_10X])

monthly_EDWF_10X = monthly_EDW_10x_AVG / monthly_OC_10x_AVG
