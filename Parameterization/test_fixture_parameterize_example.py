"""
This test will check for each of the value mentioned in the test_input and will check
whether it is less than or equal test_input data
"""
import math

import pytest


@pytest.mark.parametrize("test_input", [10, 20, 30, 40])
def test_data(test_input):
    assert test_input < 50


@pytest.mark.parametrize("inp,out", [(2, 4), (3, 27), (4, 256)])
def test_param2(inp, out):
    assert (inp ** inp) == out


data = [
    ([2, 3, 4], 'sum', 9),
    ([2, 3, 4], 'prod', 24),
]


@pytest.mark.parametrize("a,b,c", data)
def test_param03(a, b, c):
    if b == 'sum':
        assert sum(a) == c
    elif b == 'prod':
        assert math.prod(a) == c
