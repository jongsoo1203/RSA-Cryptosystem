import math
import stdio


# Entry point.
def main():
    # Initialize ETA, RHO, T, and R to appropriate values
    ETA = 9.135 * (10 ** -4)
    RHD = 0.5 * (10 ** -6)
    T = 297
    R = 8.31457

    # Calculate var as the sum of the squares of the n displacements
    # (each converted from pixels to meters) read from standard input.
    var = 0.0
    n = 0
    while not stdio.isEmpty():
        pixels = stdio.readFloat()
        meters = pixels * 0.175 * (10 ** -6)
        var += (meters ** 2)
        n += 1

    # Divide var by 2 * n.
    var = var / (2 * n)
    # Estimate Boltzmann’s constant as 6 * math.pi * var * ETA * RHO / T.
    K_B = 6 * math.pi * var * ETA * RHD / T
    # Estimate Avogadro’s constant as R / k
    K_A = R / K_B
    # Write to standard output the two constants in scientific notation
    # (using the format string ’%e’) and separated by a space.
    stdio.writef('%e %e\n', K_B, K_A)


if __name__ == '__main__':
    main()
