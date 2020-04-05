class ExtendedTuple(tuple):
    def __new__(cls, *args):
        obj = super(ExtendedTuple, cls).__new__(cls, args)
        obj._from_base_class = type(obj) == ExtendedTuple
        return obj
    pass


def cached(fn):
    cache = []

    def wrapped(*args):
        arguments = ExtendedTuple(fn.__name__, *args)
        if arguments not in cache:
            arguments.res = fn(*args)
            cache.append(arguments)
        return cache[cache.index(arguments)].res

    return wrapped




