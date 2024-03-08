import pytest


@pytest.mark.usefixtures("get_api_token", "check_api_token_status")
class TestAPI:
    api_token = None
    api_token_status = None

    def test_pre_setup(self, get_api_token, check_api_token_status):
        print("Setup Class Called")
        TestAPI.api_token = get_api_token
        TestAPI.check_api_token_status = check_api_token_status
        print(f"API Token: {TestAPI.api_token}")
        print(f"API Token Status: {TestAPI.api_token_status}")

    def setup_class(cls):
        print("It is the first method called before executing any test in the class")

    def test_api1(self):
        print("API 1 testing")
        print(f"API Token status is {TestAPI.api_token_status}")

    def test_api2(self):
        print("API 2 testing")
        print(f"API Token status is {TestAPI.api_token_status}")

    def test_api3(self, check_api_token_status):
        print("API 3 testing")
        print(f"API Token status is {TestAPI.api_token_status}")

    def teardown_class(cls):
        print("It is the Last method called executing any test in the class")
