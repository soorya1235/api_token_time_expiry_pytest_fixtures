"""
This is the sample test file
"""
import pytest


@pytest.mark.usefixtures("get_api_token", "get_api_token_session_level")
class TestAPI:
    """ Test API Class sample"""

    # breakpoint()   Used to create break point

    def test_api_one(self):
        """This is the docstring of the function"""
        # print(TestAPI.api_token)
        print(pytest.api_token_value)

    def test_api_two(self):
        """This is the docstring of the function"""
        # print(TestAPI.api_token)
        print(pytest.api_token_value)

    def test_api_three(self):
        """This is the docstring of the function"""
        # print(TestAPI.api_token)
        print(pytest.api_token_value)
