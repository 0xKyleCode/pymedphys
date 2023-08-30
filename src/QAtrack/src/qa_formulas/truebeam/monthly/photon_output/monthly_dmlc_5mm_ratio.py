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

monthly_dmlc_avg = np.mean([monthly_dmlc_5mm_1, monthly_dmlc_5mm_2])

monthly_dmlc_5mm_ratio = monthly_dmlc_avg / monthly_OC_6X_AVG
