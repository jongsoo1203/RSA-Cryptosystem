import math
import stdio
import sys


# A data type to represent a point in 2D space.
class Point:
    # Constructs a new point given its x and y coordinates.
    def __init__(self, x, y):
        self._x = x
        self._y = y

    # Returns the Euclidean distance between this point and other.
    def distanceTo(self, other):
        distance = math.sqrt((self._x - other._x) ** 2 + (self._y - other._y) ** 2)
        return distance

    # Return a string representation of this point.
    def __str__(self):
        return "(" + str(self._x) + ", " + str(self._y) + ")"


# Unit tests the data type (DO NOT EDIT).
def _main():
    x1, y1, x2, y2 = map(float, sys.argv[1:])
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    stdio.writeln('p1        = ' + str(p1))
    stdio.writeln('p2        = ' + str(p2))
    stdio.writeln('d(p1, p2) = ' + str(p1.distanceTo(p2)))


if __name__ == '__main__':
    _main()
