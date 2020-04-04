import unittest
import MergeSort


class MergeSortTest(unittest.TestCase):
    @staticmethod
    def create_file(filename):
        n = 5000
        with open(filename, 'w+') as f:
            f.writelines('{}\n'.format(i * ((-1) ** i)) for i in range(n))

    def test_merge_sort(self):
        filename = 'numbers.txt'
        MergeSortTest.create_file(filename)
        obj = MergeSort.ExternalMergeSort(filename)
        obj.merge_sort()
        with open(filename, 'r') as file:
            i = int(-4999)
            line = file.readline()
            while line and i < 0:
                self.assertEqual(int(line), i)
                line = file.readline()
                i += 2
            i = 0
            while line and i < 0:
                self.assertEqual(int(line), i)
                line = file.readline()
                i += 2


if __name__ == '__main__':
    unittest.main()
