import numpy as np

OC_15X_AVG = 0
try:
    OC_15X_AVG = np.mean([OC_15X_10x10_1, OC_15X_10x10_2, OC_15X_10x10_3])
except:
    try:
        OC_15X_AVG = np.mean([OC_15X_10x10_1, OC_15X_10x10_2])
    except:
        OC_15X_AVG = OC_15X_10x10_1

tmr_avg = np.mean([TMR_15X_1, TMR_15X_2])

TMR_15X = tmr_avg / OC_15X_AVG
