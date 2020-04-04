import unittest
import NDimensionalVector


class TestVector(unittest.TestCase):
    def test_vector(self):
        vec1 = NDimensionalVector.NDimensionalVector(1, 2, 3, 4, 5)
        vec2 = NDimensionalVector.NDimensionalVector(2, 3, 4, 5, 6, 7, 8, 9)
        sum = NDimensionalVector.NDimensionalVector(3, 5, 7, 9, 11, 7, 8, 9)
        diff = NDimensionalVector.NDimensionalVector(-1, -1, -1, -1, -1, -8, -9)
        mul = NDimensionalVector.NDimensionalVector(1, 5, 12, 20, 30)
        mul2 = NDimensionalVector.NDimensionalVector(2, 4, 8, 16, 32)
        self.assertEqual(vec1 + vec2, sum)
        self.assertEqual(vec1 - vec2, diff)
        self.assertEqual(vec1 * vec2, mul)
        self.assertEqual(vec1 * 2, mul2)
        self.assertEqual(vec1 == vec2, False)
        self.assertEqual(vec1 != vec2, True)
        self.assertEqual(len(vec1), 5)
        self.assertEqual(vec1[3], 4)


if __name__ == '__main__':
    unittest.main()
