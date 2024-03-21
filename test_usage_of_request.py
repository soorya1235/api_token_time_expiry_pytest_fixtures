import pytest


# Fixture providing data to test functions
@pytest.fixture
def data_for_tests(request):
    # Accessing the name of the test function requesting the data
    test_name = request.node.name
    if "test_addition" in test_name:
        return (2, 3)  # Example data for the test_addition function
    elif "test_subtraction" in test_name:
        return (5, 3)  # Example data for the test_subtraction function


# Test function for addition
def test_addition(data_for_tests):
    a, b = data_for_tests
    assert a + b == 5


# Test function for subtraction
def test_subtraction(data_for_tests):
    a, b = data_for_tests
    assert a - b == 2
