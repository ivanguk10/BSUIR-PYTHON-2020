import functools


def cached(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        else:
            print("receive cached value...")
        return cache[args]
    return wrapper


@cached
def my_sum(x, y):
    return x + y


if __name__ == "__main__":
    print(my_sum.__name__)
    print(my_sum(2, 3))
    print(my_sum(2, 3))
    print(my_sum(5, 6))

