from excel.utils.excel_dataclass import ExcelData

MISC_TEMPERATURE = [
    ExcelData(
        "Temperature (Photon)",
        "t_probe_photon",
        "Probe Temperature (photon)",
        False,
        "Main",
        "G35",
        "measurement",
        "%0.1f",
        "",
        1,
    ),
    ExcelData(
        "Temperature (Electron)",
        "t_probe_electron",
        "Probe Temperature (electron)",
        False,
        "Main",
        "G105",
        "measurement",
        "%0.1f",
        "",
        1,
    ),
]
