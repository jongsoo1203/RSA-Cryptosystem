import stdio
import sys

# Accept  n1 (int), n2 (int), and p (float), as command-line arguments.
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
p = float(sys.argv[3])

# for the clearity
q = 1-p

# Compute and write the values of p1 and p2, separated by a space.
p1 = (1 - (p / q)**n2) / (1 - (p / q)**(n1 + n2))
p2 = (1 - (q / p)**n1) / (1 - (q / p)**(n1 + n2))

# Write the probability to standard output.
stdio.writeln(str(p1) + " " + str(p2))
