import rsa
import stdio
import sys


# Entry point.
def main():
    # Accept private-key n (int) and d (int) as command-line arguments.
    n = int(sys.argv[1])
    d = int(sys.argv[2])

    # Get the number of bits per character (call it width).
    width = rsa.bitLength(n)
    # Accept message (binary string generated by encrypt.py) from standard input.
    message = stdio.readAll()
    # Assuming l is the length of message, for i ∈ [0, l − 1) and in increments of width:
    for i in range(0, len(message) - 1, width):
        # Set s to substring of message from i to i + width (exclusive).
        s = message[i: i + width]
        # Set y to decimal representation of the binary string s.
        y = rsa.bin2dec(s)
        # Decrypt y
        a = rsa.decrypt(y, n, d)

        # Write the character corresponding to the decrypted value,
        # obtained using the built-in function chr().
        stdio.write(chr(a))


if __name__ == '__main__':
    main()
