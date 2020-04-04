import unittest
from .. import vector

class TestVector(unittest.TestCase):
    def setUp(self):
        self.vector_1 = vector.Vector(1, 2, 3, 4, 5)
        self.vector_2 = vector.Vector(2, 4, 6, 8, 10)
        self.vector_dim = vector.Vector(1, 2, 3, 4, 5, 6)

    def test_init(self):
        with self.assertRaises(TypeError):
            v = vector.Vector(1, 2, "a")
        with self.assertRaises(TypeError):
            v = vector.Vector(1, [1, 2], {1: 2})

    def test_len(self):
        result = self.vector_1.__len__()
        self.assertEqual(result, pow(55, 1 / 2))

    def test_component(self):
        result = self.vector_1.__getitem__(2)
        self.assertEqual(result, 3)
        with self.assertRaises(IndexError):
            self.vector_1.__getitem__(5)

    def test_representation(self):
        result = self.vector_1.__repr__()
        self.assertEqual(result, "(1, 2, 3, 4, 5)")

    def test_add(self):
        result = self.vector_1 + self.vector_2
        self.assertTrue(result.__repr__() == "(3, 6, 9, 12, 15)")
        with self.assertRaises(vector.VectorError):
            self.vector_1 + self.vector_dim
        with self.assertRaises(TypeError):
            self.vector_1 + 1

    def test_subtract(self):
        result = self.vector_2 - self.vector_1
        self.assertTrue(result.__repr__() == "(1, 2, 3, 4, 5)")
        with self.assertRaises(vector.VectorError):
            self.vector_1 - self.vector_dim
        with self.assertRaises(TypeError):
            self.vector_1 - 1

    def test_equality(self):
        result = self.vector_2 == self.vector_1
        self.assertFalse(result)
        result = self.vector_1 == self.vector_1
        self.assertTrue(result)
        self.assertFalse(self.vector_1 == self.vector_dim)
        with self.assertRaises(TypeError):
            self.vector_1 == 1

    def test_multiplication(self):
        result = self.vector_2 * self.vector_1
        self.assertEqual(result, 110)
        result = self.vector_1 * 5
        self.assertTrue(result.__repr__() == "(5, 10, 15, 20, 25)")
        with self.assertRaises(vector.VectorError):
            self.vector_1 * self.vector_dim
        with self.assertRaises(TypeError):
            self.vector_1 * "a"