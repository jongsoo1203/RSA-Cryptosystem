import stdio
import sys

# Accept p (int) and q (int) as command-line argument.
p = int(sys.argv[1])
q = int(sys.argv[2])

# Repeat as long as
while p % q != 0:
    # Exchange p and q with q and p mod q.
    p, q = q, p % q

# If you got here by exhausting the while loop, write q to standard output.
stdio.writeln(q)
