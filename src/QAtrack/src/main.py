import pandas as pd
from machines.truebeam.truebeam_monthly import BCCAMonthlyTruebeamQA


# Open a file using pandas
def open_excel(file):
    df = pd.read_excel(file)

    file_name = r"src\QAtrack\data\VIFIR_TB1_JUN_2023_P.xlsm"

    print(BCCAMonthlyTruebeamQA.default_qa_name("fir"))
    print(BCCAMonthlyTruebeamQA.get_sheet_info(file_name))
    BCCAMonthlyTruebeamQA.read_main_sheet(file_name)


if __name__ == "__main__":
    open_excel("src\\QAtrack\\data\\Physicist TrueBeam Monthly QA TEMPLATE.xlsm")
