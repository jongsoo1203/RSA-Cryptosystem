import stdio
import sys

# Accept n (int) and k (int) as command-line argument.
n = int(sys.argv[1])
k = int(sys.argv[2])

# Set total to 0.
total = 0

# Repeat i for each i ∈ [1, n]
for i in range(1, n+1):
    # Increment total by
    total += i**k

# Write total to standard output.
stdio.writeln(total)
