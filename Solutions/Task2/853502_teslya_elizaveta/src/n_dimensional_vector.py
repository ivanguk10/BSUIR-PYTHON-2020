class Nd_Vector(object):
    """Class to work with vector

    Class represents methods to calculate the operations on vectors.

    Attributes:
        dimension (int): vector rank
        vector (list): values of every dimension
    """

    def __init__(self, dimension=None, vector=None):
        """NVector constructor

        Raise:
            TypeError: if rank is not integer.

        Args:
            dimension (int): set rank of constructed NVector.
            vector (list or str): list of int or float values to construct NVector,
                                    string of int or float values in format ('value1 value2 ...').
        """

        if dimension is not None:

            if isinstance(dimension, int):
                self.dimension = dimension
                self.vector = [0 for i in range(dimension)]

            else:

                raise TypeError

        elif vector is not None:

            if isinstance(vector, list):

                self.dimension = 0
                self.vector = []

                for i in vector:

                    if isinstance(i, int):

                        self.vector.append(float(i))
                        self.dimension += 1

                    elif isinstance(i, float):

                        self.vector.append(i)
                        self.dimension += 1

                    else:

                        raise TypeError

            elif isinstance(vector, str):

                self.dimension = 0
                self.vector = []

                for i in vector.split():

                    self.vector.append(float(i))
                    self.dimension += 1

            else:

                raise TypeError

        else:
            raise NVectorError('Arguments req')

    def add(self, other):
        """Sum of two vectors.

        Vectors must nave the same dimensions.

        Arguments:
            other (Nd_Vector): vector with the same dimension.

        Return:
            Nd_Vector(result_vector): result of sum
        """
        if not isinstance(other, Nd_Vector):
            raise NVectorError('Argument is invalid')

        if self.dimension != other.dimension:
            raise NVectorError('Not equal dimensions')

        result_vector = [xi + yi for xi, yi in zip(self.vector, other.vector)]
        return Nd_Vector(vector=result_vector)

    def __add__(self, other):
        return self.add(other)

    def __iadd__(self, other):
        self.vector = self.add(other).vector
        return self

    def sub(self, other):
        """Subtraction of two vectors.

         Vectors must nave the same dimensions.

        Arguments:
            other (Nd_Vector): vector with the same dimension.

        Return:
             Nd_Vector(result_vector): result of subtraction.
        """
        if not isinstance(other, Nd_Vector):
            raise NVectorError('Argument is invalid')

        if self.dimension != other.dimension:
            raise NVectorError('Not equal dimensions')

        result_vector = [xi - yi for xi, yi in zip(self.vector, other.vector)]
        return Nd_Vector(vector=result_vector)

    def __sub__(self, other):
        return self.sub(other)

    def __isub__(self, other):
        self.vector = self.sub(other).vector
        return self

    def mul(self, num):
        """Multiple number and vector.

        Arguments:
            num (float or int): number to multiple.

        Return:
            Nd_Vector(result_vector): result of multiplication.
        """

        if not isinstance(num, int) and not isinstance(num, float):
            raise NVectorError('Argument is invalid')

        result_vector = [num * xi for xi in self.vector]
        return Nd_Vector(vector=result_vector)

    def __mul__(self, other):
        return self.mul(other)

    def __imul__(self, other):
        self.vector = self.mul(other).vector
        return self

    def div(self, num):
        """Division vector and number.

        Arguments:
            num (float or int): number to division.

        Return:
            Nd_Vector(result_vector): result of division.
        """
        if not isinstance(num, int) and not isinstance(num, float):
            raise NVectorError('Argument is invalid')

        if num == 0.0:
            raise ZeroDivisionError

        result_vector = [xi / num for xi in self.vector]
        return Nd_Vector(vector=result_vector)

    def __truediv__(self, other):
        return self.div(other)

    def __itruediv__(self, other):
        self.vector = self.div(other).vector
        return self

    def floordiv(self, num):
        """Floor division vector and number.

        Arguments:
            num (float or int): number to floor division.

        Return:
            Nd_Vector(result_vector): result of floor division.
        """
        if not isinstance(num, int) and not isinstance(num, float):
            raise NVectorError('Argument is invalid')

        if num == 0.0:
            raise ZeroDivisionError

        result_vector = [xi // num for xi in self.vector]
        return Nd_Vector(vector=result_vector)

    def __floordiv__(self, other):
        return self.floordiv(other)

    def __ifloordiv__(self, other):
        self.vector = self.floordiv(other).vector
        return self

    def matmul(self,  other):
        """Multiplication of two vectors.

        Vectors must nave the same dimensions.

        Arguments:
            other (Nd_Vector): vector with the same dimension.

        Return:
            Nd_Vector(result_vector): result of multiplication.
        """
        if not isinstance(other, Nd_Vector):
            raise NVectorError('Argument is invalid')

        if self.dimension != other.dimension:
            raise NVectorError('Not equal dimensions')

        result_vector = [xi * yi for xi, yi in zip(self.vector, other.vector)]
        return Nd_Vector(vector=result_vector)

    def __matmul__(self, other):
        return self.matmul(other)

    def __imatmul__(self, other):
        self.vector = self.matmul(other).vector
        return self

    def __setitem__(self, key, value):
        self.vector[key] = value

    def __getitem__(self, key):
        return self.vector[key]

    def __neg__(self):
        result_vector = [-xi for xi in self.vector]
        return Nd_Vector(vector=result_vector)

    def __len__(self):
        return self.dimension

    def __delitem__(self, key):
        del self.vector[key]
        return self

    def __delslice__(self, i, j):
        del self.vector[i:j]
        return self

    def pow(self, power):
        """Exponentiation vector.

        Arguments:
            power (float or int): indicator.

        Return:
            Nd_Vector(result_vector): result of pow.
        Raise:
            NVector: invalid type of argument.
        """
        if not isinstance(power, int) and not isinstance(power, float):
            raise NVectorError('Argument is invalid')

        result_vector = [xi ** power for xi in self.vector]
        return Nd_Vector(vector=result_vector)

    def __pow__(self, power, modulo=None):
        return self.pow(power)

    def __ipow__(self, other):
        self.vector = self.pow(other).vector
        return self

    def equal(self, other):
        """Vector comparision

        Compare object NVector elements to other Nd_Vector elements. Return
        True if all elements of other Nd_vector is respectively equal, otherwise
        False.

        Args:
            other (Nd_Vector): NVector to compare.
        Returns:
            result (bool): result of comparison.
        """
        if not isinstance(other, Nd_Vector):
            raise NVectorError('Argument is invalid')

        if self.dimension != other.dimension:
            return False

        for xi, yi in zip(self.vector, other.vector):
            if xi != yi:
                return False
        return True

    def __eq__(self, other):
        return self.equal(other)

    def __ne__(self, other):
        return not self.equal(other)

    def __repr__(self):
        return 'Nd_vector({})'.format(self.vector)

    def __str__(self):
        return ' '.join(str(x) for x in self.vector)

    def norm(self):
        """Norm of vector

        Return euclidean norm.

        Returns:
            result (float): norm of vector.
        """

        norm = 0.0

        for xi in self.vector:
            norm += xi ** 2.0
        return norm ** 0.5

    def __abs__(self):
        return self.norm()

    def __iter__(self):
        return self.vector.__iter__()


class NVectorError(Exception):
    """Class to represent NVector error

    NVectorError represents error occurred during operations
    with Nd_Vector.

    Attributes:
        message(str): represents error message.
    """

    def __init__(self, message='Error'):
        """NVectorError constructor

        Arguments:
             message (str): represents error message. Default: 'Error'.
        """
        self.message = message
