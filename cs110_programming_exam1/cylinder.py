import math
import stdio
import sys

# accept all float
r = float(sys.argv[1])
h = float(sys.argv[2])

# Write standard outputs of Surface areas and Volume.
stdio.writeln('S = ' + str(2 * math.pi * r * (r + h)))
stdio.writeln('V = ' + str(math.pi * (r ** 2) * h))
