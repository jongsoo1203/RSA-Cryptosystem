import rsa
import stdio
import sys


# Entry point.
def main():
    # Accept lo (int) and hi (int) as command-line arguments.
    lo = int(sys.argv[1])
    hi = int(sys.argv[2])

    # Get public/private keys as a tuple.
    a = rsa.keygen(lo, hi)

    # Write the three values in the tuple, separated by a space
    stdio.writeln(str(a[0]) + ' ' + str(a[1]) + ' ' + str(a[2]))


if __name__ == '__main__':
    main()
