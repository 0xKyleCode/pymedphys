import numpy as np

monthly_OC_10X_AVG = 0
try:
    monthly_OC_10X_AVG = np.mean(
        [monthly_OC_10X_10x10_1, monthly_OC_10X_10x10_2, monthly_OC_10X_10x10_3]
    )
except:
    try:
        monthly_OC_10X_AVG = np.mean([monthly_OC_10X_10x10_1, monthly_OC_10X_10x10_2])
    except:
        monthly_OC_10X_AVG = monthly_OC_10X_10x10_1

monthly_TMR_avg = np.mean([monthly_TMR_10X_1, monthly_TMR_10X_2])

monthly_TMR_10X = monthly_OC_10X_AVG / monthly_TMR_avg
