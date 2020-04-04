class VectorError(Exception):
    def __init__(self, message):
        self.message = message

class Vector:
    def __init__(self, *components):
        for arg in components:
            if not isinstance(arg, int) and not isinstance(arg, float):
                raise TypeError
        self.components = components
        self.dimensions = len(components)

    def __len__(self):
        sum = 0
        for c in self.components:
            sum += c * c
        return pow(sum, 1 / 2)

    def __getitem__(self, i):
        if i < self.dimensions:
            return self.components[i]
        else:
            raise IndexError

    def __repr__(self):
        return repr(self.components)

    def __add__(self, vector):
        if isinstance(vector, Vector):
            if self.dimensions == vector.dimensions:
                return Vector(*[a + b for (a, b) in zip(self.components, vector.components)])
            else:
                raise VectorError("Vectors have different dimensions.")
        else:
            raise TypeError

    def __sub__(self, vector):
        if isinstance(vector, Vector):
            if self.dimensions == vector.dimensions:
                return Vector(*[a - b for (a, b) in zip(self.components, vector.components)])
            else:
                raise VectorError("Vectors have different dimensions.")
        else:
            raise TypeError

    def __eq__(self, vector):
        if isinstance(vector, Vector):
            if self.dimensions == vector.dimensions:
                return self.components == vector.components
            else:
                return False
        else:
            raise TypeError

    def __mul__(self, obj):
        if isinstance(obj, Vector):
            if self.dimensions == obj.dimensions:
                return sum([a * b for (a, b) in zip(self.components, obj.components)])
            else:
                raise VectorError("Vectors have different dimensions.")
        if isinstance(obj, int) or isinstance(obj, float):
            return Vector(*[a * obj for a in self.components])
        else:
            raise TypeError