from src.decorator_save_value import Cache_results
import pytest


def test_cache_valid():

    @Cache_results()
    def test_func(a, b):
        return a ** b

    assert test_func(4, 0) is test_func(2, 0)


def test_cache_invalid():

    @Cache_results()
    def test_func(a, b):
        return a ** b
    with pytest.raises(AssertionError):
        assert test_func(1, 2) is test_func(2, 1)


def test_function_kwargs():
    @Cache_results()
    def test_function(a, b):
        return a + b

    value1 = test_function(a=['e'], b=['r'])
    value2 = test_function(1, b=2)
    value3 = test_function(['e'], b=['r'])
    value4 = test_function(a=['e'], b=['r'])

    assert value1 is value4
    assert value1 is not value3
    assert value4 is not value2

