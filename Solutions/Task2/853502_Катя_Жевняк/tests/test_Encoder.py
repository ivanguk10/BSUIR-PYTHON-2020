import unittest
from tasks.JsonConverter.Encoder import to_json
from json import dumps


class TestJsonEncoder(unittest.TestCase):

    def test_list(self):
        list_to_json = [74, True, False, None, [1, 2],  {"key": 4}]
        self.assertTrue(to_json(list_to_json) == dumps(list_to_json))

    def test_dict(self):
        dict_to_json = {1: "one", 2: 'two'}
        self.assertTrue(to_json(dict_to_json) == dumps(dict_to_json))

    def test_bool(self):
        self.assertEqual(to_json(True), dumps(True))

    def test_none(self):
        self.assertEqual(to_json(None), dumps(None))

    def test_string(self):
        self.assertEqual(to_json("str"), dumps("str"))

    def test_integer(self):
        self.assertEqual(to_json(50), dumps(50))

    def test_float(self):
        self.assertEqual(to_json(3.4), dumps(3.4))
