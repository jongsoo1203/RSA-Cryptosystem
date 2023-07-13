import stdio
import sys

# Accept n (int) as command-line argument.
n = int(sys.argv[1])

# Repeat i for each [2, n]
for i in range(2, n+1):
    # Set total to 0
    total = 0
    # Repeat j for each [1, i // 2]
    for j in range(1, i // 2 + 1):
        # If i is dividable by j
        if i % j == 0:
            # Increment total by j.
            total += j
    # If total is equaled to i.
    if total == i:
        # Write the perfect number as standard output.
        stdio.writeln(i)
