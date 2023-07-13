import math
import stdio
import sys

# Accept g (float) and t (float) as command-line arguments.
g = float(sys.argv[1])
t = float(sys.argv[2])

# Compute and write the value of p.
p = math.exp(-g * t)

# Write the probablity to standard output.
stdio.writeln(p)
