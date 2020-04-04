from src.singleton import Singleton, singleton
import pytest


def test_decorator_singleton_valid():
    @singleton
    class MyClass:
        pass

    n = MyClass()
    n1 = MyClass()

    assert n == n1


def test_decorator_singleton_invalid():
    @singleton
    class MyClass:
        pass

    n = MyClass()
    n1 = type(n)()

    with pytest.raises(AssertionError):
        assert n == n1


def test_metaclass_singleton_valid():
    class MyClass(metaclass=Singleton):
        pass

    n = MyClass()
    n1 = type(n)()

    assert n == n1


def test_metaclass_singleton_invalid():

    class MyClass(metaclass=Singleton):
        pass

    class MyClassChild(MyClass):
        pass

    n = MyClass()
    n1 = MyClassChild()

    with pytest.raises(AssertionError):
        assert n == n1
