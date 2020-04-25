import random
import os
from src.ExternalSorter import ExternalSorter
import pytest

INPUT_TEST_FILE_NAME = 'test.txt'
OUTPUT_TEST_FILE_NAME = 'result.txt'


def check_is_sorted(file):
    line1 = file.readline()
    line2 = file.readline()

    num1 = 0

    if line1 != '':
        num1 = int(line1[:-1])

    while line1 != '' or line2 != '':
        num2 = int(line2[:-1])

        if num1 > num2:
            return False

        num1 = num2
        line2 = file.readline()
        line1 = file.readline()

    return True


def generate_file(size=10000, max_value=100000, generate_new=False):
    if not os.path.isfile('output.txt') or generate_new:
        with open(INPUT_TEST_FILE_NAME, 'w') as f:
            f.writelines('{}\n'.format(random.randint(-max_value, max_value)) for _ in range(size))


def sort_test_file():
    with open(INPUT_TEST_FILE_NAME, 'r') as input_file:
        sorter = ExternalSorter(input_file, output_file_name=OUTPUT_TEST_FILE_NAME)
        sorter.external_sort()


def test_external_sort():
    generate_file()
    sort_test_file()

    with open(OUTPUT_TEST_FILE_NAME, 'r') as output_file:
        assert check_is_sorted(output_file) is True


def test_external_sort_small_file():
    generate_file(size=100, generate_new=True)

    sort_test_file()

    with open(OUTPUT_TEST_FILE_NAME, 'r') as output_file:
        assert check_is_sorted(output_file) is True


def test_external_sort_big_values():
    generate_file(max_value=10000000, generate_new=True)

    sort_test_file()

    with open(OUTPUT_TEST_FILE_NAME, 'r') as output_file:
        assert check_is_sorted(output_file) is True


def test_external_sort_big_file():
    generate_file(size=1000000, generate_new=True)

    sort_test_file()

    with open(OUTPUT_TEST_FILE_NAME, 'r') as output_file:
        assert check_is_sorted(output_file) is True


def test_external_sort_incorrect():
    with open(INPUT_TEST_FILE_NAME, 'w'):
        pass

    sort_test_file()

    with open(OUTPUT_TEST_FILE_NAME, 'r') as output_file:
        assert check_is_sorted(output_file) is True
