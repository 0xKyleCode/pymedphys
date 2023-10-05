import os
import datetime

import pandas as pd
from pytz import utc
import requests
from qa_machines.truebeam.monthly import BCCAMonthlyTruebeamQA
from qa_api.upload.upload_template import QATrackUpload
from test_lists.truebeam.monthly.test_lists.photon_output.kv_cbct import (
    QUARTERLY_KV_CBCT,
)
from test_lists.truebeam.monthly.test_lists.planar_kv.planar_kv import MONTHLY_PLANAR_KV
from test_lists.truebeam.test_list_definitions import MONTHLY_TEST_LISTS, Monthly
from qa_api.utils.request import get, post


class MonthlyTruebeamUpload(QATrackUpload):
    def __init__(self, file_name: str):
        """

        Initialize MonthlyTruebeamUpload class

        Args:
            file_root (str): Root folder of the file
            file_name (str): Name of the file
        """

        # Set the monthly template location here
        current_dir: str = os.getcwd()
        template_file_name = os.path.join(
            current_dir,
            "src",
            "QAtrack",
            "data",
            "truebeam",
            "monthly",
            "monthly_template.xlsm",
        )

        self.plan_filename = os.path.join(
            current_dir,
            "src",
            "QAtrack",
            "data",
            "truebeam",
            "monthly",
            "monthly_definitions.xlsx",
        )

        super().__init__(file_name, template_file_name)
        self.setup_machine_template()
        self.setup_machine()

    def test(self):
        self.template.add_tests_to_main()
        return self.template.plans

    def setup_machine_template(self):
        """
        Setup machine template for QATrack+ API
        """
        self.template = BCCAMonthlyTruebeamQA(self.file_template, self.plan_filename)
        print("Set up template machine")

    def setup_machine(self):
        """
        Setup machine for QATrack+ API
        """
        self.machine = BCCAMonthlyTruebeamQA(self.file_name, self.plan_filename)
        if not self.machine.is_qa_sheet():
            raise RuntimeError("File is not a QA sheet")

        machine_info = self.machine.get_machine()
        sheet_info = self.machine.get_sheet_info()
        print(
            f"Uploading Monthly report for {machine_info['long_name']} ({machine_info['model']}) from {sheet_info[4]}."
        )

    def setup_template_sheet_data(self):
        """
        Setup template sheet data for QATrack+ API
        """
        data = self.read_excel_sheets(
            "Main", self.template.filename, self.machine.filename
        )
        print("Grabbed all data.")
        return data

    # Specific to monthly. Break up into cycles and upload
    # Cycle 1 and 2 are the same
    # Cycle 3 has extras
    def upload_data(self):
        data = self.setup_template_sheet_data()
        tests = (
            MONTHLY_TEST_LISTS[Monthly.ELECTRON.value]
            if self.machine.is_electron()
            else MONTHLY_TEST_LISTS[Monthly.NO_ELECTRON.value]
        )

        # Check if data filled out for this one
        params = {
            "unit__number": self.machine.get_machine()["id"],
        }

        info = get("/qa/unittestcollections/", params=params)

        which_cycle = self._check_cycle(data, info)
        print(f"Uploading cycle {which_cycle} data.")

        creation_time = os.path.getctime(self.machine.filename)
        str_create_time = datetime.datetime.fromtimestamp(creation_time)
        hours_to_add = datetime.timedelta(hours=2)
        # Construct the data
        utc_url = info["results"][0]["url"]
        utc_data = {
            "unit_test_collection": utc_url,
            "day": which_cycle,
            "in_progress": False,
            "include_for_scheduling": True,
            "work_started": str_create_time.strftime("%Y-%m-%d %H:%M"),
            "work_completed": (str_create_time + hours_to_add).strftime(
                "%Y-%m-%d %H:%M"
            ),
            "comment": "Auto added from excel sheets.",
            "tests": self._produce_tests(data, tests, which_cycle),
            "attachments": [],
        }
        return utc_data
        # Lets try it out!
        resp = post("/qa/testlistinstances/", data=utc_data)
        if resp.status_code == requests.codes.CREATED:  # http code 201
            completed_url = resp.json()["site_url"]
            print(
                "Test List performed successfully! View your Test List Instance at %s"
                % completed_url
            )
        else:
            print(
                f"Your request failed with error {resp.status_code} ({resp.reason}) ({resp.json()})"
            )

    def _produce_tests(self, data: pd.DataFrame, test_lists: list, cycle: int) -> dict:
        """
        Produce tests for QATrack+ API

        Args:
            data (pd.DataFrame): Data from spreadsheet
            tests (list): Tests to compare against
            cycle (int): Cycle to check

        Returns:
            dict: Tests for QATrack+ API
        """

        tests = {}
        current_cycle = test_lists["cycle"][cycle]
        for test_lists in current_cycle["name"]["sublists"]:
            if len(test_lists["name"]["test_lists"]) > 0:
                for test_list in test_lists["name"]["test_lists"]:
                    for test in test_list["name"]["tests"]:
                        try:
                            self._process_tests(data, tests, test)
                        except Exception as e:
                            continue
            else:
                for test in test_lists["name"]["tests"]:
                    try:
                        self._process_tests(data, tests, test)
                    except Exception as e:
                        continue
        return tests

    def _remove_hash(self, value):
        if isinstance(value, int):
            return value
        elif isinstance(value, str):
            return value.replace("#", "")
        else:
            return value

    def _process_tests(self, data: pd.DataFrame, tests: dict, test: dict) -> dict:
        value = data.loc[data["name"] == test["name"]]["value"].values[0]
        if "IF" not in str(value):
            tests[test["name"]] = {
                "value": self._remove_hash(value)
                if "=" not in str(value)
                else eval(value[1:]),
                "skipped": False if value is not None else True,
            }

    def _check_cycle(self, data: pd.DataFrame, info: dict) -> int:
        """
        Check which cycle the data is for

        Args:
            data (pd.DataFrame): Data from spreadsheet
            tests (list): Tests to compare against
            cycle (int): Cycle to check

        Returns:
            int: Cycle number
        """

        cycle = info["results"][0]["next_day"]
        # If the next one isn't kv CBCT, ensures no issues.
        if cycle == 2:
            cycle = 0

        test_lists = [QUARTERLY_KV_CBCT, MONTHLY_PLANAR_KV]
        for test_list in test_lists:
            for tests in (
                test_list["test_lists"]
                if len(test_list["test_lists"]) > 0
                else test_list["sublists"]
            ):
                for test in tests["name"]["tests"]:
                    value = data.loc[data["name"] == test["name"]]["value"].values[0]
                    if value is not None:
                        cycle = 2

        return cycle
