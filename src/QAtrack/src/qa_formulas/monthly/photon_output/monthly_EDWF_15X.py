import numpy as np

OC_15X_AVG = 0
try:
    OC_15X_AVG = np.mean([OC_15X_10x10_1, OC_15X_10x10_2, OC_15X_10x10_3])
except:
    try:
        OC_15X_AVG = np.mean([OC_15X_10x10_1, OC_15X_10x10_2])
    except:
        OC_15X_AVG = OC_15X_10x10_1


EDW_15X_AVG = np.mean([EDW60IN_15X, EDW60OUT_15X])

EDWF_15X = EDW_15X_AVG / OC_15X_AVG
