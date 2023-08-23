import numpy as np

monthly_OC_10Xfff_AVG = 0
try:
    monthly_OC_10Xfff_AVG = np.mean(
        [
            monthly_OC_10Xfff_10x10_1,
            monthly_OC_10Xfff_10x10_2,
            monthly_OC_10Xfff_10x10_3,
        ]
    )
except:
    try:
        monthly_OC_10Xfff_AVG = np.mean(
            [monthly_OC_10Xfff_10x10_1, monthly_OC_10Xfff_10x10_2]
        )
    except:
        monthly_OC_10Xfff_AVG = monthly_OC_10Xfff_10x10_1

monthly_TMR_avg = np.mean([monthly_TMR_10fff_1, monthly_TMR_10fff_2])

monthly_TMR_10fff = monthly_OC_10Xfff_AVG / monthly_TMR_avg
