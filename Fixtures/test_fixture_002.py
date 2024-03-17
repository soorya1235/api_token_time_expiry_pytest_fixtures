"""
We have seen how to use fixtures by passing it to a function
we have seen how to use fixtures by calling it as a decorator
"""
import pytest


@pytest.fixture()
def setup_list():
    print("\n in Fixtures..\n")
    city = ["New york", "London", "Riyadh", "Singapore", "Mumbai"]
    return city


@pytest.mark.xfail(reason="known issue :use fixtures cannot use fixture value")
@pytest.mark.usefixtures("setup_list")
def test_use_fixture_demo():
    assert 1 == 1
    print(setup_list[0])
    print(setup_list[2])
