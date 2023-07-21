from excel.truebeam_monthly.constants.photons.fir import CONSTANTS_PHOTON_FC_FIR
from excel.truebeam_monthly.constants.photons.arbutus import CONSTANTS_PHOTON_FC_ARBUTUS
from excel.truebeam_monthly.constants.photons.birch import CONSTANTS_PHOTON_FC_BIRCH
from excel.truebeam_monthly.constants.photons.cedar import CONSTANTS_PHOTON_FC_CEDAR
from excel.truebeam_monthly.constants.photons.spruce import CONSTANTS_PHOTON_FC_SPRUCE
from excel.truebeam_monthly.constants.photons.oak import CONSTANTS_PHOTON_FC_OAK

CONSTANTS_PHOTON_FC: list = (
    CONSTANTS_PHOTON_FC_FIR
    + CONSTANTS_PHOTON_FC_ARBUTUS
    + CONSTANTS_PHOTON_FC_BIRCH
    + CONSTANTS_PHOTON_FC_CEDAR
    + CONSTANTS_PHOTON_FC_SPRUCE
    + CONSTANTS_PHOTON_FC_OAK
)
