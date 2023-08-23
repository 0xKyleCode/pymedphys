import numpy as np

OC_6X_AVG = 0
try:
    OC_6X_AVG = np.mean([OC_6X_10x10_1, OC_6X_10x10_2, OC_6X_10x10_3])
except:
    try:
        OC_6X_AVG = np.mean([OC_6X_10x10_1, OC_6X_10x10_2])
    except:
        OC_6X_AVG = OC_6X_10x10_1

dmlc_avg = np.mean([dmlc_HN_1, dmlc_HN_2])

dmlc_HN_ratio = dmlc_avg / OC_6X_AVG
