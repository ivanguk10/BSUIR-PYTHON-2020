from tasks.JsonConverter.Encoder import to_json
from json import loads, dumps


def from_json(text=' '):
    if text[0] == '{':
        return json_to_dict(text, 0)[0]
    elif text[0] == '[':
        return json_to_list(text, 0)[0]
    else:
        return json_to_basic(text, 0)


def json_to_list(text, start):
    output = []
    i = start
    while i < len(text) - 1:
        i += 1
        if text[i] == ']':
            return output, i
        if text[i] == ' ' or text[i] == ',':
            continue
        if text[i] == '[':
            elem = json_to_list(text, i)
            output.append(elem[0])
            i = elem[1]

        elif text[i] == '{':
            elem = json_to_dict(text, i)
            output.append(elem[0])
            i = elem[1]
        else:
            elem = json_to_basic(text, i)
            output.append(elem[0])
            i = elem[1]


def json_to_dict(text, start):
    output = {}
    i = start
    while i < len(text) - 1:
        i += 1
        if text[i] == '}':
            return output, i
        try:
            elem = get_token(text, i)
            elem2 = get_token(text, elem[1] + 1)
            output[elem[0]] = elem2[0]
            i = elem2[1]
        except IOError as error:
            return output, int(error.args[0])
    raise IOError("Неверный формат")


def json_to_basic(text, start):
    tokens = []
    quot = False
    is_float = False

    def toIntOrFloat(s, f):
        try:
            if f:
                return float(s)
            return int(s)
        except ValueError:
            return None

    for i in range(start, len(text)):
        if (text[i] == ':' or text[i] == ' ') and not quot:
            continue
        if i == len(text) - 1:
            tokens.append(text[i])
            switcher = {"true": True, "false": False, "null": None}
            string = ''.join(tokens)
            return switcher.get(string, toIntOrFloat(string, is_float))
        if (text[i] == ',' or text[i] == ']' or text[i] == '}') and (not quot):
            switcher = {"true": True, "false": False, "null": None}
            string = ''.join(tokens)
            return switcher.get(string, toIntOrFloat(string, is_float)), i - 1
        if text[i] == '"' and quot:
            return ''.join(tokens), i
        if text[i] == '"':
            quot = not quot
            continue
        if text[i] == '.':
            is_float = True
        tokens.append(text[i])
    raise IOError("Неверный формат")


def get_token(text, start):
    for i in range(start, len(text)):
        if text[i] == ' ' or text[i] == ',':
            continue
        if text[i] == '}' or text[i] == ']':
            raise IOError("{}".format(i))
        if text[i] == '[':
            return json_to_list(text, i)
        elif text[i] == '{':
            return json_to_dict(text, i)
        else:
            return json_to_basic(text, i)


if __name__ == "__main__":
    b = [74, True, False, None, [1, 2], {"key": 4}]
    d = {1: "one", 2: 'two'}
    c = to_json(b)
    print(c)
    print(from_json(to_json(True)))
    print(dumps(b))
    print(loads(dumps(b)))
