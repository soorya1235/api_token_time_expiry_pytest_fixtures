import pytest

mon = ["jan", "feb", "march"]


def test_fixture_scope_display(setup04):
    assert 1 == 1
    assert mon == ["jan", "feb", "march", "April"]


def test_fixture_as_factories(setup05):
    assert type(setup05("list")) == list

