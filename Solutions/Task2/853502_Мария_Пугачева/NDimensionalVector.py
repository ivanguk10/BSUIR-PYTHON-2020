from numbers import Number


class NDimensionalVector:
    def __init__(self, *args):
        self.vector = [*args]

    def __add__(self, other):
        min_range = min(len(self.vector), len(other.vector))
        max_vector = self if other.vector.count == min_range else other
        result = [x + y for (x, y) in zip(self.vector, other.vector)]
        result.extend(max_vector[min_range:])

        return NDimensionalVector(*result)

    def __sub__(self, other):
        min_range = min(len(self.vector), len(other.vector))
        max_range = max(len(self.vector), len(other.vector))
        min_vector = self if self.vector.count == min_range else other
        result = [x - y for (x, y) in zip(self.vector, other.vector)]
        for i in range(min_range, max_range):
            result.append(0 - min_vector[i])

        return NDimensionalVector(*result)

    def __mul__(self, other):
        if other is Number:
            result = map(lambda x: x * other, self.vector)
        else:
            result = [x * y for (x, y) in zip(self.vector, other.vector)]
        return NDimensionalVector(*result)

    def __eq__(self, other):
        return self.vector.__eq__(other.vector)

    def __len__(self):
        return len(self.vector)

    def __getitem__(self, item):
        return self.vector[item]

    def __str__(self):
        return str(self.vector)

    pass


if __name__ == '__main__':
    vec1 = NDimensionalVector(1, 2, 3, 4, 5)
    vec2 = NDimensionalVector(2, 3, 4, 5, 6, 7, 8, 9)
    vec3 = NDimensionalVector(2, 3, 5, 6, 7, 8, 9)
    vec4 = NDimensionalVector()

    print(vec1[3])
    print(vec1 + vec3)
    print(vec4 + vec3)

    print(vec1 != vec2)


