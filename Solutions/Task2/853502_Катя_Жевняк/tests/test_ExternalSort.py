import unittest
from tasks.ExternalSort.ExternalSort import Sort


class TestSorting(unittest.TestCase):

    def setUp(self):
        Sort("test_numbers.txt")

    def test_order(self):
        with open("result_file.txt", 'r') as f:
            a = int(f.readline())
            for num in f:
                b = int(num)
                self.assertTrue(a <= b)
                a = b

    def test_number(self):
        first_counter = 0
        second_counter = 0
        with open('test_numbers.txt') as f:
            for _ in f:
                first_counter += 1
        with open('result_file.txt') as f:
            for _ in f:
                second_counter += 1
        self.assertEqual(first_counter, second_counter)
