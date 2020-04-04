import  unittest
from .. import json_converter
import json

class TestJson(unittest.TestCase):
    def setUp(self):
        self.python = {
            "name": "John",
            "age": 30,
            "married": True,
            "divorced": False,
            "children": ("Ann", "Billy"),
            "pets": None,
            "cars": [
                {"model": "BMW 230", "mpg": 27.5},
                {"model": "Ford Edge", "mpg": 24.1}
            ]
        }
        self.json = '{"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], ' \
                 '"pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}'
        class Class():
            def __init__(self):
                self.field_1 = "a"
                self.field_2 = 1
                self.field_3 = [1, 2, 3]
        self.obj = Class()

    def test_to_json(self):
        result = json_converter.to_json(self.python)
        self.assertEqual(result, json.dumps(self.python))
        result = json_converter.to_json(self.obj)
        self.assertEqual(result, '{"field_1": "a", "field_2": 1, "field_3": [1, 2, 3]}')

    def test_from_json(self):
        result = json_converter.from_json(self.json)
        self.assertEqual(result, json.loads(self.json))

if __name__ == '__main__':
    unittest.main()