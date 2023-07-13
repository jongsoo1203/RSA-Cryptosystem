import stdio
import sys

# Accept n (int) as command-line argument.
n = int(sys.argv[1])

# Set a as 1 to begin
a = 1

# Use multiple while loops in order to satisfy the conditions of ramanujan's number
while a * a * a <= n:
    # For the range, set b = a + 1
    b = a + 1
    while b * b * b <= (n - a * a * a):
        # For the range, set c = a + 1
        c = a + 1
        while (a + 1) ** 3 <= c * c * c <= n:
            # For the range, set d = c + 1
            d = c + 1
            while d * d * d <= (n - c * c * c):
                # While a, b, c, and d satisfy all the ranges.
                # If the equation satisfies, then print the outputs.
                if a * a * a + b * b * b == c * c * c + d * d * d:
                    stdio.writeln(str(a * a * a + b * b * b) + " = " + str(a) + "^3 + " + str(b)
                                  + "^3 = " + str(c) + "^3 + " + str(d) + "^3")
                # When the ranges are not satisfied, make the numbers increment by 1.
                d += 1
            c += 1
        b += 1
    a += 1
