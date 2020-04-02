def singleton(class_):
    """Singleton decorator function

    Arguments:
        class_: singleton class
    """
    instance = {}

    def get_instance(*args, **kwargs):

        if class_ not in instance:
            instance[class_] = class_(*args, **kwargs)

        return instance[class_]

    return get_instance


class Singleton(type):
    """Singleton class

    Metaclass to provide Singleton pattern
    to custom Python class.
    """
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class MyClass(metaclass=Singleton):

    def __init__(self, o):
        self.o = o

    def bark(self):
        print('gav')

    def von(self):
        print(self.o)


@singleton
class MyClassWithDec:
    def __init__(self, o):
        self.o = o

    def bark(self):
        print('gav')

    def von(self):
        print(self.o)
