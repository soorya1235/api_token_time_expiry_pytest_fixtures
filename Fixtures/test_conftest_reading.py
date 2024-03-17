"""
If we want to know which fixtures are called as part of the test we need to give the option
pytest -v -k test_conftest_reading.py --setup-show (setup-show is used to show the fixtures
which are called as part of the test functions)

"""
import pytest


def test_delitem(setup01):
    del setup01[-1]
    print(setup01)
    assert setup01 == pytest.weekdays1


def test_remove_item(setup02):
    print(setup02)
    setup02.remove("thur")
    assert setup02 == pytest.weekdays2
