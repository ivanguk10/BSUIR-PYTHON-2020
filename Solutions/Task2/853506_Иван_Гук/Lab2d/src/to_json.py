def __list_tuple_to_json(obj, level):
    string = '[\n'
    for element in obj[:-1]:
        string += '\t' * level + __value_to_json(element, level + 1) + ',\n'

    string += '\t' * level + __value_to_json(obj[-1], level + 1)
    string += ']'

    return string


def __dict_to_json(obj: dict, level):
    string = '{\n'
    for key, value in list(obj.items())[:-1]:
        string += '\t' * level + '"{}": '.format(str(key)) + __value_to_json(value, level + 1) + ",\n"

    last_key, last_value = list(obj.items())[-1]

    string += '\t' * level + '"{}": '.format(str(last_key)) + __value_to_json(last_value, level + 1)
    string += '}'

    return string


def __value_to_json(value, level):
    string = ''

    if isinstance(value, dict):
        string = __dict_to_json(value, level)

    elif isinstance(value, list) or isinstance(value, tuple):
        string = __list_tuple_to_json(value, level)

    elif isinstance(value, bool):
        string = 'true' if value else 'false'

    elif isinstance(value, int) or isinstance(value, float) or isinstance(value, complex):
        string = str(value)

    elif isinstance(value, str):
        string = '"{}"'.format(str(value))

    elif value is None:
        string = 'null'

    else:
        string += __object_to_json(value, level)

    return string


def __object_to_json(obj: object, level):
    json_string = '{\n'

    if isinstance(obj, dict):
        iterable_dict = obj
    else:
        iterable_dict = vars(obj)

    for key, value in list(iterable_dict.items())[:-1]:
        json_string += '\t' * level + '"{}": {}'.format(str(key), __value_to_json(value, level + 1)) + ',\n'

    last_key, last_value = list(iterable_dict.items())[-1]
    json_string += '\t' * level + '"{}": {}'.format(str(last_key), __value_to_json(last_value, level + 1))

    json_string += '}'
    return json_string


def to_json(obj: object):
    return __object_to_json(obj, 0)
