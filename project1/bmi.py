import stdio
import sys

# Accept weight (float) and height (float) as command-line arguments.
weight = float(sys.argv[1])
height = float(sys.argv[2])

# Set bmi to weight divided by square of height.
bmi = weight / height**2

# Write bmi to standard output.
stdio.writeln(bmi)
