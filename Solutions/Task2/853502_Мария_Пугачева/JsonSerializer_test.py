import unittest
import jsonSerializer
import json


class Cl:
    def __init__(self):
        self.i = 55
        self.st = 'hhh'
    pass


class JsonSerializerTest(unittest.TestCase):
    def test_Correct(self):
        temp = {'a': 'string', 'b': 4, 'c': [1, 2]}
        json_str = jsonSerializer.to_json(temp)
        obj = json.loads(json_str)
        self.assertEqual(temp, obj)

    def test_Incorrect(self):
        obj = Cl()
        temp = {'a': 'string', 'b': obj, 'c': [1, 2]}
        json_str = jsonSerializer.to_json(temp)
        obj = json.loads(json_str)
        self.assertNotEquals(temp, obj)
        ''' 
        получившийся объект не равен исходному, 
        тк десериализация всегда преобразовывавет json объекты в словари,
        а изначально 'obj' был объектом класса Cl
        '''


if __name__ == '__main__':
    unittest.main()
