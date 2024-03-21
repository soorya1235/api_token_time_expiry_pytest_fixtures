import pytest

# Sample function to test JSON payloads
def process_json(json_data):
    # Your JSON processing logic goes here
    return len(json_data)

# Define test cases with different JSON payloads
@pytest.mark.parametrize("json_payload, expected_length", [
    ({"key1": "value1", "key2": "value2"}, 2),  # Simple JSON with two key-value pairs
    ({"key1": {"nested_key": "nested_value"}}, 1),  # JSON with nested structure
    ({"array": [1, 2, 3]}, 1),  # JSON with an array
    ({"key1": "value1", "key2": "value2", "key3": "value3"}, 3),  # JSON with three key-value pairs
    # Add more test cases as needed
])
def test_process_json(json_payload, expected_length):
    result = process_json(json_payload)
    assert result == expected_length
