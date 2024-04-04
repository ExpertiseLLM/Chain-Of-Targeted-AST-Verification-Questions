# Copyright (c) "Neo4j"
# Neo4j Sweden AB [https://neo4j.com]
#
# This file is part of Neo4j.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from typing import (
    Tuple,
    TypeVar,
)

__all__ = [
    "nano_add",
    "nano_div",
    "nano_divmod",
    "symmetric_divmod",
    "round_half_to_even",
]


def nano_add(x, y):
    """

        >>> 0.7 + 0.2
        0.8999999999999999
        >>> -0.7 + 0.2
        -0.49999999999999994
        >>> nano_add(0.7, 0.2)
        0.9
        >>> nano_add(-0.7, 0.2)
        -0.5

    :param x:
    :param y:
    :returns:
    """
    return (int(1000000000 * x) + int(1000000000 * y)) / 1000000000


def nano_div(x, y):
    """

        >>> 0.7 / 0.2
        3.4999999999999996
        >>> -0.7 / 0.2
        -3.4999999999999996
        >>> nano_div(0.7, 0.2)
        3.5
        >>> nano_div(-0.7, 0.2)
        -3.5

    :param x:
    :param y:
    :returns:
    """
    return float(1000000000 * x) / int(1000000000 * y)


def nano_divmod(x, y):
    """

        >>> divmod(0.7, 0.2)
        (3.0, 0.09999999999999992)
        >>> nano_divmod(0.7, 0.2)
        (3, 0.1)

    :param x:
    :param y:
    :returns:
    """
    number = type(x)
    nx = int(1000000000 * x)
    ny = int(1000000000 * y)
    q, r = divmod(nx, ny)
    return int(q), number(r / 1000000000)


_TDividend = TypeVar("_TDividend", int, float)


def symmetric_divmod(
        dividend: _TDividend, divisor: float
) -> Tuple[int, _TDividend]:
    number = type(dividend)
    if dividend >= 0:
        quotient, remainder = divmod(dividend, divisor)
        return int(quotient), number(remainder)
    else:
        quotient, remainder = divmod(-dividend, divisor)
        return -int(quotient), -number(remainder)

<insert generated code here>

if __name__ == "__main__":
    isT = True
    test_cases = dict()
    try:
        test_cases['test1'] = round_half_to_even(3) == 3
    except Exception as error:
        test_cases['test1'] = type(error).__name__

    try:
        test_cases['test2'] = round_half_to_even(3.2) == 3
    except Exception as error:
        test_cases['test2'] = type(error).__name__

    try:
        test_cases['test3'] = round_half_to_even(3.5) == 4
    except Exception as error:
        test_cases['test4'] = type(error).__name__

    try:
        test_cases['test4'] = round_half_to_even(3.7) == 4
    except Exception as error:
        test_cases['test5'] = type(error).__name__

    try:
        test_cases['test5'] = round_half_to_even(4) == 4
    except Exception as error:
        test_cases['test5'] = type(error).__name__

    try:
        test_cases['test6'] = round_half_to_even(4.2) == 4
    except Exception as error:
        test_cases['test6'] = type(error).__name__

    try:
        test_cases['test7'] = round_half_to_even(4.5) == 4
    except Exception as error:
        test_cases['test7'] = type(error).__name__

    try:
        test_cases['test8'] = round_half_to_even(4.7) == 5
    except Exception as error:
        test_cases['test8'] = type(error).__name__
print(test_cases)
