from warnings import warn
from collections.abc import Hashable


def __hash_arguments(args: tuple, kwargs: dict):
    hash_value = 0
    for value in args:
        if not isinstance(value, Hashable):
            warn("Unhashable object {} of type {}".format(value, type(value)), RuntimeWarning)
            hash_value += hash(str(value))
        else:
            hash_value += hash(value)

    for key in sorted(kwargs.keys()):
        if not isinstance(kwargs[key], Hashable):
            warn("Unhashable object {} of type {}".format(kwargs[key], type(kwargs[key])), RuntimeWarning)

            hash_value += hash(key)
            hash_value += hash(str(kwargs[key]))
        else:
            hash_value += hash(str(key))
            hash_value += hash(kwargs[key])

    return hash_value


def cached(func):
    values = dict()
    doc_string = func.__doc__

    def cache_function(*args, **kwargs):
        string = __hash_arguments(args, kwargs)
        if string in values.keys():
            return values[string]
        else:
            value = func(*args, **kwargs)
            values[string] = value
            return value

    cache_function.__doc__ = doc_string
    return cache_function
