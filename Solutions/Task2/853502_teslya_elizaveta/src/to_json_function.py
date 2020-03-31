def _list_tuple_to_json(obj):
    """Serialize list or tuple to JSON

    Args:
        obj (list, tuple): list or tuple to serialize.
    Returns:
        string(str): JSON-string representation of list or tuple.
    """

    string = '['
    for element in obj[:-1]:
        string += _value_to_json(element) + ','

    string += _value_to_json(obj[-1])
    string += ']'

    return string


def _dict_to_json(obj: dict):
    """Serialize dict to JSON

    Args:
        obj (dict): dict to serialize.
    Returns:
        string(str): JSON-string representation of dict.
    """

    string = '{'

    for key, value in list(obj.items())[:-1]:
        string += '"{}": '.format(str(key)) + _value_to_json(value) + ","

    last_key, last_value = list(obj.items())[-1]

    string += '"{}": '.format(str(last_key)) + _value_to_json(last_value)
    string += '}'

    return string


def _value_to_json(value):
    """Serialize object to JSON-string

    Args:
        value (obj): object to serialize.
    Returns:
        string(str): JSON-string representation of object.
    """
    string = ''

    if isinstance(value, dict):
        string = _dict_to_json(value)

    elif isinstance(value, list) or isinstance(value, tuple):
        string = _list_tuple_to_json(value)

    elif isinstance(value, bool):
        string = 'true' if value else 'false'

    elif isinstance(value, int) or isinstance(value, float) or isinstance(value, complex):
        string = str(value)

    elif isinstance(value, str):
        string = '"{}"'.format(str(value))

    elif value is None:
        string = 'null'

    else:
        string += _object_to_json(value)

    return string


def _object_to_json(obj: object):
    """Serialize object to JSON

    Args:
        obj (object): object to serialize.
    Returns:
        string(str): JSON-string representation of object.
    """
    json_str = '{'

    if isinstance(obj, dict):
        iterable_dict = obj
    else:
        iterable_dict = obj.__dict__

    for key, value in list(iterable_dict.items())[:-1]:
        json_str += '"{}": {}'.format(str(key), _value_to_json(value)) + ','

    last_key, last_value = list(iterable_dict.items())[-1]
    json_str += '"{}": {}'.format(str(last_key), _value_to_json(last_value))

    json_str += '}'
    return json_str


def to_json(obj: object):
    """Serializes Python object to JSON

    Serialize Python object with __dict__ attribute into JSON string.

    Args:
        obj (object): serializable object.
    Raises:
        TypeError: if object doesn't have __dict__ attribute.
    Return:
        json_string (str): JSON representation of object.
    """

    return _object_to_json(obj)


class Veh(object):

    def __init__(self, color, doors, tires):

        self.color = color
        self.doors = doors
        self.tires = tires
