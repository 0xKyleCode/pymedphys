import numpy as np

OC_10x_AVG = 0
try:
    OC_10x_AVG = np.mean([OC_10X_10x10_1, OC_10X_10x10_2, OC_10X_10x10_3])
except:
    try:
        OC_10x_AVG = np.mean([OC_10X_10x10_1, OC_10X_10x10_2])
    except:
        OC_10x_AVG = OC_10X_10x10_1


EDW_10x_AVG = np.mean([EDW60IN_10X, EDW60OUT_10X])

EDWF_10X = EDW_10x_AVG / OC_10x_AVG
