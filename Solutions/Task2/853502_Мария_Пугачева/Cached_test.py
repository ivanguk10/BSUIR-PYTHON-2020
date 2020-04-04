import unittest
import Cached


class TestCashed(unittest.TestCase):
    counter = 0

    @staticmethod
    @Cached.cached
    def Counter(num):
        TestCashed.counter += num
        return TestCashed.counter

    def test_cached(self):
        TestCashed.Counter(2)
        a = TestCashed.Counter(2)
        self.assertEqual(a, 2)


if __name__ == '__main__':
    unittest.main()
