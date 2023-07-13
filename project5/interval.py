import stdio
import sys


# A data type to represent a 1-dimensional interval [lbound, rbound].
class Interval:
    # Construct a new interval given its lower and upper bounds.
    def __init__(self, lbound, rbound):
        self._lbound = lbound
        self._rbound = rbound

    # Returns the lower bound of this interval.
    def lower(self):
        return self._lbound

    # Returns the upper bound of this interval.
    def upper(self):
        return self._rbound

    # Returns True if this interval contains the point x, and False otherwise.
    def contains(self, x):
        if self._lbound <= x <= self._rbound:
            return True
        return False

    # Returns True if this interval intersects other, and False otherwise.
    def intersects(self, other):
        # Imagine two intervals self._(x1, y1) and other._(x2, y2).
        # if x2 is less or equal to y1, it means x2 is in (x1, y1).
        # Also, if x1 is less or equal to y2, it means y2 is in (x1, y1).
        if other._lbound <= self._rbound and self._lbound <= other._rbound:
            return True
        return False

    # Returns a string repesentation of this interval.
    def __str__(self):
        return "[" + str(self._lbound) + ", " + str(self._rbound) + "]"


# Unit tests the data type (DO NOT EDIT).
def _main():
    x = float(sys.argv[1])
    intervals = []
    while not stdio.isEmpty():
        lbound = stdio.readFloat()
        rbound = stdio.readFloat()
        intervals += [Interval(lbound, rbound)]
    for i in range(len(intervals)):
        if intervals[i].contains(x):
            stdio.writef('%s contains %f\n', intervals[i], x)
    for i in range(len(intervals)):
        for j in range(i + 1, len(intervals)):
            if intervals[i].intersects(intervals[j]):
                stdio.writef('%s intersects %s\n', intervals[i], intervals[j])


if __name__ == '__main__':
    _main()
