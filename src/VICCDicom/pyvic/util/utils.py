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

import functools
import logging
import warnings
import sys
from logging import Logger
import pathos.multiprocessing as mp
import time
from inspect import getargspec


def multi_process_func(iterable_args, iterable_kwargs=None):
    if iterable_kwargs is not None:
        raise NotImplementedError(
            "iterable kwargs not yet implemented in multi_process_func decorator"
        )

    iterable_kwargs = iterable_kwargs or []

    if not (
        hasattr(iterable_args, "__iter__") and hasattr(iterable_kwargs, "__iter__")
    ):
        raise RuntimeError(
            "multi_process_decor: error, iterable_args must be list of numbered iterable arguments, "
            "iterable_kwargs must be list of names of iterable kwargs"
        )

    def mp_wrap(func):
        arg_names = getargspec(func)[0]

        if "num_cpu" in arg_names:
            raise RuntimeError(
                f'argument named "num_cpu" already exists for function {func.__name__}, '
                "can't decorate with multi_process_func"
            )

        def mp_func_wrap(*args, **kwargs):
            if not all([s in range(len(args)) for s in iterable_args]):
                raise RuntimeError(
                    f"multi_process_decor: stated iterable_args {iterable_args} not value for function prototype {arg_names}"
                )

            num_cpu = kwargs.pop("num_cpu", mp.cpu_count() - 1) or (mp.cpu_count() - 1)

            it_arg_names = [arg_names[s] for s in iterable_args]
            arg_lists = [
                args[s] if hasattr(args[s], "__iter__") else [args[s]]
                for s in iterable_args
            ]
            arg_list_sizes = [len(s) for s in arg_lists]

            if not all([s == arg_list_sizes[0] for s in arg_list_sizes]):
                arg_size_dict = {
                    it_arg_names[s]: arg_list_sizes[s] for s in range(len(it_arg_names))
                }
                raise RuntimeError(
                    f"multi_process_decor: not all mp arg lists have same size {arg_size_dict}"
                )

            total_runs = len(args[iterable_args[0]])

            if num_cpu > 1:
                print(
                    f'multi processing "{func.__name__}" with {num_cpu} cpus as {total_runs} chunks'
                )

                pool = mp.Pool(num_cpu)
                pool_out = []

                for i in range(total_runs):
                    this_arg = list(args)
                    for ia in iterable_args:
                        this_arg[ia] = args[ia][i]
                    pool_out.append(pool.apply_async(func, this_arg, kwargs))

                start = time.time()
                pool.close()
                pool.join()

                to_ret = [s.get() for s in pool_out]
                print(f"\t completed in {time.time() - start}")

                return to_ret
            else:
                print(f'multi processing "{func.__name__}" with 1 cpu')
                return [
                    func(
                        *[
                            args[ia][i] if ia in iterable_args else arg
                            for ia, arg in enumerate(args)
                        ],
                        **kwargs,
                    )
                    for i in range(total_runs)
                ]

        return mp_func_wrap

    return mp_wrap


def deprecated(func):
    """
    This is a decorator which can be used to mark functions
    as deprecated. It will result in a warning being emitted
    when the function is used.
    Source: https://wiki.python.org/moin/PythonDecoratorLibrary#Generating_Deprecation_Warnings
    :param func: Implicit function parameter.
    """

    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warnings.warn_explicit(
            "Call to deprecated function {}.".format(func.__name__),
            category=DeprecationWarning,
            filename=func.func_code.co_filename,
            lineno=func.func_code.co_firstlineno + 1,
        )
        return func(*args, **kwargs)

    return new_func


class ObjectWithID:
    def __init__(self, identifier):
        """"""
        self._id = id

    def id(self):
        return self._id


def flatten_tuple_list(tuple_list):
    return [y for x in tuple_list for y in x]


def accepts(*types):
    def check_accepts(f):
        # assert len(types) == f.func_code.co_argcount
        def new_f(*args, **kwds):
            for a, t in zip(args, types):
                assert isinstance(a, t), "arg {!r} does not match {}".format(a, t)
            return f(*args, **kwds)

        new_f.__name__ = f.__name__
        return new_f

    return check_accepts


@accepts(str)
def str_is_float(x):
    try:
        a = float(x)
    except ValueError:
        return False
    else:
        return True


@accepts(str)
def str_is_int(x):
    """
    true if string can be converted to integer without rounding
    :param x: string input
    :return: boolean
    """
    try:
        a = float(x)
        b = int(a)
    except ValueError:
        return False
    else:
        return a == b


@accepts(str)
def str_is_float(x):
    """
    true if string can be converted to float
    :param x:
    :return:
    """
    try:
        a = float(x)
    except ValueError:
        return False
    else:
        return True


@accepts(str)
def str_as_number(x):
    """
    converts string to number (int first if possible, then float, then None)
    :param x: string
    :return: int(x) if integer, float(x) if float, None if no conversion possible
    """
    if str_is_int(x):
        return int(x)
    elif str_is_float(x):
        return float(x)
    else:
        return None


def logger_initialize(
    stream=sys.stdout,
    level=logging.WARNING,
    format="%(asctime)s %(levelname)8s %(name)s - %(message)s",
    datefmt="%H:%M:%S",
):
    """
    Initialize the root logger and set the log level for all loggers with names starting with 'pydose'.
    :param stream:
    :param level:
    :param format:
    :param datefmt:
    :return:
    """
    logging.basicConfig(stream=stream, level=level, format=format, datefmt=datefmt)

    # set log level for all loggers found
    logger = logging.getLogger("root")
    for lname, l in logger.manager.loggerDict.iteritems():
        assert isinstance(lname, str)
        if isinstance(l, Logger) and lname.startswith("pydose"):
            l.setLevel(level)


def pretty_xml_string(xml_string):
    import xml.dom.minidom

    md = xml.dom.minidom.parseString(xml_string)
    return md.toprettyxml()


def is_empty_or_nonelist(obj):
    if obj is None:
        return True
    if hasattr(obj, "__iter__"):
        if len(obj) == 0:
            return True
        return all([is_empty_or_nonelist(s) for s in obj])
    else:
        return False
