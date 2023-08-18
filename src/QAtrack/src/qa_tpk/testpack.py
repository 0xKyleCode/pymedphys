import os
import json
import pandas as pd
import uuid
import copy
from openpyxl import load_workbook
from collections import defaultdict
from datetime import datetime, timezone

from constants.test_list_definitions import ALL_TEST_LISTS

TPK_CALC_TEMPLATE = os.path.join(
    os.getcwd(), "src", "QAtrack", "data", "constant_tpk", "sample_calc.tpk"
)

TPK_CONSTANT_TEMPLATE = os.path.join(
    os.getcwd(), "src", "QAtrack", "data", "constant_tpk", "sample_constant.tpk"
)

TPK_NUMERIC_TEMPLATE = os.path.join(
    os.getcwd(), "src", "QAtrack", "data", "constant_tpk", "sample_numeric.tpk"
)

TPK_PULLDOWN_TEMPLATE = os.path.join(
    os.getcwd(), "src", "QAtrack", "data", "constant_tpk", "sample_pulldown.tpk"
)

TPK_DEPEN_TEMPLATE = {
    "model": "qa.category",
    "fields": {
        "name": "Template",
        "slug": "template",
        "description": "Template tests used for bulk test importing",
    },
}


class BCCATestpack:
    def read_excel_sheet(self, type: str, file_name: str) -> pd.DataFrame:
        """
        Reads the excel sheet and returns a dataframe of main.

        Args:
            file_name (str): _description_

        Returns:
            pd.DataFrame: _description_
        """
        # Load your workbook
        workbook = load_workbook(filename=file_name)
        # Get your sheets
        sheet1 = workbook[f"QATrack_{type}"]
        sheet2 = workbook[type]
        sheet3 = workbook["QATrack_Definitions"]

        # Initialize an empty dictionary to store names, corresponding values and cell locations
        data = defaultdict(dict)

        # Iterate through all cells in sheet1
        for row in sheet1.iter_rows():
            for cell in row:
                # Check if cell is not empty and contains a string
                if (
                    cell.value
                    and isinstance(cell.value, str)
                    and cell.value.startswith("#!")
                ):
                    # Get corresponding value from same cell in sheet2
                    value = sheet2[cell.coordinate].value
                    # Store name and value in the dictionary
                    data[cell.coordinate]["name"] = cell.value[2:]
                    data[cell.coordinate]["value"] = value

        # Now find matching short_name rows in Sheet3 and gather the row data
        for row in sheet3.iter_rows():
            for cell in row:
                # If the cell is in the 'short_name' column and its value is a name we've gathered,
                # get the entire row data

                if cell.column_letter == "B" and any(
                    cell.value == info["name"] for info in data.values()
                ):
                    for cell_in_row in row:
                        # Store the data using the column header as key
                        data[
                            next(
                                key
                                for key, value in data.items()
                                if value["name"] == cell.value
                            )
                        ][
                            sheet3[cell_in_row.column_letter + "1"].value
                        ] = cell_in_row.value

        # Turn data into a dataframe
        df = pd.DataFrame(data.values())
        return df

    def load_tpk_template(self, type: str) -> dict:
        """
        Loads the TPK file.

        Args:
            file_name (str): The TPK file name.

        Returns:
            dict: The TPK file in json format
        """
        if type == "calculation":
            with open(TPK_CALC_TEMPLATE) as f:
                template = json.load(f)

        elif type == "constant":
            with open(TPK_CONSTANT_TEMPLATE) as f:
                template = json.load(f)
        elif type == "numeric":
            with open(TPK_NUMERIC_TEMPLATE) as f:
                template = json.load(f)
        elif type == "pulldown":
            with open(TPK_PULLDOWN_TEMPLATE) as f:
                template = json.load(f)

        template["objects"]["tests"] = [
            json.loads(s) for s in template["objects"]["tests"]
        ]
        return template

    def write_test_tpk(self, testpack_dict: dict, outfile: str):
        """
        Writes the testpack to a file.

        Args:
            testpack_dict (dict): The testpack in dictionary format.
            outfile (str): The output file name.
        """
        testpack_dict["objects"]["tests"] = [
            json.dumps(s) for s in testpack_dict["objects"]["tests"]
        ]

        testpack_dict["objects"]["testlists"] = [
            json.dumps(s) for s in testpack_dict["objects"]["testlists"]
        ]
        with open(outfile, "w") as f:
            json.dump(testpack_dict, f, indent=4)

    def make_calculation_tpk(self, df: pd.DataFrame) -> list[dict]:
        """
        Makes a QATrack+ test list for calulations

        Args:
            df (pd.DataFrame): The dataframe containing the test data.

        Returns:
            list[dict]: The test list in dictionary format.
        """
        tests = []
        # do calculation first
        calc_template = self.load_tpk_template("calculation")
        for index, row in df[df["type"] == "calculation"].iterrows():
            # Copy the first element of the tests array, which will be a dictionary of a test
            current_test = copy.deepcopy(calc_template["objects"]["tests"][0])

            # Set key to short name
            current_test["key"][0] = row["short"]

            # Based off short name, we're gonna read the in contents of the python file and use that as calculation prodecure
            # Read the content of the Python file
            with open(
                os.path.join(
                    os.getcwd(),
                    "src",
                    "QAtrack",
                    "src",
                    "qa_formulas",
                    f"{row['short']}.py",
                )
            ) as python_file:
                python_code = python_file.read()

            # Set object params
            temp_field = {
                "name": row["short"],
                "display_name": row["long"],
                "slug": row["short"],
                "description": row["description"],
                "procedure": None,
                "category": row["category"].split(","),
                "chart_visibility": True,
                "type": "composite",
                "flag_when": None,
                "hidden": False,
                "skip_without_comment": False,
                "require_comment": False,
                "display_image": False,
                "choices": None,
                "constant_value": None,
                "wrap_low": None,
                "wrap_high": None,
                "calculation_procedure": python_code,
                "formatting": row["format"],
            }
            current_test["object"]["fields"] = temp_field

            if row["category"] is not None:
                for c in row["category"].split(","):
                    depen = copy.deepcopy(TPK_DEPEN_TEMPLATE)
                    depen["fields"]["name"] = c
                    depen["fields"]["slug"] = c.lower()
                    current_test["dependencies"].append(depen)

            tests.append(current_test)

        return tests

    def make_constant_tpk(self, df: pd.DataFrame) -> list[dict]:
        """
        Makes a QATrack+ test list for constants

        Args:
            df (pd.DataFrame): The dataframe containing the test data.

        Returns:
            list[dict]: The test list in dictionary format.
        """
        tests = []

        constant_template = self.load_tpk_template("constant")
        for index, row in df[df["type"] == "constant"].iterrows():
            # Copy the first element of the tests array, which will be a dictionary of a test
            current_test = copy.deepcopy(constant_template["objects"]["tests"][0])

            # Set key to short name
            current_test["key"][0] = row["short"]

            # Set object params
            temp_field = {
                "name": row["short"],
                "display_name": row["long"],
                "slug": row["short"],
                "description": row["description"],
                "procedure": None,
                "category": row["category"].split(","),
                "chart_visibility": False,
                "type": "constant",
                "flag_when": None,
                "hidden": True,
                "skip_without_comment": False,
                "require_comment": False,
                "display_image": False,
                "choices": None,
                "constant_value": row["value"],
                "wrap_low": None,
                "wrap_high": None,
                "calculation_procedure": "",
                "formatting": row["format"],
            }
            current_test["object"]["fields"] = temp_field

            if row["category"] is not None:
                for c in row["category"].split(","):
                    depen = copy.deepcopy(TPK_DEPEN_TEMPLATE)
                    depen["fields"]["name"] = c
                    depen["fields"]["slug"] = c.lower()
                    current_test["dependencies"].append(depen)

            tests.append(current_test)

        return tests

    def make_numeric_tpk(self, df: pd.DataFrame) -> list[dict]:
        """
        Makes a QATrack+ test list for numerics

        Args:
            df (pd.DataFrame): The dataframe containing the test data.

        Returns:
            list[dict]: The test list in dictionary format.
        """
        tests = []
        num_template = self.load_tpk_template("numeric")
        for index, row in df[df["type"] == "numeric"].iterrows():
            # Copy the first element of the tests array, which will be a dictionary of a test
            current_test = copy.deepcopy(num_template["objects"]["tests"][0])

            # Set key to short name
            current_test["key"][0] = row["short"]

            # Set object params
            temp_field = {
                "name": row["short"],
                "display_name": row["long"],
                "slug": row["short"],
                "description": row["description"],
                "procedure": None,
                "category": row["category"].split(","),
                "chart_visibility": True,
                "type": "simple",
                "flag_when": None,
                "hidden": False,
                "skip_without_comment": False,
                "require_comment": False,
                "display_image": False,
                "choices": None,
                "constant_value": None,
                "wrap_low": None,
                "wrap_high": None,
                "calculation_procedure": "",
                "formatting": row["format"],
            }
            current_test["object"]["fields"] = temp_field

            if row["category"] is not None:
                for c in row["category"].split(","):
                    depen = copy.deepcopy(TPK_DEPEN_TEMPLATE)
                    depen["fields"]["name"] = c
                    depen["fields"]["slug"] = c.lower()
                    current_test["dependencies"].append(depen)

            tests.append(current_test)

        return tests

    def make_pulldown_tpk(self, df: pd.DataFrame) -> list[dict]:
        """
        Makes a QATrack+ test list for pulldowns

        Args:
            df (pd.DataFrame): The dataframe containing the test data.

        Returns:
            list[dict]: The test list in dictionary format.
        """
        tests = []
        pd_template = self.load_tpk_template("pulldown")
        for index, row in df[df["type"] == "pulldown"].iterrows():
            # Copy the first element of the tests array, which will be a dictionary of a test
            current_test = copy.deepcopy(pd_template["objects"]["tests"][0])

            # Set key to short name
            current_test["key"][0] = row["short"]

            # Set object params
            temp_field = {
                "name": row["short"],
                "display_name": row["long"],
                "slug": row["short"],
                "description": row["description"],
                "procedure": None,
                "category": row["category"].split(","),
                "chart_visibility": True,
                "type": "multchoice",
                "flag_when": None,
                "hidden": False,
                "skip_without_comment": False,
                "require_comment": False,
                "display_image": False,
                "choices": row["format"],
                "constant_value": None,
                "wrap_low": None,
                "wrap_high": None,
                "calculation_procedure": "",
                "formatting": "",
            }
            current_test["object"]["fields"] = temp_field

            if row["category"] is not None:
                for c in row["category"].split(","):
                    depen = copy.deepcopy(TPK_DEPEN_TEMPLATE)
                    depen["fields"]["name"] = c
                    depen["fields"]["slug"] = c.lower()
                    current_test["dependencies"].append(depen)

            tests.append(current_test)

        return tests

    def process_test(
        self,
        tests,
        test,
        test_list_name,
        final_test_names,
        dependencies,
        final_tests,
        memberships,
    ):
        filtered_list = next(
            (d for d in tests if d.get("key")[0] == test["name"]), None
        )

        if not filtered_list:
            return

        dependencies.append(filtered_list["dependencies"][1])
        final_tests.append(filtered_list["object"])
        memberships.append(
            {
                "model": "qa.testlistmembership",
                "fields": {
                    "test_list": [test_list_name],
                    "test": [test["name"]],
                    "order": test["order"],
                },
            }
        )
        final_test_names.add(test["name"])

    def make_test_list(self, tests: list) -> list[dict]:
        """
        Makes a QATrack+ test list.

        Args:
            tests (list): List of all tests

        Returns:
            list: list of all testlists
        """
        tests_lists = []

        for test_list in ALL_TEST_LISTS:
            final_tests = []
            dependencies = []
            memberships = []
            testlist_extra = []
            sublist = []
            final_test_names = (
                set()
            )  # To check the existence of test names without looping through final_tests
            # Check tests array
            for test in test_list["tests"]:
                self.process_test(
                    tests,
                    test,
                    test_list["slug"],
                    final_test_names,
                    dependencies,
                    final_tests,
                    memberships,
                )

            # Check test lists array
            for t_list in test_list["test_lists"]:
                # Append for the testlist
                testlist_extra.append(
                    {
                        "model": "qa.testlist",
                        "fields": {
                            "name": t_list["list"]["long name"],
                            "slug": t_list["list"]["slug"],
                            "description": t_list["list"]["description"],
                            "javascript": "",
                            "warning_message": "Out of tolerance",
                        },
                    }
                )

                # append for the sublist
                sublist.append(
                    {
                        "model": "qa.sublist",
                        "fields": {
                            "parent": [test_list["slug"]],
                            "child": [t_list["list"]["slug"]],
                            "outline": True,
                            "order": t_list["order"],
                        },
                    }
                )

                # Check sublists for tests that haven't not been added yet and add them
                for test in t_list["list"]["tests"]:
                    if test["name"] not in final_test_names:
                        self.process_test(
                            tests,
                            test,
                            t_list["list"]["slug"],
                            final_test_names,
                            dependencies,
                            final_tests,
                            memberships,
                        )

            # Combine to make correct format
            tests_lists.append(
                {
                    "key": [test_list["slug"]],
                    "object": {
                        "model": "qa.testlist",
                        "fields": {
                            "name": test_list["long name"],
                            "slug": test_list["slug"],
                            "description": test_list["description"],
                            "javascript": "",
                            "warning_message": "Out of tolerance",
                        },
                    },
                    "dependencies": dependencies
                    + final_tests
                    + memberships
                    + testlist_extra
                    + sublist,
                }
            )

        return tests_lists

    def make_test_tpk(self, file_name: str) -> dict:
        """
        Makes a QATrack+ test list.

        Args:
            file_name (str): The file name.

        Returns:
            dict: The test list in dictionary format.
        """

        df = pd.concat(
            [
                self.read_excel_sheet("Main", file_name),
                self.read_excel_sheet("Data", file_name),
            ]
        )

        calculations_tpk = self.make_calculation_tpk(df)
        constants_tpk = self.make_constant_tpk(df)
        numerics_tpk = self.make_numeric_tpk(df)
        pulldowns_tpk = self.make_pulldown_tpk(df)

        tests = calculations_tpk + constants_tpk + numerics_tpk + pulldowns_tpk

        temp_tpk = self.load_tpk_template("calculation")
        temp_tpk["objects"]["tests"] = tests
        temp_tpk["objects"]["testlists"] = self.make_test_list(tests)
        # Adjust Meta
        temp_tpk["meta"]["version"] = "3.1.1"
        temp_tpk["meta"]["id"] = str(uuid.uuid4())
        temp_tpk["meta"]["name"] = "Testpack"
        temp_tpk["meta"]["datetime"] = datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S.%f%z"
        )
        return temp_tpk
