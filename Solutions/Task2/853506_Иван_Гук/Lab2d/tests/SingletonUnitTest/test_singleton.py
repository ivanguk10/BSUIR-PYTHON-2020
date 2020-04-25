import pytest
from src.Singleton import SingletonMeta


def test_singleton():
    class TestClass(metaclass=SingletonMeta):
        pass

    value1 = TestClass()
    value2 = TestClass()

    assert value1 is value2


def test_inherited_singleton():
    class TestClassParent:
        pass

    class TestClassChild(TestClassParent, metaclass=SingletonMeta):
        pass

    value1 = TestClassChild()
    value2 = TestClassChild()
    value3 = TestClassParent()

    assert value1 is value2
    assert value3 is not value1

