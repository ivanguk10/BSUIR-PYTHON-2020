import unittest
from tasks.N_Dimensional_Vector import Vector


class TestVector(unittest.TestCase):
    def setUp(self):
        self.vector1 = Vector(1, 2, 5, 3, 10, 7, 17, 18)
        self.vector2 = Vector(20, 1, 3, 2, 1, 5, 7, 0)
        self.vector3 = Vector(6, 8)
        self.vector4 = Vector(1, 1)

    def test_add(self):
        self.assertEqual(self.vector1 + self.vector2, Vector(21, 3, 8, 5, 11, 12, 24, 18))

    def test_sub(self):
        self.assertEqual(self.vector1 - self.vector2, Vector(-19, 1, 2, 1, 9, 2, 10, 18))

    def test_mul(self):
        self.assertEqual(self.vector3 * 10, Vector(60, 80))
        self.assertEqual(self.vector3 * self.vector4, 14)

    def test_eq(self):
        self.assertFalse(self.vector1 == self.vector2)

    def test_str(self):
        self.assertEqual(self.vector4.__str__(), '(1, 1)')

    def test_length(self):
        self.assertEqual(Vector.length(self.vector3), 10)

    def test_get_item(self):
        self.assertEqual(self.vector2[2], 3)
