import rsa
import stdio
import sys


# Entry point.
def main():
    # Accept public-key n (int) and e (int) as command-line arguments.
    n = int(sys.argv[1])
    e = int(sys.argv[2])

    # Get the number of bits per character (call it width) needed for encryption,
    # ie, number of bits needed to encode n.
    width = rsa.bitLength(n)
    # Accept message to encrypt from standard input.
    message = stdio.readAll()

    # Use the built-in function ord() to turn each character c in message into an integer x.
    for i in range(0, len(message)):
        x = ord(message[i])
        # Encrypt x.
        a = rsa.encrypt(x, n, e)

        # Write the encrypted value as a width-long binary string.
        stdio.write(rsa.dec2bin(a, width))

    # Write a newline character.
    stdio.writeln()


if __name__ == '__main__':
    main()
