""""
Example of conftest file
If you see below example we have defined the global variables in pytest_configure,
and it can be accessed using pytest .

"""
import pytest


def test_display_global_variables():
    print(pytest.weekdays1)
    print(pytest.weekdays2)
