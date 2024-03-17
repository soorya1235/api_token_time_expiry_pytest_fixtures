import pytest


@pytest.fixture(params=[(1, 2), [3, 4]], ids=["tuple", "list"])
def fixture_parameterization(request):
    return request.param


@pytest.fixture(params=["access", "slice", "assign", "len"])
def fixture02(request):
    return request.param


def test_fixture(fixture_parameterization):
    print(fixture_parameterization)


def test_fixture_multiple(fixture_parameterization, fixture02):
    if fixture02 == "access":
        assert fixture_parameterization[0]
    elif fixture02 == "slice":
        assert (fixture_parameterization[::-1])
    elif fixture02 == "assign":
        fixture_parameterization[0] = 99
        assert True
    elif fixture02 == "len":
        assert len(fixture02)
