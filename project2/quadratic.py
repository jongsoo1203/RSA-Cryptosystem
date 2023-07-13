import math
import stdio
import sys

# Accept a (float), b (float), and c (float) as command-line arguments.
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a == 0:
    # If a is 0, write the message "Value of a must not be 0" to standard output.
    stdio.writeln("Value of a must not be 0")
else:
    # Compute discriminant (b^2 - 4ac).
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        # If discriminant is negative, write the message "Value of discriminant must not be
        # negative" to standard output.
        stdio.writeln("Value of discriminant must not be negative")
    else:
        # Compute the two roots of the quadratic equation ax^2 + bx + c = 0.
        root1 = (-b + (b**2 - 4 * a * c)**(1/2)) / 2 * a
        root2 = (-b - (b**2 - 4 * a * c)**(1/2)) / 2 * a

        # Write the two roots to standard output, separated by a space.
        stdio.writeln(f"{root1} {root2}")
