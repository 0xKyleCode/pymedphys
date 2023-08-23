import numpy as np

OC_10X_AVG = 0
try:
    OC_10X_AVG = np.mean([OC_10X_10x10_1, OC_10X_10x10_2, OC_10X_10x10_3])
except:
    try:
        OC_10X_AVG = np.mean([OC_10X_10x10_1, OC_10X_10x10_2])
    except:
        OC_10X_AVG = OC_10X_10x10_1

tmr_avg = np.mean([TMR_10X_1, TMR_10X_2])

TMR_10X = tmr_avg / OC_10X_AVG
