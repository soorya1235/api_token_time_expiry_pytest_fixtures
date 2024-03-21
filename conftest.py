""""
Example of Conftest file
If we define the variables in the pytest_configure,those will be accessible across all the test files.
"""
import smtplib
import datetime
import pytest


@pytest.fixture(scope="session")
def get_api_token_session_level():
    print("Called Before the Session")
    # Assigning the API token value to the pytest variable
    pytest.api_token_value = "123123123"
    yield "token_value"
    print("Called after the Session")


@pytest.fixture(scope="class")
def get_api_token():
    print("called before the class")
    # Checking if the token is not expired
    # pytest.api_token_value = "123123123"
    yield
    print("Called after the class")


def pytest_configure():
    pytest.weekdays1 = ["mon", "tue", "wed"]
    pytest.weekdays2 = ["fri", "sat", "sun"]
    pytest.api_token_value = "tobefilled"
    current_time = datetime.datetime.now()
    current_hour = current_time.strftime("%H")  # 24-hour format
    current_minute = current_time.strftime("%M")
    current_second = current_time.strftime("%S")
    pytest.current_time = current_hour + current_minute + current_second


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


@pytest.fixture(scope="class")
def check_api_token_status():
    print("Calling Before the Class")
    print("Checking API Token Status and Returning Value")
    print(f"Printing the Token Status")
    yield True
    print("Calling After the End of Class")


"""
Function Level Fixture
"""

# @pytest.fixture(scope='function', autouse=True)
# def smtp_connection() -> smtplib.SMTP:
#     """
#     A fixture to create an SMTP connection.
#
#     Returns:
#         An SMTP connection
#     """
#     print("SMTP Connection fixture start")
#     yield smtplib.SMTP("smtp.gmail.com", 587, timeout=60)
#     print("SMTP Connection Tear Down")
#
#
# """
# Module Level Fixture
# """
#
#
# @pytest.fixture(scope='module', autouse=True)
# def smtp_connection_module() -> smtplib.SMTP:
#     """
#     A fixture to create an SMTP connection.
#
#     Returns:
#         An SMTP connection
#     """
#     print("SMTP Connection fixture start")
#     yield smtplib.SMTP("smtp.gmail.com", 587, timeout=60)
#     print("SMTP Connection Tear Down")
