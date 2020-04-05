class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TestClass(metaclass=MetaSingleton):
    pass


if __name__ == "__main__":
    test1 = TestClass()
    test2 = TestClass()
    print(test1, test2)
