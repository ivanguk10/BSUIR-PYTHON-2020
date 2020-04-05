def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class T:
    def __init__(self):
        self.d = {'a': 1, 'b': 2, 'c': 'cc'}
        self.ll = [1, True, 'aa', '']
        self.s = 'ss'
        self.n = 42
        self.b = False
        self.bb = True
        self.null = ''
    pass


if __name__ == '__main__':
    temp1 = T()
    temp2 = T()
