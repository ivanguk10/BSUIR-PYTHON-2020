import unittest
from lab2.ExSort import ExSort
from lab2.decorator_cashed import *
from lab2.Singleton import *
from lab2.vector_n import *
from lab2.JSON_Serializer import *
from json import dumps


class TestExSort(unittest.TestCase):
    def test_ex_sort(self):
        for i in range(1):
            s = ExSort(10000, 1000)
            s.create_file()
            s.split_file()
            s.merge_sort()
            check = []
            result = []
            with open('result', 'r') as file:
                for line in file:
                    result.append(int(line))
            with open('numbers.txt', 'r') as file:
                for line in file:
                    check.append(int(line))
            check = sorted(check)
            self.assertEqual(result, check)


class TestDecorator(unittest.TestCase):
    def test_dec(self):
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(5), 5)
        self.assertEqual(sum(1, 2, 3, 4, 5), 15)
        self.assertEqual(sum(1, 2, 3, 4, 5), 15)


class TestSingleton(unittest.TestCase):
    def test_Singleton(self):
        man = Zeus()
        woman = Zeus()
        self.assertEqual(man, woman)


class TestVector(unittest.TestCase):
    def test_vector(self):
        v1 = Vector(10, 5, 3)
        v2 = Vector(2, 3, 3)
        v3 = Vector(12, 8, 6)
        v6 = Vector(60, 30, 18)
        v4 = Vector(8,2,0)
        self.assertEqual(v3, v1+v2)
        self.assertEqual(v1*v2, 44)
        self.assertEqual(v6, v1*6)
        v3[2] = 6
        self.assertEqual(v3[2], 6)
        self.assertEqual(v1 == v2, False)
        self.assertEqual(v1 == v1, True)
        self.assertEqual(len(v1), 3)
        self.assertEqual(v1-v2, v4)


class TestToJSON(unittest.TestCase):
    def test_list(self):
        ser = JSON_Serializer([1, 2, 3, 4])
        dumps_string = dumps([1, 2, 3, 4])
        self.assertSequenceEqual(str(ser), dumps_string)

    def test_string(self):
        string = 'Legendarnoe,zolotoe otlichno'
        ser = JSON_Serializer(string)
        dumps_string = dumps(string)
        self.assertSequenceEqual(str(ser), dumps_string)

    def test_dict(self):
        dictionary = {'a': 1, "b": "Just String", "list": [1, 2, 3, 4]}
        ser = JSON_Serializer(dictionary)
        dumps(dictionary)
        self.assertSequenceEqual(str(ser), dumps(dictionary))

    def test_user_defined_objects(self):
        from lab2.JSON_Serializer import TestClass
        import json

        class MyEncoder(json.JSONEncoder):
            def default(self, o):
                dictionary = o.__dict__
                return dictionary

        ser = JSON_Serializer(TestClass())

        self.assertSequenceEqual(MyEncoder().encode(TestClass()), str(ser))


from lab2.JSON_Deserializer import *

class TestFromJSON(unittest.TestCase):
    def test(self):
        parser = Parser("{dic:{a:3,b:2,c:1},int1:1,int2:3,l1:[1,2,3,4]}")
        diction = loads("{\"dic\":{\"a\":3,\"b\":2,\"c\":1},\"int1\":1,\"int2\":3,\"l1\":[1,2,3,4]}")
        parser.start()
        Sh = Shtirlits(parser.to_dict())
        self.assertSequenceEqual(str(diction["dic"]["a"]), Sh.dic.a)


if __name__ == '__main__':
    unittest.main()
