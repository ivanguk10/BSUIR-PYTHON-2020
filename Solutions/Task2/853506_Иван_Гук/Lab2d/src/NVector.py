class NVector:
    def __init__(self, rank=None, array=None, string=None):
        if rank is not None:
            if isinstance(rank, int):
                self.rank = rank
                self.vector = (0 for i in range(rank))
            else:
                raise TypeError('Rank must be integer')

        elif array is not None:
            if isinstance(array, list):
                self.vector = list()
                self.rank = 0
                for num in array:
                    if isinstance(num, float) or isinstance(num, int):
                        self.vector.append(float(num))
                        self.rank += 1
                    else:
                        raise TypeError('Array must be from floats')
            else:
                raise TypeError('Array must be list')

        elif string is not None:
            if isinstance(string, str):
                self.vector = list()
                self.rank = 0
                for num in string.split():
                    self.vector.append(float(num))
                    self.rank += 1
            else:
                raise TypeError('Rank must be integer')

    def add(self, other):
        if self.rank != other.rank:
            raise NVectorError
        else:
            new_vector = list()
            for xi, yi in zip(other, self):
                new_vector.append(xi + yi)
            return NVector(array=new_vector)

    def sub(self, other):
        if self.rank != other.rank:
            raise NVectorError
        else:
            new_vector = list()
            for xi, yi in zip(self, other):
                new_vector.append(xi - yi)
            return NVector(array=new_vector)

    def mul(self, scalar):
        new_vector = list()
        for xi in self:
            new_vector.append(xi * scalar)
        return NVector(array=new_vector)

    def div(self, scalar):
        if scalar == 0.0:
            raise ZeroDivisionError
        else:
            new_vector = list()
            for xi in self:
                new_vector.append(xi / scalar)
            return NVector(array=new_vector)

    def matmul(self, other):
        if self.rank != other.rank:
            raise NVectorError
        else:
            dot_product = 0.0
            for xi, yi in zip(other, self):
                dot_product += xi * yi
            return dot_product

    def equal(self, other):
        if self.rank != other.rank:
            raise NVectorError
        else:
            for xi, yi in zip(self, other):
                if xi != yi:
                    return False
            return True

    def norm(self):
        norm = 0.0
        for xi in self.vector:
            norm += xi ** 2
        return norm ** 0.5

    def __len__(self):
        return self.rank

    def __str__(self):
        return ', '.join(str(i) for i in self.vector)

    def __repr__(self):
        string_vector = '['
        for xi in self:
            string_vector += '{}, '.format(xi)
        string_vector = string_vector[:-2]
        string_vector += ']'

        return string_vector

    def __getitem__(self, item):
        return self.vector[item]

    def __setitem__(self, key, value):
        self.vector[key] = value

    def __add__(self, other):
        return self.add(other)

    def __iadd__(self, other):
        self.vector = self.add(other).vector
        return self

    def __sub__(self, other):
        return self.sub(other)

    def __isub__(self, other):
        self.vector = self.sub(other).vector
        return self

    def __mul__(self, scalar):
        return self.mul(scalar)

    def __imul__(self, scalar):
        self.vector = self.mul(scalar).vector
        return self

    def __truediv__(self, scalar):
        return self.div(scalar)

    def __idiv__(self, scalar):
        self.vector = self.div(scalar).vector
        return self

    def __matmul__(self, other):
        return self.matmul(other)

    def __eq__(self, other):
        return self.equal(other)

    def __ne__(self, other):
        return ~self.equal(other)

    def __abs__(self):
        return self.norm()

    def __iter__(self):
        return self.vector.__iter__()


class NVectorError(Exception):
    def __init__(self, message='Error'):
        self.message = message
