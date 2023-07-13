# A library of color-related functions.

from color import Color
import stdio
import sys


# Returns the luminance of the Color c.
def luminance(c):
    r = c.getRed()
    g = c.getGreen()
    b = c.getBlue()
    if r == g and r == b:
        return r
    return 0.299 * r + 0.587 * g + 0.114 * b


# Returns the grayscale equivalent of Color c.
def toGray(c):
    y = int(round(luminance(c)))
    gray = Color(y, y, y)
    return gray


# Returns True if Color c1 is compatible with Color c2, and False otherwise.
def areCompatible(c1, c2):
    return abs(luminance(c1) - luminance(c2)) >= 128.0


# Unit tests the library.
def _main():
    r1 = int(sys.argv[1])
    g1 = int(sys.argv[2])
    b1 = int(sys.argv[3])
    r2 = int(sys.argv[4])
    g2 = int(sys.argv[5])
    b2 = int(sys.argv[6])
    c1 = Color(r1, g1, b1)
    c2 = Color(r2, g2, b2)
    stdio.writeln(str(c1) + ' compatible with ' + str(c2) + '? ' + str(areCompatible(c1, c2)))


if __name__ == '__main__':
    _main()
