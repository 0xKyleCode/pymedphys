"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.

Authors: Clay Lindsay and Mark Baker
"""

import abc
import logging
import os
import numpy as np
import csv
import fnmatch
import pickle as picklerlib
from pandas import DataFrame, read_pickle

_logger = logging.getLogger(__name__)


class LoadableObj:
    """
    A serializable object that can be saved to and loaded from a file using Python's pickle module.
    """

    def save(self, path: str) -> None:
        """
        Save the current instance of the object to the specified file path using pickle.

        Args:
        - path (str): The file path to which the object should be saved.

        Returns:
        - None
        """
        _logger.info("Saving %s file to %s", self.__class__.__name__, path)

        with open(path, "wb") as fh:
            picklerlib.dump(self, fh, protocol=picklerlib.HIGHEST_PROTOCOL)

    @classmethod
    def load(cls, path_or_obj: str) -> "LoadableObj":
        """
        Load an object from a file path or return the given object if it's an instance of the current class.

        Args:
        - path_or_obj (str): Either a file path to load the object from or an already existing object.

        Returns:
        - LoadableObj: The loaded object or the passed-in object if it's already an instance of the current class.
        """
        if isinstance(path_or_obj, cls):
            return path_or_obj

        _logger.info("Loading %s file from %s", cls.__name__, path_or_obj)

        with open(path_or_obj, "rb") as fh:
            ret = picklerlib.load(fh)

        if not isinstance(ret, cls):
            raise ValueError(f"Loaded object is not an instance of {cls.__name__}")

        return ret

    @classmethod
    def load_if_exists(cls, path: str, *args, **kwargs) -> "LoadableObj":
        """
        Load an object from the given file path if it exists, otherwise create a new object and save it.

        Args:
        - path (str): File path to load the object from.
        - *args: Positional arguments to pass to the class constructor if creating a new object.
        - **kwargs: Keyword arguments to pass to the class constructor if creating a new object.

        Returns:
        - LoadableObj: The loaded or newly created object.
        """
        try:
            return cls.load(path)
        except Exception as e:
            _logger.warning(
                "Error loading %s file (%s), building from scratch", cls.__name__, e
            )
            obj = cls(*args, **kwargs)
            obj.save(path)

            if not isinstance(obj, cls):
                raise ValueError(f"Created object is not an instance of {cls.__name__}")

            return obj

    @classmethod
    def from_pickle(cls, path: str) -> "LoadableObj":
        """
        Load an object from a pickle file.

        Args:
        - path (str): File path to load the object from.

        Returns:
        - LoadableObj: The loaded object.
        """
        with open(path, "rb") as f:
            ret = picklerlib.load(f)

        return ret

    @classmethod
    def to_pickle(cls, obj: "LoadableObj", path: str) -> None:
        """
        Save an object to a pickle file.

        Args:
        - obj (LoadableObj): Object to be saved.
        - path (str): File path to save the object to.

        Returns:
        - None
        """
        with open(path, "wb") as outFile:
            picklerlib.dump(obj, outFile, protocol=picklerlib.HIGHEST_PROTOCOL)


class FileGrouper:
    """
    File grouping abstract class.  Groups files by common grouping regex (pattern with one match)
    """

    import abc

    __metaclass__ = abc.ABCMeta

    NO_REPEAT_FILES = False

    @abc.abstractmethod
    def get_file_grouping_string(self, file_path):
        """string to match for file grouping"""
        pass

    @abc.abstractmethod
    def is_filetype(self, file_path):
        """returns true if file is desired type"""
        pass

    def parse_metadata(self):
        dict = {s: {} for s in self.grouping_string_set}
        return dict

    def __init__(self, file_list):
        """
        :param file_list: list of file paths to group
        """
        import re

        unique_file_groupings = {
            self.get_file_grouping_string(f) for f in file_list if self.is_filetype(f)
        }

        self.file_groups = sorted(
            [
                sorted(
                    [
                        f
                        for f in file_list
                        if self.is_filetype(f)
                        and re.match(
                            "%s" % re.escape(s), self.get_file_grouping_string(f)
                        )
                        is not None
                    ]
                )
                for s in unique_file_groupings
            ]
        )

        if self.NO_REPEAT_FILES:
            for f in file_list:
                in_groups = [g for g in self.file_groups if f in g]
                if len(in_groups) > 1:
                    glen = [len(self.get_group_string(g)) for g in in_groups]
                    from numpy import argmax

                    # determine longest group name
                    maxlen = argmax(glen)
                    del in_groups[maxlen]
                    # remove f from all other groups
                    for flist in self.file_groups:
                        if flist in in_groups:
                            flist.remove(f)

        self.meta_data_dict = self.parse_metadata()

    @classmethod
    def from_unix_wildcard(cls, unix_wc, recursive=False):
        """
        :param unix_wc: unix wildcard to match input file list
        :param recursive: if true, recurse into directory structure
        :return:
        """
        return cls(list_files_by_wildcard(unix_wc, recursive=recursive))

    @classmethod
    def from_directory(cls, path, recursive=False):
        from os.path import join

        print("Grouping files from dir: %s" % join(path, cls.STANDARD_FORMAT_UNIX_WC))
        return cls.from_unix_wildcard(
            join(path, cls.STANDARD_FORMAT_UNIX_WC), recursive=recursive
        )

    def __iter__(self):
        yield from self.file_groups

    def __getitem__(self, item):
        return self.file_groups[item]

    class InvalidGroupingRegexException(Exception):
        pass

    @property
    def grouping_string_set(self):
        return [self.get_file_grouping_string(s[0]) for s in self.file_groups]

    def __str__(self):
        toRet = ""

        for fg in self.file_groups:
            name = self.get_file_grouping_string(fg[0])
            toRet += "{} : {}\n\t{}\n".format(name, len(fg), self.get_metadata(fg))
        return toRet

    def get_metadata(self, file_group):
        if file_group in self.file_groups:
            return self.meta_data_dict[self.get_file_grouping_string(file_group[0])]
        elif isinstance(file_group, str):
            return self.meta_data_dict[self.get_file_grouping_string(file_group)]

    def get_group_string(self, file_group):
        if file_group in self.file_groups:
            return self.get_file_grouping_string(file_group[0])
        else:
            raise IndexError("group %s not in file grouper" % file_group)


class DataFrameableCollectable(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def to_dataframe_dict(self):
        pass

    @abc.abstractmethod
    def from_dataframe_dict(self):
        pass

    @classmethod
    def to_dataframe(cls, list_of_collectable_obj, meta_data=None):
        assert all([isinstance(s, cls) for s in list_of_collectable_obj])
        if meta_data is None:
            meta_data = []

        df = DataFrame([s.to_dataframe_dict() for s in list_of_collectable_obj])
        df._metadata = meta_data
        return df

    @classmethod
    def from_dataframe(cls, df_file):
        if isinstance(df_file, DataFrame):
            df = df_file
        else:
            try:
                df = read_pickle(df_file)
            except ValueError:
                with open(df_file, "rb") as f:
                    df = picklerlib.load(f)
            except OSError:
                try:
                    df = read_pickle(df_file + ".pkl")
                except OSError:
                    raise OSError(f"cannot find file {df_file} or {df_file}.pkl")

        to_ret = [cls.from_dataframe_dict(r[1][0]) for r in df.iterrows()]

        return to_ret, df._metadata

    def save(self, file_name):
        d = self.to_dataframe([self])
        d.to_pickle(file_name)

    @classmethod
    def load(cls, file_name):
        df = cls.from_dataframe(file_name)[0]

        if len(df) != 1:
            raise NotImplementedError(
                "load method only used for singleton dataframe storage"
            )

        return df[0]


def csv_to_tuple(
    fName: str, rowList: list, delChar: str = ",", commentChar: str = "#"
) -> tuple:
    """
    Convert specific rows of a CSV file to a tuple of numpy arrays.

    Args:
    - fName (str): Input file path.
    - rowList (list): List of row numbers to be extracted.
    - delChar (str, optional): Delimiter character. Defaults to ",".
    - commentChar (str, optional): Comment character. Lines starting with this character will be ignored. Defaults to "#".

    Returns:
    - tuple: A tuple containing numpy arrays corresponding to the rows specified in `rowList`.
    """

    # Expand any environment variables in the file name
    fName = os.path.expandvars(fName)

    # Initialize a list of empty lists to hold row data
    retList = [[] for _ in range(len(rowList))]

    with open(fName) as csvFile:
        for line in csvFile:
            # Split the line by the delimiter
            row = line.split(delChar)

            # Skip empty rows or commented rows
            if not row or row[0].strip().startswith(commentChar):
                continue

            # Extract data from the desired columns and append to retList
            for i, rowIndex in enumerate(rowList):
                try:
                    retList[i].append(float(row[rowIndex].strip()))
                except (IndexError, ValueError):
                    # Handle cases where the row does not have enough columns or the data is not a number
                    _logger.warning(
                        f"Skipping line: {line.strip()} due to missing or invalid data."
                    )
                    break

    # Convert lists to numpy arrays
    retList = [np.array(data) for data in retList]

    return tuple(retList)


def array_tuple_to_csv(
    fname: str,
    arrayTuple: tuple,
    str_formats: list = None,
    delim: str = ",",
    commentChar: str = "#",
    headerString: str = None,
) -> None:
    """
    Write a tuple of arrays to a CSV file.

    Args:
    - fname (str): Name of the file to write to.
    - arrayTuple (tuple): A tuple of arrays, each representing a column in the CSV.
    - str_formats (list, optional): A list of string format specifiers for each array.
                                    Must be of same length as arrayTuple if provided.
    - delim (str, optional): Delimiter to use in the CSV. Defaults to ",".
    - commentChar (str, optional): Comment character. Defaults to "#".
    - headerString (str, optional): Optional header string to be written at the start of the CSV.

    Returns:
    - None
    """

    print(f"writing csv {fname}")

    if str_formats is not None:
        assert len(str_formats) == len(
            arrayTuple
        ), "str_formats length must match arrayTuple length"

    with open(
        fname, "w", newline=""
    ) as f:  # Using 'w' and added 'newline' for better cross-platform support
        writer = csv.writer(f, delimiter=delim)

        if headerString is not None:
            f.write(f"{commentChar} {headerString}\n")

        for i in range(len(arrayTuple[0])):
            row = []
            for j, column in enumerate(arrayTuple):
                formatted_value = (
                    str_formats[j] % column[i] if str_formats else column[i]
                )
                row.append(formatted_value)
            writer.writerow(row)


def list_files_by_wildcard(
    pattern: str, recursive: bool = False, do_sort: bool = True
) -> list:
    """
    List files matching a given UNIX wildcard pattern.

    Args:
    - pattern (str): UNIX wildcard pattern.
    - recursive (bool, optional): If true, search recursively into directories. Defaults to False.
    - do_sort (bool, optional): If true, sort the resulting list of files. Defaults to True.

    Returns:
    - list: List of files matching the given pattern.
    """

    _dirname, wc = os.path.split(pattern)

    if recursive:
        matched_files = [
            os.path.join(dirPath, f)
            for dirPath, _, filenames in os.walk(_dirname)
            for f in filenames
            if fnmatch.fnmatch(os.path.join(dirPath, f), wc)
        ]
    else:
        matched_files = [
            os.path.join(_dirname, f)
            for f in os.listdir(_dirname)
            if fnmatch.fnmatch(f, wc)
        ]

    return sorted(matched_files) if do_sort else matched_files
