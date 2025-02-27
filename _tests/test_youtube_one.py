import pytest

@pytest.fixture()
def bootstrap_list():
    return list(range(10))


def mean(l):
    return sum(l) / len(l)



def test_list_mean(bootstrap_list):
    l = bootstrap_list

    assert 4.5 == mean(l)