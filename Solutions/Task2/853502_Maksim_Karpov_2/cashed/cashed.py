import functools


def cached(function):
    func_dict = {}

    @functools.wraps(function)
    def function_counter(*args, **kwargs):
        key = args + tuple(sorted(kwargs.items()))
        if key not in func_dict:
            func_dict[key] = function(*args, **kwargs)
        return func_dict[key]

    return function_counter

@cached
def multiply(a, b):
    print("Функция вызвана")
    return a*b


if __name__ == "__main__":
    print(multiply(3, 4))
    print(multiply(3, 4))