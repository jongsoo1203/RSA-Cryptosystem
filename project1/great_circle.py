import math
import stdio
import sys

# Accept x1 (float), y1 (float), x2 (float), and y2 (float) as command-line arguments.
x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

# Write down the equation for the distance between two points on Earth.
# Use math.radians() to convert degrees to radians.
d = 6359.83 * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) +
                        math.cos(math.radians(x1)) * math.cos(math.radians(x2))
                        * math.cos(math.radians(y1 - y2)))

# Write distance to standard output.
stdio.writeln(d)
