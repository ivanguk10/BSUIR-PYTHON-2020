from src.to_json_function import to_json
from src.from_json import Json_to_object, FromJsonError
import pytest


def test_from_json_valid():

    parser = Json_to_object()

    js = '{"color": {"color": "ppp","doors": true,"tires": [0.78,"data deleted","o"]},' \
         '"doors": true,"tires": [0.78,"data deleted","o"]}'
    js_obj = parser.from_json(js)

    assert js_obj == {'color': {'color': 'ppp', 'doors': True, 'tires': [0.78, 'data deleted', 'o']},
                      'doors': True, 'tires': [0.78, 'data deleted', 'o']}


def test_from_json_invalid():

    parser = Json_to_object()

    js = '{s}'

    with pytest.raises(FromJsonError):
        parser.from_json(js)

    js = '{":}'

    with pytest.raises(IndexError):
        print(parser.from_json(js))

    js = '}'

    with pytest.raises(FromJsonError):
        print(parser.from_json(js))


def test_to_json_valid():
    class Vehicle(object):

        def __init__(self, color, doors, tires):
            self.color = color
            self.doors = doors
            self.tires = tires

    m = Vehicle('ppp', True, [0.78, 'data deleted', 'o'])
    mo = Vehicle(m, True, [0.78, 'data deleted', 'o'])

    assert to_json(m) == '{"color": "ppp","doors": true,"tires": [0.78,"data deleted","o"]}'

    assert to_json(mo) == '{"color": {"color": "ppp","doors": true,"tires": [0.78,"data deleted","o"]},' \
                          '"doors": true,"tires": [0.78,"data deleted","o"]}'

    with pytest.raises(AttributeError):
        to_json([])
