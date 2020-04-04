import unittest
from . import test_external_sort
from . import test_cached
from . import test_json_converter
from . import test_singleton
from . import test_vector

def run():
    suite_cached = unittest.TestLoader().loadTestsFromModule(test_cached)
    suite_sort = unittest.TestLoader().loadTestsFromModule(test_external_sort)
    suite_json = unittest.TestLoader().loadTestsFromModule(test_json_converter)
    suite_singleton = unittest.TestLoader().loadTestsFromModule(test_singleton)
    suite_vector = unittest.TestLoader().loadTestsFromModule(test_vector)
    all_tests = unittest.TestSuite([suite_cached, suite_sort, suite_json, suite_singleton, suite_vector])
    unittest.TextTestRunner(verbosity=2).run(all_tests)