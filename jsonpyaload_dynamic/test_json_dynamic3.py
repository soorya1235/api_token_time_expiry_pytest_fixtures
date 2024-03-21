import json
import os
import pytest


# Define a fixture to load JSON data from files
@pytest.fixture
def json_data(request):
    # Get the name of the JSON file associated with the test case
    breakpoint()
    test_file_name = request.param
    # Load JSON data from the file
    file_path = os.path.join(os.path.dirname(__file__), "json_data", test_file_name)
    with open(file_path, "r") as file:
        return json.load(file)


# Example test function using the json_data fixture
@pytest.mark.parametrize("json_data", ["test_data_1.json", "test_data_2.json"], indirect=True)
def test_json_data_length(json_data):
    assert isinstance(json_data, dict)  # Assuming JSON data is expected to be a dictionary
    assert len(json_data) > 0  # Example assertion to ensure data is loaded successfully
    # Additional test logic using the loaded JSON data
    # For example, you can test specific keys/values in the JSON data


"""
Certainly! The @pytest.mark.parametrize decorator is a powerful feature of pytest that allows you to run the same test function with different input values. This is particularly useful when you want to test multiple scenarios without duplicating test code. Let's break down the statement @pytest.mark.parametrize("json_data", ["test_data_1.json", "test_data_2.json"], indirect=True):

@pytest.mark.parametrize: This is the decorator provided by pytest for parameterized testing. It lets you specify the parameters for your test function and the values you want to test.

"json_data": This is the name of the parameter that you want to parametrize. In this case, it refers to the json_data fixture we defined earlier. The test function will receive the loaded JSON data through this parameter.

["test_data_1.json", "test_data_2.json"]: This is an iterable containing the values that you want to use for the parameterized test. Each item in the iterable corresponds to one test case. In this case, we're providing a list of JSON file names (test_data_1.json and test_data_2.json) that contain the JSON data to be loaded and tested.

indirect=True: This parameter tells pytest that the values provided to the @pytest.mark.parametrize decorator are the names of fixtures. By setting indirect=True, we're telling pytest to treat these values as fixture names and invoke them to obtain the actual test parameters. In our case, the json_data fixture is invoked for each value provided in the list, and the loaded JSON data is passed to the test function.

So, when you use @pytest.mark.parametrize("json_data", ["test_data_1.json", "test_data_2.json"], indirect=True), pytest will run the test function twice: once with the JSON data loaded from test_data_1.json, and then again with the JSON data loaded from test_data_2.json. This allows you to write a single test function that can be reused with different JSON data, promoting code reusability and maintainability.
"""