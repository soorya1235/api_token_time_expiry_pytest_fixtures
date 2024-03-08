import pytest
import smtplib


@pytest.fixture(scope="session")
def get_api_token():
    print("Called Before the Session")
    yield "token_value"
    print("Called after the Session")


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


@pytest.fixture(scope='function', autouse=True)
def smtp_connection() -> smtplib.SMTP:
    """
    A fixture to create an SMTP connection.

    Returns:
        An SMTP connection
    """
    print("SMTP Connection fixture start")
    yield smtplib.SMTP("smtp.gmail.com", 587, timeout=60)
    print("SMTP Connection Tear Down")


"""
Module Level Fixture
"""


@pytest.fixture(scope='module', autouse=True)
def smtp_connection_module() -> smtplib.SMTP:
    """
    A fixture to create an SMTP connection.

    Returns:
        An SMTP connection
    """
    print("SMTP Connection fixture start")
    yield smtplib.SMTP("smtp.gmail.com", 587, timeout=60)
    print("SMTP Connection Tear Down")
