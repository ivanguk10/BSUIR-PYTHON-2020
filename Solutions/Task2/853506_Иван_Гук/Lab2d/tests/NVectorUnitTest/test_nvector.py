import pytest
from src.NVector import NVector, NVectorError


@pytest.fixture
def supply_two_vectors_same_rank():
    vector1 = NVector(string='1 2 3')
    vector2 = NVector(string='2 3 4')

    return vector1, vector2

@pytest.fixture
def supply_two_vectors_not_same_rank():
    vector1 = NVector(string='1 2 3')
    vector2 = NVector(string='1 2')

    return vector1, vector2

def test_nvector_init_rank_valid():
    NVector(rank=1)


def test_nvector_init_rank_invalid():
    with pytest.raises(TypeError):
        NVector(rank=1.3)


def test_nvector_init_array_valid():
    NVector(array=[1, 2, 4])


def test_nvector_init_array_invalid():
    with pytest.raises(TypeError):
        NVector(array=[1, '23'])


def test_nvector_init_strint_valid():
    NVector(string='1.3 3.3 4.3')


def test_nvector_init_string_invalid():
    with pytest.raises(ValueError):
        NVector(string='3 1, 3')


def test_nvector_add_valid(supply_two_vectors_same_rank):

    sum = supply_two_vectors_same_rank[0] + supply_two_vectors_same_rank[1]
    assert sum == NVector(string='3 5 7')


def test_nvector_add_invalid(supply_two_vectors_not_same_rank):
    with pytest.raises(NVectorError):
        vector = supply_two_vectors_not_same_rank[0] + supply_two_vectors_not_same_rank[1]


def test_nvector_sub_valid(supply_two_vectors_same_rank):
    sub = supply_two_vectors_same_rank[0] - supply_two_vectors_same_rank[1]

    assert sub == NVector(string='-1.0 -1.0 -1.0')


def test_nvector_sub_invalid(supply_two_vectors_not_same_rank):
    with pytest.raises(NVectorError):
        vector = supply_two_vectors_not_same_rank[0] - supply_two_vectors_not_same_rank[1]


def test_nvector_mul_valid(supply_two_vectors_same_rank):
    mul = supply_two_vectors_same_rank[0] * 2

    assert mul == NVector(string='2 4 6')


def test_nvector_div_valid(supply_two_vectors_same_rank):
    div = (supply_two_vectors_same_rank[0] * 6) / 3
    assert div == NVector(string='2 4 6')


def test_nvector_div_invalid(supply_two_vectors_same_rank):
    with pytest.raises(ZeroDivisionError):
        div = supply_two_vectors_same_rank[0] / 0.0


def test_nvector_matmul_valid(supply_two_vectors_same_rank):
    result = supply_two_vectors_same_rank[0] @ supply_two_vectors_same_rank[1]
    assert result == 20


def test_nvector_matmul_invalie(supply_two_vectors_not_same_rank):
    with pytest.raises(NVectorError):
        result = supply_two_vectors_not_same_rank[0] @ supply_two_vectors_not_same_rank[1]


def test_nvector_norm(supply_two_vectors_same_rank):
    assert abs(supply_two_vectors_same_rank[0]) == 14 ** 0.5


def test_nvector_len(supply_two_vectors_same_rank):
    assert len(supply_two_vectors_same_rank[1]) == 3


def test_nvector_str(supply_two_vectors_same_rank):
    assert str(supply_two_vectors_same_rank[0]) == '1.0, 2.0, 3.0'


def test_nvector_repr(supply_two_vectors_same_rank):
    assert repr(supply_two_vectors_same_rank[0]) == '[1.0, 2.0, 3.0]'


def test_nvector_not_equal_valid(supply_two_vectors_same_rank):
    assert supply_two_vectors_same_rank[0] != supply_two_vectors_same_rank[1]


def test_nvector_not_equal_invalid(supply_two_vectors_not_same_rank):
    with pytest.raises(NVectorError):
        value = supply_two_vectors_not_same_rank[0] != supply_two_vectors_not_same_rank[1]


def test_nvector_equal_valid(supply_two_vectors_same_rank):
    assert supply_two_vectors_same_rank[0] == supply_two_vectors_same_rank[0]


def test_nvector_equal_invalid(supply_two_vectors_not_same_rank):
    with pytest.raises(NVectorError):
        value = supply_two_vectors_not_same_rank[0] == supply_two_vectors_not_same_rank[1]
