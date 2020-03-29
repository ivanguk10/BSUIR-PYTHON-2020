import json
import os
from lab2_setupable.lab2_decorator import CacheDecorator
from lab2_setupable.lab2_json import JSON
from lab2_setupable.lab2_singleton import Singleton
from lab2_setupable.lab2_vector import Vector
from lab2_setupable.lab2_sort import ExternalSort

def json_exmpl():
    class TestClass2:
        def __init__(self):
            self.age = 10
            self.gender = 'Man'
            self.home = 'Minsk, Pushkinskaya 38/120'
            self.ingo = ['', '', False]

    class TestClass:
        def __init__(self, age=0, name='', sex=False, attributes=[]):
            self.age = age
            self.attributes = attributes
            self.name = name
            self.sex = sex
            self.cl = TestClass2()

    test_data = TestClass(18, 'Andrey', True, [[1, 2, False], 'test', 'JSON'])
    serialized = JSON.serialize(test_data)
    print('{}\n\nDeserialized:'.format(serialized))
    print("Standard method result: ", json.loads(serialized))
    print("My method result:       ", JSON.deserialize(serialized))

def decorator_exmpl():
    @CacheDecorator.cache
    def test_func(**kwargs):
        for arg in kwargs:
            print("{}, ".format(arg))
        return True
    print("Вызовем одну и ту же функцию два раза подряд с одинаковыми параметрами:\n"
          "Если будет выведено \'Decorator works!\', значит было использовано значение из декоратора.")
    print("Значение функции 1: ", test_func(10, 22))
    print("Значение функции 2: ", test_func(10, 22))

def vector_exmpl():
    x1 = Vector(*[1, 2, 5, 16, 74, 29])
    x2 = Vector(*[1, 5, 16, 28, 120, 77])
    mul_pr = lambda x, y, zn, r: print("{} {} {} = {}".format(x, y, zn, r))
    mul_pr(str(x1), '*', str(x2), x1.scalar_multiply(x2))
    mul_pr(str(x1), '*', 17, str(x1*17))
    mul_pr(str(x1), '+', str(x2), str(x1 + x2))
    mul_pr(str(x1), '+', 29, str(x1 + 29))
    print("X1: \tX2:")
    for i in range(len(x1)):
        print("[{}] \t[{}]".format(x1[i], x2[i]))
    print("mod{} = {}".format(x1, len(x1)))
    print("{}*{}")

def singleton_exmpl():
    class TestClass(metaclass=Singleton):

        def __init__(self, age=0, name='', sex=False, attributes=[]):
            self.age = age
            self.attributes = attributes
            self.name = name
            self.sex = sex

    print("Первое создание: {}\nВторое создание: {}".format(TestClass(name="Pappi"), TestClass(sex=True)))

def sort_exmpl():
    print('Ama here')
    DEFAULT_FILEPATH = os.getcwd() + '\\test_files\\numbers_test.txt'
    RESULT_PATH = os.getcwd() + '\\test_files\\results_test.txt'
    ExternalSort.sort_external(DEFAULT_FILEPATH, RESULT_PATH)
    print("Файл отсортирован. Можете увидеть результат по пути {}".format(RESULT_PATH))