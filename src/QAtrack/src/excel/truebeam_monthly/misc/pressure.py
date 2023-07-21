from excel.utils.excel_dataclass import ExcelData

MISC_PRESSURE = [
    ExcelData(
        "Pressure (Photon)",
        "p_corr_photon",
        "Corrected Pressure (photon)",
        False,
        "Main",
        "D35",
        "measurement",
        "%0.1f",
        "",
        1,
    ),
    ExcelData(
        "Pressure (Electron)",
        "p_corr_electron",
        "Corrected Pressure (electron)",
        False,
        "Main",
        "D105",
        "measurement",
        "%0.1f",
        "",
        1,
    ),
]
