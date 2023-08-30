from constants.truebeam.monthly import BCCAMonthlyTruebeamQA
from qa_api.upload.upload_template import QATrackUpload


class MonthlyTruebeamUpload(QATrackUpload):
    def __init__(self, file_name: str, file_path: str, file_template: str):
        super().__init__(file_name, file_path, file_template)
        self.setup_machine_template()
        self.setup_machine()

    def setup_machine_template(self):
        """
        Setup machine template for QATrack+ API
        """
        self.template = BCCAMonthlyTruebeamQA(self.file_template)

    def setup_machine(self):
        """
        Setup machine for QATrack+ API
        """
        file_location = self.find_file_recursive(self.file_path, self.file_name)
        self.machine = BCCAMonthlyTruebeamQA(file_location)
        if not self.machine.is_qa_sheet():
            raise RuntimeError("File is not a QA sheet")

        machine_info = self.machine.get_machine()
        print(machine_info)

    def setup_template_sheet_data(self):
        """
        Setup template sheet data for QATrack+ API
        """
        data = self.read_excel_sheets("Main", self.template.book, self.machine.book)
