import stdio
import sys

# Accept n (int) as command-line argument.
n = int(sys.argv[1])

# Set a, b (the first two Fibonacci numbers) to 1, and i to 3.
a = b = 1
i = 3

# Repeat as long as i ≤ n:
while i <= n:
    # Exchange a and b with b and a + b
    a, b = b, a+b
    i += 1

# If you got here by exhausting the while loop, write b (nth Fibonacci number) as standard output.
stdio.writeln(b)
