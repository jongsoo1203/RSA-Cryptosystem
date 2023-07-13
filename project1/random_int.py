import stdio
import stdrandom
import sys

# Accept a (int) and b (int) as command-line arguments.
a = int(sys.argv[1])
b = int(sys.argv[2])

# Set r to a random integer between a and b, obtained by calling stdrandom.uniformInt().
r = stdrandom.uniformInt(a, b)

# Write r to standard output.
stdio.writeln(r)
