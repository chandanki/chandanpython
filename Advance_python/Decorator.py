import pytest


@pytest.fixture
def sample():
    return {"username": "admin", "pass": "ad12"}


def test(sample):
    assert sample["username"] == "admin"
    assert sample['pass']== 'd12'