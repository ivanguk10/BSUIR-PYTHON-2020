class Cached:
    def __init__(self, func):
        self.cache = {}
        self.func = func

    def __call__(self, *args, **kwargs):
        n = "".join(str(args)).join(str(kwargs))
        if n in self.cache:
            print('Берем значение из кеша\t' + self.func.__name__)
            return self.cache[n]
        else:
            print('Новое значение функции\t' + self.func.__name__)
            result = self.func(*args)
            self.cache[n] = result
            return result


@Cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        fib1 = fib2 = 1
        while n > 2:
            fib1, fib2 = fib2, fib1 + fib2
            n -= 1
        return fib2


@Cached
def sum(*args):
    res = 0
    for num in args:
        res += num
    return res

'''
if __name__ == "__main__":
    # fib = Cached(fib)
    print(fib(5))
    print(fib(5))
    print(fib(7))
    print(sum(1, 2, 3, 4, 5))
    print(sum(1, 2, 3, 4, 5))
    print(sum(1, 2, 3, 3, 5))
'''
