""""
Example of Conftest file
If we define the variables in the pytest_configure,those will be accessible
across all the test files.
"""
import pytest


def pytest_configure():
    pytest.weekdays1 = ["mon", "tue", "wed"]
    pytest.weekdays2 = ["fri", "sat", "sun"]


@pytest.fixture(scope="module")
def setup01():
    print("\n Fixture setup01 Opening")
    wk = pytest.weekdays1.copy()
    wk.append("thur")
    yield wk
    print("\n Fixture setup01 Closing")


@pytest.fixture()
def setup02():
    wk2 = pytest.weekdays2.copy()
    wk2.insert(0, "thur")
    yield wk2


@pytest.fixture()
def setup04(request):
    mon = getattr(request.module, "mon")
    print("\n Fixture Setup04 \n")
    print("\n Fixture Scope: " + str(request.scope))
    print("\n Function Name: " + str(request.function.__name__))
    print("\n Module Name: " + str(request.module.__name__))
    mon.append("April")
    yield mon

"""
Below are factories of fixtures, which will call function and based on the function call
we are returning the data
"""
@pytest.fixture()
def setup05():
    def get_structure(name):
        if name == 'list':
            return [1, 2, 3]
        if name == 'tuple':
            return (1, 2, 3)
    return get_structure
