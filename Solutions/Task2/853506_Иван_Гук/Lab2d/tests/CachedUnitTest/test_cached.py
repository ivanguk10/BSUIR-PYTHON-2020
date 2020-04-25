import pytest
from src.cached import cached
from datetime import datetime


def test_function_one_argv():
    @cached
    def function_to_test(a):
        return a + '1'

    value1 = function_to_test('')
    value2 = function_to_test('a')
    value3 = function_to_test('')

    assert value1 is value3
    assert value1 is not value2


def test_function_two_argv():
    @cached
    def function_to_test(a, b):
        return str(a) + str(b)

    value1 = function_to_test('', 'a')
    value2 = function_to_test(0, 1)
    value3 = function_to_test('', 'a')
    value4 = function_to_test(0, 1)

    assert value1 is not value2
    assert value2 is value4
    assert value1 is value3


def test_function_kwargs():
    @cached
    def function_to_test(first, second):
        return first + second

    value1 = function_to_test(first=[1], second=[2])
    value2 = function_to_test('a', second='b')
    value3 = function_to_test([1], second=[2])
    value4 = function_to_test(first=[1], second=[2])

    assert value1 is value4
    assert value1 is not value3
    assert value4 is not value2


def test_function_no_arguments():
    @cached
    def function_to_test():
        return datetime.now()

    value1 = function_to_test()
    value2 = function_to_test()

    assert value1 is value2



