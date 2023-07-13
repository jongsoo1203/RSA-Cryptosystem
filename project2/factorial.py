import stdio
import sys

# Accept n (int) as command-line argument.
n = int(sys.argv[1])

# Set result to 1.
result = 1

# Set output to the appropriate string based on value.
for i in range(2, n+1):
    # Set result to its current value times i.
    result *= i

# Write result to standard output.
stdio.writeln(result)
