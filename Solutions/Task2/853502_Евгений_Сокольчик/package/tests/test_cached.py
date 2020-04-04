import unittest
from .. import cached
from timeit import default_timer as timer

class TestCached(unittest.TestCase):
    def setUp(self):
        def sum(a, b):
            return (a + b + a + b) * a * b / a / b
        self.sum = cached.cached(sum)

    def test_cached(self):
        start = timer()
        self.sum(99999999999, 99999999999)
        time_1 = timer() - start
        start = timer()
        self.sum(99999999999, 99999999999)
        time_2 = timer() - start
        self.assertTrue((time_1 / time_2) > 2)