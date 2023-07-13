import stdio
import stdrandom
import sys

# Accept n (int) as command-line arguments.
n = int(sys.argv[1])

# Use stdrandom.uniformInt() with suitable arguments to simulate a single roll of an n-sided die.
n1 = stdrandom.uniformInt(1, n+1)
n2 = stdrandom.uniformInt(1, n+1)

# Write the sum of the numbers rolled
stdio.writeln(n1 + n2)
