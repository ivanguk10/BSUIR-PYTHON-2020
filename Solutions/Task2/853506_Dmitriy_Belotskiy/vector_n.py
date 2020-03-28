"""Класс “n мерный вектор”. У этого класса должны быть определены все
естественные для вектора операции - сложение, вычитание, умножение на
константу и скалярное произведение, сравнение на равенство. Кроме этого
должны быть операции вычисления длины, получение элемента по индексу,
а также строковое представление."""


class Vector():
    def __init__(self, *args):
        args = list(args)
        self.size = len(args)
        self.values = args

    def __str__(self):
        return self.values.__str__()

    def __add__(self, other):
        if self.size == other.size:
            i = 0
            args = []
            while i < self.size:
                args.append(self.values[i] + other.values[i])
                i += 1
            return Vector(*args)

    def __sub__(self, other):
        if self.size == other.size:
            i = 0
            args = []
            while i < self.size:
                args.append(self.values[i] - other.values[i])
                i += 1
            return Vector(*args)

    def __mul__(self, other):
        if isinstance(other, int):
            i = 0
            args = []
            while i < self.size:
                args.append(self.values[i] * other)
                i += 1
            return Vector(*args)
        else:
            if self.size == other.size:
                i = 0
                res = 0
                while i < self.size:
                    res += (self.values[i] * other.values[i])
                    i += 1
                return res
            else:
                raise ArithmeticError

    def __getitem__(self, key):
        if 0 <= key < self.size:
            return self.values[key]

    def __setitem__(self, key, value):
        if 0 <= key < self.size:
            self.values[key] = value

    def __eq__(self, other):
        if self.size == other.size:
            i = 0
            while i < self.size:
                if(self.values[i] != other.values[i]):
                    return False
                i += 1
        return True

    def __len__(self):
        return self.values.__len__()

'''
if __name__ == '__main__':
    v1 = Vector(10, 5, 3)
    v2 = Vector(2, 3, 3)
    v3 = v1 + v2
    print(v3)
    v3 = v1 * v2
    print(v3)
    v3 = v1 * 6
    print(v3)
    print(v3[2])
    print(v1==v2)
    print(v1 == v1)
    print(len(v1))
'''
