import json
import os
import pytest


# Sample function to test JSON payloads
def process_json(json_data):
    # Your JSON processing logic goes here
    return len(json_data)


# Define a fixture to load JSON data from files
@pytest.fixture
def json_payload(request):
    # Get the name of the JSON file associated with the test case
    test_file_name = request.param
    # Load JSON data from the file
    file_path = os.path.join(os.path.dirname(__file__), "json_data", test_file_name)
    with open(file_path, "r") as file:
        return json.load(file)


# Define test cases with file names of JSON payloads
@pytest.mark.parametrize("json_payload, expected_length", [
    ("test_data_1.json", 2),  # Provide the file name containing JSON payload
    ("test_data_2.json", 3),  # Provide another file name
    # Add more file names as needed
], indirect=["json_payload"])  # Indicate that the json_payload parameter is a fixture
def test_process_json(json_payload, expected_length):
    result = process_json(json_payload)
    assert result == expected_length
