import math
import stdio
import sys


# Entry point (DO NOT EDIT).
def main():
    x = math.radians(float(sys.argv[1]))
    stdio.writeln(_sin(x))


# Returns sin(x) calculated using the formula: sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
def _sin(x):
    # Set total to 0.0, term to 1.0, sign to 1, and i to 1.
    total = 0.0
    term = 1.0
    sign = 1
    i = 1

    while total != total + term:
        # Repeat until convergence...

        # Set term to its previous value times x divided by i.
        term *= x / i

        # If i is odd, increment total by sign times term, and toggle (ie, negate) sign.
        if i % 2 != 0:
            total += sign * term
            sign = -sign
        # Increment i by 1.
        i += 1

    # Return total.
    return total


if __name__ == '__main__':
    main()
