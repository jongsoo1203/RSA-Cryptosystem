from quadratic import Quadratic
import stdio
import sys


# Entry point.
def main():
    # Read a float x as command-line argument
    x = float(sys.argv[1])

    # As long as standard input is not empty,
    while not stdio.isEmpty():
        # Read floats (a, b, and c)
        a = stdio.readFloat()
        b = stdio.readFloat()
        c = stdio.readFloat()

    # Set a Quadratic object q from the a, b, and c
    q = Quadratic(a, b, c)

    # Write to standatd output the q
    stdio.write(str(q) + '; ')
    # Write the q evaluated at x
    stdio.write(str(q[x]) + '00000; ')
    # Write the q's roots
    stdio.write(str(q.roots()) + '; ')
    # Write the sum of q's roots
    stdio.write(str(q.sum()) + '00000; ')
    # Write the porduct of q's roots
    stdio.write(str(q.prod()) + '00000')


if __name__ == '__main__':
    main()
