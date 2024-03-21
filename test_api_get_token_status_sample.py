import pytest


class TestAPI:
    api_token = None
    api_token_status = None

    def test_pre_setup(self, get_api_token, check_api_token_status):
        print("Setup Class Called")
        TestAPI.api_token = get_api_token
        TestAPI.api_token_status = check_api_token_status
        # breakpoint()

    def test_api1(self):
        print("API 1 testing")
        print(f"API Token status is {TestAPI.api_token_status}")

    def test_api2(self):
        print("API 2 testing")
        print(f"API Token status is {TestAPI.api_token_status}")

    def test_api3(self, check_api_token_status):
        print("API 3 testing")
        print(f"API Token status is {TestAPI.api_token_status}")
