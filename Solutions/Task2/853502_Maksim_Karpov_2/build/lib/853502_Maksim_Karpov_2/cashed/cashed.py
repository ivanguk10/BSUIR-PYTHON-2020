import json
import os.path


def cached(func):
    d = {}
    if os.path.exists("cashed.txt"):
        with open("cashed.txt") as f:
            d = json.load(f)

    def wrapped(*args, **kwargs):
        if d.get('{}'.format(args, kwargs)) is None:
            d['{}'.format(args, kwargs)] = func(*args, **kwargs)
        with open("cashed.txt", 'w') as f:
            json.dump(d, f)

        return d.get('{}'.format(args, kwargs))

    return wrapped


@cached
def sumator(n, a, b):
    return n + a + b


@cached
def struct(lst, a):
    return sum(lst) + a


print(struct([1, 2, 3, 4], 5))
