import stdio
import sys

# Accept k (int),c (float), epsilon (float) as command-line argument.
k = int(sys.argv[1])
c = float(sys.argv[2])
epsilon = float(sys.argv[3])

# Set t (our guess) to c.
t = c

# Repeat as long as
while abs(1 - c / t**k) > epsilon:
    t -= (t**k - c) / (k * t**(k - 1))

# Write t to standard output.
stdio.writeln(t)
