from src.n_dimensional_vector import Nd_Vector
from src.n_dimensional_vector import NVectorError
import pytest


def test_add_vectors_valid():

    v = Nd_Vector(vector=[1, 3, 4, 3])
    w = Nd_Vector(vector=[1, 3, 4, 3])

    assert v + w == Nd_Vector(vector=[2, 6, 8, 6])


def test_add_vectors_invalid():

    v = Nd_Vector(vector=[1, 3, 4, 3])
    w = Nd_Vector(vector=[1, 3, 4, 3])

    with pytest.raises(AssertionError):
        assert v + w == Nd_Vector(vector=[2, 3, 4, 5])


def test_sub_vectors_valid():

    v = Nd_Vector(vector=[1, 3, 4, 3])
    w = Nd_Vector(vector=[1, 3, 4, 3])

    assert v - w == Nd_Vector(vector=[0, 0, 0, 0])


def test_sub_vectors_invalid():

    v = Nd_Vector(vector=[0, 9, 7, 2])
    w = Nd_Vector(vector=[9, 8, 8])

    with pytest.raises(NVectorError):
        v - w


def test_type_error():

    with pytest.raises(TypeError):
        Nd_Vector(dimension='k')


def test_arguments_error():

    with pytest.raises(NVectorError):
        Nd_Vector()


def test_div_invalid():
    w = Nd_Vector(vector=[9, 8, 8])

    with pytest.raises(ZeroDivisionError):
        w / 0.0


def test_div_valid():
    w = Nd_Vector(vector=[9, 6, 3])

    assert w / 3 == Nd_Vector(vector=[3, 2, 1])


def test_norm_valid():
    w = Nd_Vector(vector=[1, 1, 1, 1])

    assert w.norm() == 2


def test_matmul_valid():

    v = Nd_Vector(vector=[9, 6, 3])
    w = Nd_Vector(vector=[9, 6, 3])

    assert v @ w == Nd_Vector(vector=[81, 36, 9])


def test_floordiv_valid():

    v = Nd_Vector(vector=[9, 6, 3])

    assert v.floordiv(4) == Nd_Vector(vector=[2, 1, 0])


def test_mul_valid():

    v = Nd_Vector(vector=[9, 6, 3])

    assert v.mul(1 / 3) == Nd_Vector(vector=[3, 2, 1])


def test_pow_valid():

    v = Nd_Vector(vector=[9, 16, 36])

    assert v.pow(1 / 2) == Nd_Vector(vector=[3, 4, 6])














