import time
from src.create_numbers import create_files
from src.merge_sort_upgrade import splitting
from src.to_json_function import Veh, to_json
from src.from_json import Json_to_object
from src.external_merge_one import merge_sort
from src.external_merge import ExternalSorter
from src.decorator_save_value import cat_potato
from src.singleton import MyClass, MyClassWithDec
from src.n_dimensional_vector import Nd_Vector


def faster_sort_example(number):

    create_files(number)
    start_time = time.time()
    splitting()
    print("--- %s seconds ---" % (time.time() - start_time))


def to_json_example():

    ex = Veh('ppp', True, [0.78, 'data deleted', 'o'])
    print(to_json(ex))

    ex1 = Veh(ex, True, [0.78, 'data deleted', 'o'])
    print(to_json(ex1))


def from_json_example(js):

    parser = Json_to_object()

    js1 = '{"color": {"color": "ppp","d": true,"t": [0.78,"data deleted","o"]}, "doors": true,"tires": ["l", {"s": 3}]}'

    js_obj = parser.from_json(js)
    js_obj1 = parser.from_json(js1)

    print(js, js_obj)
    print(js1, js_obj1)


def slow_sort_example(number):

    create_files(number)
    start_time = time.time()
    merge_sort()
    print('--- %s seconds ---' % (time.time() - start_time))


def fastest_sort_example(number):

    create_files(number)
    start_time = time.time()

    with open('numbers.txt', 'r') as input_file:
        sorter = ExternalSorter(input_file, 'result.txt')
        sorter.external_sort()

    print("--- %s seconds ---" % (time.time() - start_time))


def cached_example():

    n = cat_potato(4, 2)
    n1 = cat_potato('i', 'ii')
    n2 = cat_potato(4, 2)

    if n is n1:
        print('The first function is the second function')
    else:
        print('The first function isn\'t the second function')

    if n is n2:
        print('The first function is the third function')
    else:
        print('The first function isn\'t the third function')


def singleton_example():

    m1 = MyClass('With metaclass')
    m2 = MyClass('6')
    k = type(m1)('What?')

    m1.von()
    m2.von()
    k.von()

    print('metaclass:')
    if m1 is m2:
        print('m1 is m2')

    else:
        print('m1 is not m2')

    m1 = MyClassWithDec('With decorator')
    m2 = MyClassWithDec('6')
    k = type(m1)('wtf')

    m1.von()
    m2.von()
    k.von()

    print('decorator:')
    if m1 is m2:
        print('m1 is m2')

    else:
        print('m1 is not m2')


def nd_vector_example():

    vector_1 = Nd_Vector(dimension=4)
    vector_2 = Nd_Vector(vector='0 1 2 3')
    vector_3 = Nd_Vector(vector=[0, 1, 4, 9])

    print('vector_1 @ vector_2 = ', vector_1 @ vector_2)
    print('vector_3 ** (1 / 2) = ', vector_3 ** (1 / 2))
    print('vector_3 - vector_2 = ', vector_3 - vector_2)
    print('vector_2 * 7 = ', vector_2 * 7)
    print('vector_2 / 2 = ', vector_2 / 2)



