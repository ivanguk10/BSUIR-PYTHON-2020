from numbers import Number


def to_json_obj(obj) -> str:
    json_str = ''
    if not isinstance(obj, (dict, list, tuple, Number, str)):
        json_str += '{'
        for attr, value in obj.__dict__.items():
            value = to_json(value)
            json_str += '"' + str(attr) + '"' + ':' + value
        json_str = json_str[:-1]  # delete the last comma
        json_str += '}'
    else:
        if isinstance(obj, tuple):
            obj = [*obj]
        elif isinstance(obj, bool):
            if obj:
                obj = 'true'
            else:
                obj = 'false'
        elif not obj:
            obj = 'null'
        elif isinstance(obj, str):
            obj = '"' + obj + '"'
        json_str += str(obj)
    json_str += ','
    json_str = json_str.replace("'", '"')
    json_str = json_str.replace(' ', '')
    return json_str


def to_json(obj) -> str:
    return to_json_obj(obj)[:-1]  # remove the last comma


def from_json(s):
    i = 0
    s = s.replace(' ', '')
    element, i = parse_json(s, i)
    return element


def parse_json(s, i):
    first_char = s[i]

    if first_char == '{':
        return parse_object(s, i)
    elif first_char == '[':
        return parse_array(s, i)
    elif first_char == '"':
        return parse_string(s, i)
    elif first_char == 'n':
        return parse_null(s, i)
    elif first_char == 't':
        return parse_true(s, i)
    elif first_char == 'f':
        return parse_false(s, i)
    else:
        return parse_number(s, i)


def parse_object(s, i):
    i = i + 1
    new_dict = {}

    while s[i] != '}':
        key, i = parse_string(s, i)
        value, i = parse_json(s, i + 1)
        new_dict[key] = value

        if s[i] == ',':
            i = i + 1
    return new_dict, i + 1


def parse_array(s, i):
    i = i + 1
    new_list = []

    while s[i] != ']':
        element, i = parse_json(s, i)
        new_list.append(element)

        if s[i] == ',':
            i = i + 1
    return new_list, i + 1


def parse_string(s, i):
    i += 1
    j = i
    while s[i] != '"':
        i = i + 1

    python_string = s[j:i]
    return python_string, i + 1


def parse_null(s, i):
    return None, i + 4


def parse_true(s, i):
    return True, i + 4


def parse_false(s, i):
    return False, i + 5


def parse_number(s, i):
    is_number_char = lambda char: '0' <= char <= '9' or char in '+-.'
    j = next((j for j in range(i, len(s)) if not is_number_char(s[j])), len(s))
    use_float = any(s[i] in '.' for i in range(i, j))
    convert = float if use_float else int
    return convert(s[i:j]), j

