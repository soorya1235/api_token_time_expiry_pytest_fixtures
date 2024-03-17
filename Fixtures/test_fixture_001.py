import pytest


@pytest.fixture()
def setup_list():
    print("\n in Fixtures..\n")
    city = ["New york", "London", "Riyadh", "Singapore", "Mumbai"]
    return city


def test_getitem(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == "New york"
    assert setup_list[::2] == ["New york", "Riyadh", "Mumbai"]


def my_reverse(lst):
    lst.reverse()
    return lst


def test_reverse_list(setup_list):
    assert setup_list[::-2] == ["Mumbai", "Riyadh", "New York"]
    assert setup_list[::-1] == my_reverse(setup_list)
