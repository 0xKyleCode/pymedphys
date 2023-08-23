import numpy as np

OC_6X_AVG = 0
try:
    OC_6X_AVG = np.mean([OC_6X_10x10_1, OC_6X_10x10_2, OC_6X_10x10_3])
except:
    try:
        OC_6X_AVG = np.mean([OC_6X_10x10_1, OC_6X_10x10_2])
    except:
        OC_6X_AVG = OC_6X_10x10_1


EDW_6X_AVG = np.mean([EDW60IN_6X, EDW60OUT_6X])

EDWF_6X = EDW_6X_AVG / OC_6X_AVG
