from pprint import pprint
from typing import Callable, Collection, List, Mapping, Optional, Tuple, TypeVar

from test_project_python.package_builder import (
    verify_instance_is_from_type,
)


InputArguments                         = TypeVar('InputArguments') 


def main():
    test_function(data_verify_instance_is_from_type)


def test_function(function_data: Tuple[Callable, Tuple[InputArguments, str]]):
    function, test_cases = function_data
    successes           = 0
    failures            = 0
    test_case_successes = []
    test_case_failures  = []
    for input_arguments, description in test_cases:
        try:
            verify_instance_is_from_type(*input_arguments)
        except TypeError as e:
            failures += 1
            test_case_failures.append((input_arguments, description))
        else:
            successes += 1
            test_case_successes.append((input_arguments, description))
    print(f'{successes} test cases passed, {failures} test cases failed for the `verify_instance_is_from_type` function!')
    print('Passing test cases:')
    for input_arguments, description in test_case_successes:
        print(format_result(function, input_arguments, description))
    print('Failing test cases:')
    for input_arguments, description in test_case_failures:
        print(format_result(function, input_arguments, description))
    return (successes, failures, test_case_successes, test_case_failures)


def format_result(function, input_arguments, description):
    return f'{description}: {function.__name__}{input_arguments}'

none_type  = type(None)
data_verify_instance_is_from_single_acceptable_type = [
    ('s',   str,        'str_val'),
    (1,     int,        'int_val'),
    (1.0,   float,      'float_val'),
    ([],    Collection, 'list_val'),
    ((),    Collection, 'tuple_val'),
    ({},    Collection, 'dict_val'),
    (set(), Collection, 'set_val'),
    ('s',   Collection, 'str_val'),
    ({},    Mapping,    'dict_val'),
]

data_verify_instance_is_from_type = [
    verify_instance_is_from_type,
    (
        *(
            ((obj, acceptable_type, variable_name), f'{variable_name:<9} input with `{str(acceptable_type):<17}` as only acceptable type')
            for obj, acceptable_type, variable_name in data_verify_instance_is_from_single_acceptable_type
        ),
        (('s',   (str, none_type),       'str_var'),      '`str`   input with `str` and `None`        as acceptable types'),
        ((1,     (int, none_type),        'int_var'),     '`int`   input with `int` and `None`        as acceptable types'),
        ((1.0,   (float, none_type),      'float_var'),   '`float` input with `float` and `None`      as acceptable types'),
        (([],    (Collection, none_type), 'list_var'),    '`list`  input with `Collection` and `None` as acceptable types'),
        (((),    (Collection, none_type), 'tuple_var'),   '`tuple` input with `Collection` and `None` as acceptable types'),
        (({},    (Collection, none_type), 'dict_var'),    '`dict`  input with `Collection` and `None` as acceptable types'),
        ((set(), (Collection, none_type), 'set_var'),     '`set`   input with `Collection` and `None` as acceptable types'),
        (('s',   (Collection, none_type), 'str_var'),     '`str`   input with `Collection` and `None` as acceptable types'),
        (({},    (Mapping, none_type) ,   'dict_var'),    '`dict`  input with `Mapping` and `None`    as acceptable types'),
    )
]


if __name__ == '__main__':
    main()
