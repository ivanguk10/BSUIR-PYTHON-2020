from src.external_merge import ExternalSorter
from src.merge_sort_upgrade import splitting
from src.external_merge_one import merge_sort
from random import randint


def check_is_sorted(file):
    line1 = file.readline()
    line2 = file.readline()

    while line2 != '' and line1 != '':
        num1 = int(line1[:-1])
        num2 = int(line2[:-1])

        if num1 > num2:
            return False

        line1 = line2
        line2 = file.readline()

    return True


def create_numbers(num):
    with open('../src/numbers.txt', 'w') as f, open('../src/result.txt', 'w') as result:
        f.writelines('{}\n'.format(randint(-1000000, 1000000)) for x in range(num))


def test_small_file():

    create_numbers(100)

    with open('../src/numbers.txt', 'r') as input_file:

        sorter = ExternalSorter(input_file, '../src/result.txt')
        sorter.external_sort()

    with open('../src/result.txt') as result:
        assert check_is_sorted(result) is True


def test_big_file():

    create_numbers(1000000)

    with open('../src/numbers.txt', 'r') as input_file:

        sorter = ExternalSorter(input_file, '../src/result.txt')
        sorter.external_sort()

    with open('../src/result.txt') as result:
        assert check_is_sorted(result) is True


def test_external_sort_incorrect():
    with open('../src/numbers.txt', 'w'):
        pass

    with open('../src/numbers.txt', 'r') as input_file:
        sorter = ExternalSorter(input_file, '../src/result.txt')
        sorter.external_sort()

    with open('../src/result.txt', 'r') as output_file:
        assert check_is_sorted(output_file) is True


def test_merge_upgrade():

    create_numbers(10000)

    splitting()

    with open('../src/result.txt') as result:
        assert check_is_sorted(result) is True


def test_merge_sort_out():

    create_numbers(100)

    merge_sort()

    with open('../src/numbers.txt') as result:
        assert check_is_sorted(result) is True