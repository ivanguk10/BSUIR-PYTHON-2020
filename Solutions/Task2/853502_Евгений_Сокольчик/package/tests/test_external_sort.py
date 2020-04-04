import unittest
import random
from .. import external_sort

class TestSort(unittest.TestCase):
    def setUp(self):
        with open("input.txt", "w") as file:
            file.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for i in range(1000000))

    def test_sort(self):
        with open("input.txt", "r") as file:
            expect = file.readlines()
            expect = list(map(int, expect))
            expect.sort()
        external_sort.external_sort("input.txt", "output.txt", 10000)
        with open("output.txt", "r") as file:
            result = file.readlines()
            result = list(map(int, result))
        self.assertEqual(result, expect)
        external_sort.external_sort("input.txt", "output.txt", 1000)
        with open("output.txt", "r") as file:
            result = file.readlines()
            result = list(map(int, result))
        self.assertEqual(result, expect)

    def test_file(self):
        with self.assertRaises(FileNotFoundError):
            with open("n.txt", "r"):
                pass