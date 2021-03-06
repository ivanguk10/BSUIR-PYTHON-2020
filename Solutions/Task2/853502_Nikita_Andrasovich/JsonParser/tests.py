import parser
import unittest


class NestedClass:
    def __init__(self, inner_objects=None):
        self.inner_objects = inner_objects


class TestParse(unittest.TestCase):

    def test_two_way_list(self):
        list = ["Wow", None, "Boom", 5, False, 4.2]

        json = parser.to_json(list)
        restored_list = parser.from_json(json, globals())

        self.assertEqual(list, restored_list)

    def test_nested_class(self):
        nested_class = NestedClass([NestedClass(), NestedClass()])

        json = parser.to_json(nested_class)
        restored_class = parser.from_json(json, globals())

        self.assertEqual(len(nested_class.inner_objects),
                         len(restored_class.inner_objects))

    def test_restore_type(self):
        some_class = NestedClass()

        json = parser.to_json(some_class)
        restored_class = parser.from_json(json, globals())

        self.assertEqual(type(some_class), type(restored_class))

    def test_predefined_json(self):
        some_class = NestedClass()

        json = parser.to_json(some_class)

        self.assertEqual(
            json, "{ \"py/object\": \"NestedClass\", \"inner_objects\": null }")

    def test_broken_json(self):
        with self.assertRaises(Exception):
            parser.from_json("Not a Json", globals())


def tests_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestParse, 'test'))
    return suite
