class JsonError(Exception):
    def __init__(self, message):
        self.message = message

def to_json(obj):
    obj_type = type(obj)
    if obj_type == int or obj_type == float:
        return str(obj)
    elif obj_type == str:
        return '"' + obj + '"'
    elif obj_type == bool:
        string = str(obj)
        string = string.replace("T", "t")
        string = string.replace("F", "f")
        return string
    elif obj is None:
        string = str(obj).replace("None", "null")
        return string
    elif obj_type == list or obj_type == tuple:
        string = "["
        i = 0
        for val in obj:
            string += f"{to_json(val)}"
            if i < len(obj) - 1:
                string += ", "
            i += 1
        string += "]"
        return string
    elif obj_type == dict:
        string = "{"
        i = 0
        for key, val in obj.items():
            string += f'"{key}": {to_json(val)}'
            if i < len(obj) - 1:
                string += ", "
            i += 1
        string += "}"
        return string
    else:
        string = str(vars(obj)).replace("'", '"')
        string = string.replace("(", "[")
        string = string.replace(")", "]")
        return string
    raise TypeError

def from_json(string):
    string = string.replace("true", "True")
    string = string.replace("false", "False")
    string = string.replace("null", "None")
    return eval(string)