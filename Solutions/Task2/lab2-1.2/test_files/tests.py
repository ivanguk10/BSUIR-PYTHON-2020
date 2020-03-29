import unittest
import json
import os
from lab2_setupable.lab2_decorator import CacheDecorator
from lab2_setupable.lab2_json import JSON
from lab2_setupable.lab2_singleton import Singleton
from lab2_setupable.lab2_vector import Vector
from lab2_setupable.lab2_sort import ExternalSort

# <editor-fold desc="Additional test classes">

@CacheDecorator.cache
def test_func(number, *args):
    result = 0

    for arg in list(args):
        result += int(arg)
    return result * number


@CacheDecorator.cache
def test_func_2(number, bubble):
    return "number: {} bubble: {}".format(number, bubble)


@CacheDecorator.cache
def test_func_3(**kwargs):
    return True


class TestClass2:
    def __init__(self):
        self.age = 10
        self.gender = 'Man'
        self.home = 'Minsk, Pushkinskaya 38/120'
        self.ingo = ['', '', False]


class TestClass(metaclass=Singleton):

    def __init__(self, age = 0, name = '', sex = False, attributes=[]):
        self.age = age
        self.attributes = attributes
        self.name = name
        self.sex = sex
        self.cl = TestClass2()

# </editor-fold>

# <editor-fold desc="Test classes">


class TestSort(unittest.TestCase):
    def test_sort(self):
        DEFAULT_FILEPATH = os.getcwd() + '\\test_files\\numbers_test.txt'
        RESULT_PATH = os.getcwd() + '\\test_files\\results_test.txt'
        ExternalSort.sort_external(DEFAULT_FILEPATH, RESULT_PATH)


class TestJSON(unittest.TestCase):
    def test_JSON(self):
        test_dict = {"data": ['value1', True, 123], "value": [{"value_1": "value1", "value_2": [1, 2, 3]}, 1]}
        test_list = ["value", True, {1: '1', "r": 12}]
        test_data = TestClass(18, 'Andrey', True, ['Check', 'test', [1, 2, 3]])
        serialized = JSON.serialize(test_data)
        serialized_dict = JSON.serialize(test_dict)
        serialized_list = JSON.serialize(test_list)
        JSON.deserialize(serialized_dict)
        self.assertTrue(isinstance(serialized_dict, str))
        test_result = JSON.deserialize(serialized)
        self.assertEqual(test_data.name, test_result["name"])
        self.assertEqual(test_data.age, test_result["age"])
        self.assertEqual(test_data.attributes, test_result["attributes"])
        self.assertEqual(test_data.sex, test_result["sex"])
        self.assertTrue(test_data.cl.__dict__ == test_result["cl"])
        self.assertEqual(test_result, json.loads(serialized))


class TestVectorMethods(unittest.TestCase):


    def test_init(self):
        with self.assertRaises(ValueError):
            Vector(*['f', 'g'])
        self.assertEqual(str(Vector(*[1, 2, 3, 4])), str([1, 2, 3, 4]))

    def test_add(self):
        test_vector = Vector(*[1, 2, 3, 4])
        self.assertTrue(test_vector + Vector(*[2, 3, 4, 5]) == Vector(*[3, 5, 7, 9]))
        self.assertTrue(test_vector + 3 == Vector(*[4, 5, 6, 7]))
        self.assertTrue(test_vector.scalar_multiply(test_vector))
        with self.assertRaises(AttributeError):
            test_vector.scalar_multiply(Vector(*[1, 2]))
        with self.assertRaises(TypeError):
            test_vector.scalar_multiply('2')
        with self.assertRaises(TypeError):
            test_vector + 'CHECK'
        with self.assertRaises(TypeError):
            test_vector + Vector(*[2, 4, 5, 10, 12, 46, 77])

    def test_sub(self):
        test_vector = Vector(*[5, 6, 7, 8])
        self.assertTrue(test_vector - Vector(*[2, 3, 4, 5]) == Vector(*[3, 3, 3, 3]))
        self.assertTrue(test_vector - 3 == Vector(*[2, 3, 4, 5]))
        with self.assertRaises(TypeError):
            test_vector - 'CHECK'
        with self.assertRaises(TypeError):
            test_vector - Vector(*[2, 4, 5, 10, 12, 46, 77])

    def test_multiply(self):
        test_vector = Vector(*[1, 2, 3, 4])
        self.assertEqual(test_vector * 2, Vector(*[2, 4, 6, 8]))
        self.assertEqual(test_vector.scalar_multiply(Vector(*[2, 2, 2, 2])), 20)
        with self.assertRaises(TypeError):
            test_vector.scalar_multiply('CHECK')
        with self.assertRaises(AttributeError):
            test_vector.scalar_multiply(Vector(*[1, 2]))
        with self.assertRaises(TypeError):
            test_vector * 'str'

    def test_equal(self):
        test_vector = Vector(*[1, 2, 3, 4])
        self.assertTrue(not (test_vector == 'f'))
        self.assertTrue(not (test_vector == Vector(*[1,2,3])))


class TestDecorator(unittest.TestCase):
    def test_decorator(self):

        self.assertTrue(test_func(10, 1, 3, 3, 4) != test_func(12, 5, 7))
        self.assertTrue(test_func(10, 1, 3, 3, 4) == test_func(10, 3, 1, 3, 4))
        self.assertTrue(test_func(10, 1, 3, 3, 4) == test_func(10, 1, 3, 3, 4))
        self.assertEqual(test_func_2(12, 25), test_func_2(bubble=25, number=12))
        self.assertTrue(test_func_3(val= "value", map= "map"))


class TestSingleton(unittest.TestCase):
    def test_singleton(self):
        self.assertEqual(TestClass(name = "name"), TestClass())

# </editor-fold>


if __name__ == "__main__":
    unittest.main()