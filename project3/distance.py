import math
import stdio
import sys

# Accept n (int) as command-line argument.
n = int(sys.argv[1])

# Accept n floats from standard input and store them in a list x.
x = []
for i in range(n):
    x += [stdio.readFloat()]

# Accept n floats from standard input and store them in a list y.
y = []
for i in range(n):
    y += [stdio.readFloat()]

# Set distance to 0.0.
distance = 0.0

# Compute the squared Euclidean distance between x and y.
for i in range(n):
    # Add square of (x[i] - y[i]) to distance.
    distance += (x[i] - y[i]) ** 2

# Set distance to the square root of itself.
distance = (math.sqrt(distance))

# Write distance to standard output.
stdio.writeln(distance)
