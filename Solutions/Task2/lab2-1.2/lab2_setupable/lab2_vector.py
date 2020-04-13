
class Vector:
    def __init__(self, *args):
        self._data_ = []
        self._length_ = 0
        for argument in args:
            self._data_.append(int(argument))
            self._length_ += 1

    def __getitem__(self, item):
        if self._length_ - 1 < item:
            raise ReferenceError("Index out of vector!")
        else:
            return self._data_[item]

    def __len__(self):
        return self._length_

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*[self._data_[index] * other for index in range(self._length_)])
        else:
            raise TypeError("Unsupported operand type(s) for -: \'Vector\' and \'{}\'".format((type(other)).__name__))

    def __eq__(self, other):
        if isinstance(other, Vector) and len(other) == self._length_:
            for index in range(self._length_):
                if self._data_[index] != other[index]:
                    return False
            else:
                return True
        return False

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*[self._data_[index] + other for index in range(self._length_)])
        elif isinstance(other, Vector) and len(other) == self._length_:
            return Vector(*[self._data_[index] + other[index] for index in range(self._length_)])
        raise TypeError("Unsupported operand type(s) for -: \'Vector\' and \'{}\'!".format((type(other)).__name__))

    def __sub__(self, other):
        if isinstance(other, int):
            return Vector(*[self._data_[index] - other for index in range(self._length_)])
        elif isinstance(other, Vector) and len(other) == self._length_:
            return Vector(*[self._data_[index] - other[index] for index in range(self._length_)])
        raise TypeError("Unsupported operand type(s) for -: \'Vector\' and \'{}\'".format((type(other)).__name__))

    def __str__(self):
        return str(self._data_)

    def scalar_multiply(self, other):
        if not isinstance(other, Vector):
            raise TypeError("An other - attribute must be Vector-type, but received \'{}\'".format(
                (type(other)).__name__))
        elif len(other) != self._length_:
            raise AttributeError("The other - vector length must be the same as the multiplied vector")
        else:
            result = 0
            for index in range(self._length_):
                result += self._data_[index] * other[index]
            return result

