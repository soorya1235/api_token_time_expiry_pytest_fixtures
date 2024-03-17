"""
Example of tear down fixture
"""
import pytest
import os

filename = "file1.txt"


@pytest.fixture()
def setup_file():
    f = open(filename, 'w')
    f.write("Pytest is good")
    f.close()
    f = open(filename, 'r+')
    yield f
    f.close()
    os.remove(filename)


def test_file(setup_file):
    assert (setup_file.readline()) == "Pytest is good"
