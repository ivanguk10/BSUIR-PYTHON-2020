import pytest
from src.to_json import to_json


def supply_non_white_spaced_json(cls):
    json = to_json(cls())
    without_white_spaces = ''.join(json.split())
    return without_white_spaces


class TestSimpleClass:
    def __init__(self):
        self.a = 'a'
        self.b = None
        self.c = 1
        self.d = 2.4


class TestClassWithList:
    def __init__(self):
        self.a = 1
        self.b = [1, 2, 'ad']


class TestClassWithDict:
    def __init__(self):
        self.a = True
        self.b = {"c": 1, "d": 2}


class TestClassWithNestedObject:
    def __init__(self):
        self.a = False
        self.b = TestSimpleClass()


def test_serialize_simple_class():
    assert supply_non_white_spaced_json(TestSimpleClass) == '{"a":"a","b":null,"c":1,"d":2.4}'


def test_serialize_invalid_object_int():
    with pytest.raises(TypeError):
        json = to_json(2)


def test_serialize_invalid_object_list():
    with pytest.raises(TypeError):
        json = to_json([1, 2])


def test_serialize_dict():
    dictionary = {'a': 1, 'b': 2, 'c': TestSimpleClass()}
    json = to_json(dictionary)
    without_white_spaces = ''.join(json.split())

    assert without_white_spaces == '{"a":1,"b":2,"c":{"a":"a","b":null,"c":1,"d":2.4}}'


def test_serialize_class_with_list():
    assert supply_non_white_spaced_json(TestClassWithList) == '{"a":1,"b":[1,2,"ad"]}'


def test_serialize_class_with_dict():
    assert supply_non_white_spaced_json(TestClassWithDict) == '{"a":true,"b":{"c":1,"d":2}}'


def test_serialize_class_with_nested_object():
    assert supply_non_white_spaced_json(TestClassWithNestedObject) == '{"a":false,"b":{"a":"a","b":null,"c":1,"d":2.4}}'
