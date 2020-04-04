import unittest
from tasks.JsonConverter.Decoder import from_json
from tasks.JsonConverter.Encoder import to_json
from json import loads, dumps


class TestJsonEncoder(unittest.TestCase):

    def test_list(self):
        list_from_json = to_json([74, True, False, None, [1, 2],  {"key": 4}])
        self.assertTrue(from_json(list_from_json) == loads(list_from_json))

    def test_dict(self):
        dict_from_json = to_json({1: "one", 2: 'two'})
        self.assertTrue(from_json(dict_from_json) == loads(dict_from_json))

    def test_bool(self):
        self.assertEqual(from_json(to_json(True)), loads(dumps(True)))

    def test_none(self):
        self.assertEqual(from_json(to_json(None)), loads(dumps(None)))

    def test_integer(self):
        self.assertEqual(from_json('50'), loads('50'))

    def test_float(self):
        self.assertEqual(from_json('3.4'), loads('3.4'))
