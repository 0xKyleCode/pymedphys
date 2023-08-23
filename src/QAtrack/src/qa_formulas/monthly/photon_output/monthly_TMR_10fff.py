import numpy as np

OC_10Xfff_AVG = 0
try:
    OC_10Xfff_AVG = np.mean([OC_10Xfff_10x10_1, OC_10Xfff_10x10_2, OC_10Xfff_10x10_3])
except:
    try:
        OC_10Xfff_AVG = np.mean([OC_10Xfff_10x10_1, OC_10Xfff_10x10_2])
    except:
        OC_10Xfff_AVG = OC_10Xfff_10x10_1

tmr_avg = np.mean([TMR_10fff_1, TMR_10fff_2])

TMR_10fff = tmr_avg / OC_10Xfff_AVG
