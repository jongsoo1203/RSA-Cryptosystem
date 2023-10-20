import stdarray
import stdio
import stdrandom
import sys


# Generates and returns the public/private keys as a tuple (n, e, d). Prime numbers p and q.
# needed to generate the keys are picked from the interval [lo, hi).
def keygen(lo, hi):
    # Get a list of primes from the interval [lo, hi).
    # Set a as a list that samples two distinct prime numbers from list a.
    a = _sample(_primes(lo, hi), 2)
    # Define p and q
    p = a[0]
    q = a[1]

    # Set n and m to p * q and (p − 1) * (q − 1), respectively.
    n, m = p * q, (p - 1) * (q - 1)

    # Get a list of primes from the interval [2, m).
    z = _primes(2, m)

    # Choose a random prime e from the list such that e does not divide m.
    e = _choice(z)
    # While it devides, set another e.
    while m % e == 0:
        e = _choice(z)

    # Find a d ∈ [1, m) such that e * d mod m == 1.
    for d in range(1, m):
        if (e * d) % m == 1:
            break

    # Return the tuple (n, e, d)
    return (n, e, d)


# Encrypts x (int) using the public key (n, e) and returns the encrypted value.
def encrypt(x, n, e):
    return x ** e % n


# Decrypts y (int) using the private key (n, d) and returns the decrypted value.
def decrypt(y, n, d):
    return y ** d % n


# Returns the least number of bits needed to represent n.
def bitLength(n):
    return len(bin(n)) - 2


# Returns the binary representation of n expressed in decimal, having the given width, and padded
# with leading zeros.
def dec2bin(n, width):
    return format(n, '0%db' % (width))


# Returns the decimal representation of n expressed in binary.
def bin2dec(n):
    return int(n, 2)


# Returns a list of primes from the interval [lo, hi).
def _primes(lo, hi):
    # Create an empty list.
    a = []

    # For each p ∈ [lo, hi) and for i ∈ [lo, hi).
    for p in range(lo, hi):
        if p == 0 or p == 1:
            continue
        for i in range(2, p):

            # If i divides p, p is not prime number. Break.
            if p % i == 0:
                break

        # Else, add the number in the list a.
        else:
            a.append(p)

    # Return the list
    return a


# Returns a list containing a random sample (without replacement) of k items from the list a.
def _sample(a, k):
    # Copy list a to b
    b = a[:]

    # Shuffle the first k elements of b
    for i in range(k):
        r = stdrandom.uniformInt(i, len(b))
        b[i], b[r] = b[r], b[i]

    # Return a list containing the first k elements of b.
    return b[:k]


# Returns a random item from the list a.
def _choice(a):
    # Get list r ∈ [0, l), where l is the number of elements in a
    r = _primes(0, len(a))
    # Set a random number.
    random = stdrandom.uniformInt(0, len(r))

    # Return the element in r at the index random
    return r[random]


# Unit tests the library [DO NOT EDIT].
def _main():
    x = ord(sys.argv[1])
    n, e, d = keygen(25, 100)
    encrypted = encrypt(x, n, e)
    stdio.writef('encrypt(%c) = %d\n', x, encrypted)
    decrypted = decrypt(encrypted, n, d)
    stdio.writef('decrypt(%d) = %c\n', encrypted, decrypted)
    width = bitLength(x)
    stdio.writef('bitLength(%d) = %d\n', x, width)
    xBinary = dec2bin(x, width)
    stdio.writef('dec2bin(%d) = %s\n', x, xBinary)
    stdio.writef('bin2dec(%s) = %d\n', xBinary, bin2dec(xBinary))


if __name__ == '__main__':
    _main()
