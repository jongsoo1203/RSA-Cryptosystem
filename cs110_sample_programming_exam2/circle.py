import math


class Circle:
    # Constructs a circle of radius r centered at (h, k); when no arguments are given, the circle
    # is a unit circle centered at the origin.
    def __init__(self, h=0, k=0, r=1):
        self._r = r
        self._h = h
        self._k = k

    # Returns the area of this circle.
    def area(self):
        area = math.pi * self._r ** 2
        return area

    # Returns the circumference of this circle.
    def circumference(self):
        circumf = math.pi * 2 * self._r
        return circumf

    # Returns True if this circle contains the point (x, y) and False otherwise.
    def contains(self, x, y):
        return (self._h + x) ** 2 + (self._k + y) ** 2 <= self._r ** 2

    # Returns a new circle whose center is the same as this circle, but with radius r.
    def scale(self, r):
        return Circle(self._h, self._k, r)

    # Returns the Euclidean distance between the centers of this circle and other.
    def distanceTo(self, other):
        Euelidean = math.sqrt((self._h - other._h) ** 2 + (self._k - other._k) ** 2)
        return Euelidean

    # Returns True if this circle is the same as other (ie, they have the same centers and radii)
    # and False otherwise.
    def __eq__(self, other):
        return self._r == other._r and self._h == other._h and self._k == other._k

    # Returns True if this circle's area is smaller than other's area and False otherwise.
    def __lt__(self, other):
        return self.area() < other.area()

    # Returns a string representation of this circle.
    def __str__(self):
        return "(" + str(self._h) + ", " + str(self._k) + ", " + str(self._r) + ")"


# Unit tests the data type.
def _main():
    import stdio

    c = Circle()
    d = Circle(1, 1, 2)
    stdio.writeln('c                 = ' + str(c))
    stdio.writeln('d                 = ' + str(d))
    stdio.writeln('c.area()          = ' + str(c.area()))
    stdio.writeln('c.circumference() = ' + str(c.circumference()))
    stdio.writeln('c.contains(1, 1)  = ' + str(c.contains(1, 1)))
    stdio.writeln('c.scale(2)        = ' + str(c.scale(2)))
    stdio.writeln('c.distanceTo(d)   = ' + str(c.distanceTo(d)))
    stdio.writeln('c == d or c == c  = ' + str(c == d or c == c))
    stdio.writeln('d < c             = ' + str(d < c))


if __name__ == '__main__':
    _main()
