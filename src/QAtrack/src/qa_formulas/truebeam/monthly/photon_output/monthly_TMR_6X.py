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

monthly_TMR_avg = np.mean([monthly_TMR_6X_1, monthly_TMR_6X_2])

monthly_TMR_6X = monthly_OC_6X_AVG / monthly_TMR_avg
