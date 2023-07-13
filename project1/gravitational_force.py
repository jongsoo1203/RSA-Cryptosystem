import stdio
import sys

# Accept m1 (float), m2 (float), and r (float) as command-line arguments.
m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])

# Use scientific notation for the value of G (eg, 6.022e23 for 6.022 × 1023)
G = 6.674e-11

# Compute and write the value of gravitational force f.
f = G * m1 * m2 / r**2

# Write force to standard output.
stdio.writeln(f)
