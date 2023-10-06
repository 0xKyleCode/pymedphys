import os
import json
import pandas as pd
import uuid
import copy
from openpyxl import load_workbook
from collections import defaultdict
from datetime import datetime, timezone
import copy

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

        testpack_dict["objects"]["testlistcycles"] = [
            json.dumps(s) for s in testpack_dict["objects"]["testlistcycles"]
        ]
        with open(outfile, "w") as f:
            json.dump(testpack_dict, f, indent=4)

    def find_file_recursive(self, directory, target_filename):
        for root, dirs, files in os.walk(directory):
            if target_filename in files:
                return os.path.join(root, target_filename)

        return None

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

            # Get location
            directory_path = os.path.join(
                os.getcwd(),
                "src",
                "QAtrack",
                "src",
                "qa_formulas",
            )
            target_filename = f"{row['short']}.py"
            python_file_path = self.find_file_recursive(directory_path, target_filename)
            # Read the content of the Python file
            if python_file_path is None:
                raise FileNotFoundError(
                    f"File {target_filename} not found in {directory_path}"
                )
            with open(python_file_path) as python_file:
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
        order,
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
                    "order": order,
                },
            }
        )
        final_test_names.add(test["name"])

    def process_testlist(
        self,
        name,
        test_list,
        final_test_names,
        testlist_extra,
        sublist,
        dependencies,
        final_tests,
        memberships,
        tests,
    ):
        for index, t_list in enumerate(test_list):
            t_list_updated = self.transfer_test_list_to_test(t_list)
            t_list_updated["name"]["tests"] = self.flatten_list(
                t_list_updated["name"]["tests"]
            )

            testlist_extra.append(
                {
                    "model": "qa.testlist",
                    "fields": {
                        "name": t_list_updated["name"]["long name"],
                        "slug": t_list_updated["name"]["slug"],
                        "description": t_list_updated["name"]["description"],
                        "javascript": "",
                        "warning_message": "Out of tolerance",
                    },
                }
            )

            sublist.append(
                {
                    "model": "qa.sublist",
                    "fields": {
                        "parent": [name],
                        "child": [t_list_updated["name"]["slug"]],
                        "outline": True,
                        "order": index,
                    },
                }
            )
            for test_index, test in enumerate(t_list_updated["name"]["tests"]):
                if test["name"] not in final_test_names:
                    self.process_test(
                        tests,
                        test,
                        t_list_updated["name"]["slug"],
                        final_test_names,
                        dependencies,
                        final_tests,
                        memberships,
                        test_index,
                    )

    def transfer_test_list_to_test(self, test_list: dict) -> list[dict]:
        """
        Condenses a test list into a list of tests.

        Args:
            test_list (dict): The test list.
        Returns:
            list[dict]: The list of tests.
        """
        new_test_list = copy.deepcopy(test_list)
        for tests in new_test_list["name"]["test_lists"]:
            # Recursively make sure all tests get added
            updated_test_list = self.transfer_test_list_to_test(tests)
            new_test_list["name"]["tests"].insert(
                tests["order"], updated_test_list["name"]["tests"]
            )

        return new_test_list

    def flatten_list(self, nested_list: list) -> list:
        """
        Flattens a nested list.

        Args:
            nested_list (list): List to be flatten

        Returns:
            list: Flattened list
        """
        return [
            item
            for sublist in nested_list
            for item in (
                self.flatten_list(sublist) if isinstance(sublist, list) else [sublist]
            )
        ]

    def make_test_list(
        self, tests: list, ALL_TEST_LISTS: list[dict]
    ) -> (list[dict], list[dict]):
        """
        Makes a QATrack+ test list.

        Args:
            tests (list): List of all tests

        Returns:
            list: list of all testlists
        """
        tests_lists = []
        test_list_cycles = []
        for test_list in ALL_TEST_LISTS:
            final_tests = []
            dependencies = []
            memberships = []
            testlist_extra = []
            sublist = []
            cycle = []
            final_test_names = set()

            # Check tests array
            for index, test in enumerate(test_list["tests"]):
                self.process_test(
                    tests,
                    test,
                    test_list["slug"],
                    final_test_names,
                    dependencies,
                    final_tests,
                    memberships,
                    index,
                )

            self.process_testlist(
                test_list["slug"],
                test_list["sublists"],
                final_test_names,
                testlist_extra,
                sublist,
                dependencies,
                final_tests,
                memberships,
                tests,
            )

            # Check cycle lists array
            for cycle_index, cycle_list in enumerate(test_list["cycle"]):
                cycle.append(
                    {
                        "model": "qa.testlistcyclemembership",
                        "fields": {
                            "test_list": [cycle_list["name"]["slug"]],
                            "cycle": [test_list["slug"]],
                            "order": cycle_index,
                        },
                    }
                )

                self.process_testlist(
                    cycle_list["name"]["slug"],
                    cycle_list["name"]["sublists"],
                    final_test_names,
                    testlist_extra,
                    sublist,
                    dependencies,
                    final_tests,
                    memberships,
                    tests,
                )

            if len(test_list["cycle"]) > 0:
                # Combine to make correct format
                test_list_cycles.append(
                    {
                        "key": [test_list["slug"]],
                        "object": {
                            "model": "qa.testlistcycle",
                            "fields": {
                                "name": test_list["long name"],
                                "slug": test_list["slug"],
                                "description": test_list["description"],
                                "javascript": "",
                                "drop_down_label": "Choose Month",
                                "day_option_text": "day",
                            },
                        },
                        "dependencies": dependencies
                        + final_tests
                        + memberships
                        + testlist_extra
                        + sublist
                        + cycle,
                    }
                )
            else:
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

        return tests_lists, test_list_cycles

    def make_test_tpk(
        self, definitions: pd.DataFrame, ALL_TEST_LISTS: list[dict]
    ) -> dict:
        """
        Makes a QATrack+ test list.

        Args:
            file_name (str): The file name.

        Returns:
            dict: The test list in dictionary format.
        """

        df = definitions

        calculations_tpk = self.make_calculation_tpk(df)
        constants_tpk = self.make_constant_tpk(df)
        numerics_tpk = self.make_numeric_tpk(df)
        pulldowns_tpk = self.make_pulldown_tpk(df)

        tests = calculations_tpk + constants_tpk + numerics_tpk + pulldowns_tpk

        temp_tpk = self.load_tpk_template("calculation")
        temp_tpk["objects"]["tests"] = tests
        test_lists, test_list_cycles = self.make_test_list(tests, ALL_TEST_LISTS)
        temp_tpk["objects"]["testlists"] = test_lists
        temp_tpk["objects"]["testlistcycles"] = test_list_cycles

        # Adjust Meta
        temp_tpk["meta"]["version"] = "3.1.1"
        temp_tpk["meta"]["id"] = str(uuid.uuid4())
        temp_tpk["meta"]["name"] = "Testpack"
        temp_tpk["meta"]["datetime"] = datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S.%f%z"
        )
        return temp_tpk
