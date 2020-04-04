import unittest
from .. import singleton

class TestSingleton(unittest.TestCase):
    def setUp(self):
        class Class(metaclass=singleton.Singleton):
            pass
        self.obj_1 = Class()
        self.obj_2 = Class()

    def test_singleton(self):
        self.assertEqual(self.obj_1, self.obj_2)