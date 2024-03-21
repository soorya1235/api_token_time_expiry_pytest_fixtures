import pytest


# Fixture called at module level
@pytest.fixture(scope="module")
def module_level_fixture():
    return "Module Level Fixture Value"


# Another fixture that captures the value of the module level fixture
@pytest.fixture(scope="module")
def captured_fixture(module_level_fixture):
    captured_value = module_level_fixture
    return captured_value


# Test function that uses the captured fixture
def test_captured_fixture(captured_fixture):
    assert captured_fixture == "Module Level Fixture Value"
