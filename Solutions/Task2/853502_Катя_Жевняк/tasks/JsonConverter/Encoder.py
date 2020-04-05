from json import dumps


def to_json(obj):
    if isinstance(obj, (int, float, str, bool, type(None))):
        return basic_type_to_json(obj)
    elif isinstance(obj, (list, tuple)):
        return tuple_or_list_to_json(obj)
    elif isinstance(obj, dict):
        return dict_to_json(obj)
    else:
        return custom_class_to_json(obj)


def basic_type_to_json(obj):
    if isinstance(obj, str):
        return f'"{obj}"'
    elif isinstance(obj, bool):
        return f'{obj.__str__().lower()}'
    elif isinstance(obj, type(None)):
        return "null"
    else:
        return obj.__str__()


def tuple_or_list_to_json(obj_list):
    return '[{}]'.format(", ".join(to_json(obj) for obj in obj_list))


def dict_to_json(obj_dict):
    return '{%s}' % (', '.join('"{}": {}'.format(key, to_json(value)) for key, value in obj_dict.items()))


def custom_class_to_json(obj):
    fields = [(f, obj.__getattribute__(f)) for f in dir(obj) if
              not callable(getattr(obj, f)) and not (f.startswith('__') or f.startswith('_'))]
    obj_dict = dict(fields)
    return dict_to_json(obj_dict)


if __name__ == "__main__":
    combo = [74, True, False, None, [1, 2],  {"key": 4}]
    test_dict = {5: "may", 4: 'april'}
    a = to_json(combo)
    print("Json:\n" + to_json(combo), end="\n\n")
    print(dumps(combo))
    print("Json:\n" + to_json(test_dict), end="\n\n")

