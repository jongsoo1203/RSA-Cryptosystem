import math


# A data type to represent the quadratic function ax^2 + bx + c, where a != 0.
class Quadratic:
    # Constructs a quadratic function given the coefficients a, b, and c.
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # Returns the coefficients of this quadratic function as a tuple.
    def coeffs(self):
        return self._a, self._b, self._c

    # Returns the value of this quadratic function at x.
    def __getitem__(self, x):
        return self._a * (x ** 2) + self._b * x + self._c

    # Returns the two roots of this quadratic function as a tuple, the first being (-b + sqrt(b^2
    # - 4ac)) / 2a and the second being (-b - sqrt(b^2 - 4ac)) / 2a.
    def roots(self):
        # Set quad for the insdie sqrt for readability and preventing from exceeding line limit.
        quad = self._b ** 2 - 4 * self._a * self._c
        root1 = (-self._b + math.sqrt(quad)) / (2 * self._a)
        root2 = (-self._b - math.sqrt(quad)) / (2 * self._a)
        return root1, root2

    # Returns the sum of the roots of this quadratic function.
    def sum(self):
        # Get a tuple of roots from roots() function.
        a = self.roots()
        return a[0] + a[1]

    # Returns the product of the roots of this quadratic function.
    def prod(self):
        # Get a tuple of roots from roots() function.
        a = self.roots()
        return a[0] * a[1]

    # Returns True if the quadratic functions self and other have the same sum and product of
    # roots, and False otherwise.
    def __eq__(self, other):
        return self.sum() == other.sum() and self.prod() == other.prod()

    # Returns a string representation of this quadratic function.
    def __str__(self):
        s = ''
        if self._a == 1:
            s += 'x^2'
        else:
            s += str(self._a) + 'x^2'
        if self._b == 0:
            pass
        elif self._b == 1:
            s += ' + x'
        elif self._b < 0:
            s += ' - ' + str(-self._b) + 'x'
        else:
            s += ' + ' + str(self._b) + 'x'
        if self._c == 0:
            pass
        elif self._c < 0:
            s += ' - ' + str(-self._c)
        else:
            s += ' + ' + str(self._c)
        return s


# Unit tests the data type.
def _main():
    import stdio

    q1 = Quadratic(1, -5, 6)
    q2 = Quadratic(1, -4, 0)
    q3 = Quadratic(3, -15, 18)
    stdio.writeln('q1          : ' + str(q1))
    stdio.writeln('q2          : ' + str(q2))
    stdio.writeln('q3          : ' + str(q3))
    stdio.writeln('q1.coeffs() : ' + str(q1.coeffs()))
    stdio.writeln('q2[5]       : ' + str(q2[5]))
    stdio.writeln('q3.roots()  : ' + str(q3.roots()))
    stdio.writeln('q3.sum()    : ' + str(q3.sum()))
    stdio.writeln('q3.prod()   : ' + str(q3.prod()))
    stdio.writeln('q1 == q2    : ' + str(q1 == q2))
    stdio.writeln('q1 == q3    : ' + str(q1 == q3))


if __name__ == '__main__':
    _main()
