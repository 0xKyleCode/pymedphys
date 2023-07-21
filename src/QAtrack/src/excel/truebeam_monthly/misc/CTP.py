from excel.utils.excel_dataclass import ExcelData

MISC_CTP = [
    ExcelData(
        "CTP (Photon)",
        "ctp_photon",
        "Corrected Temperature Pressure (photon)",
        False,
        "Main",
        "J35",
        "calculation",
        "%0.3f",
        "ctp_photon=(760/p_corr_photon)*(t_probe_photon+273.15)/295.15",
        1,
        "",
    ),
    ExcelData(
        "CTP (Electron)",
        "ctp_electron",
        "Corrected Temperature Pressure (electron)",
        False,
        "Main",
        "J105",
        "calculation",
        "%0.3f",
        "ctp_electron=(760/p_corr_electron)*(t_probe_electron+273.15)/295.15",
        1,
        "",
    ),
]
