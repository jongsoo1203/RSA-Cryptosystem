import math
import stdio
import sys

# Accept T1 (float), n1 (float), and n2 (float) as command-line arguments.
T1 = float(sys.argv[1])
n1 = float(sys.argv[2])
n2 = float(sys.argv[3])

# Compute and write the value of the angle of refraction θ2 in degrees.
# To calculate the arcsine of a number, use math.asin().
T2 = math.degrees(math.asin(n1 * math.sin(math.radians(T1)) / n2))

# Write the angle to standard output.
stdio.writeln(T2)
