class Vector:
    def __init__(self, *values):
        self.coordinates = list(values)
        self.check_values()

    def check_values(self):
        for value in self.coordinates:
            if not isinstance(value, (int, float)):
                raise ValueError('Coordinates of the vector must be numbers.')

    def __len__(self):
        return len(self.coordinates)

    def __getitem__(self, index):
        if index < -len(self) or index >= len(self):
            raise IndexError("Index is out of range.")
        return self.coordinates[index]

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Can't add.")
        result = Vector()
        for i in range(len(self)):
            result.coordinates.append(self[i] + other[i])
        return result

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Can't subtract.")
        result = Vector()
        for i in range(len(self)):
            result.coordinates.append(self[i] - other[i])
        return result

    def __str__(self):
        return "({0})".format(', '.join(str(coordinate) for coordinate in self.coordinates))

    def __mul__(self, other):
        result = Vector()
        if isinstance(other, (int, float)):
            for i in range(len(self)):
                result.coordinates.append(self[i] * other)
            return result
        elif isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Can't multiply.")
            return sum(self[i] * other[i] for i in range(len(self)))
        else:
            raise TypeError("Can't multiply by the type.")

    def __eq__(self, other):
        if len(self) != len(other):
            raise ValueError("Can't compare.")
        return Vector.length(self-other) == 0

    @staticmethod
    def length(vector):
        result = sum(vector[i] ** 2 for i in range(vector.__len__()))
        return result ** (1 / 2)


if __name__ == '__main__':
    a = Vector(20, 30, 40, 50, 60)
    b = Vector(2, 3, 4, 5, 6)
    c = Vector(6, 8)
    d = Vector(1, 1)
    # d = Vector("ghj", 2, 4)
    print(a+b)
    print(a-b)
    print(a*b)
    print(a*5)
    print(a[3])
    print(Vector.length(c))
    print(a == b)
    print(a == a)

