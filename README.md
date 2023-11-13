# RSA-Cryptosystem

The RSA (Rivest-Shamir-Adleman) cryptosystem is widely used for secure communication in browsers, bank ATM machines,
credit card machines, mobile phones, smart cards, and operating systems. It works by manipulating integers. To thwart
eavesdroppers, the RSA cryptosystem must manipulate huge integers (hundreds of digits), which is naturally supported by
the int data type in Python. Your task is to implement a library that supports core functions needed for developing the RSA
cryptosystem and implement programs for encrypting and decrypting messages using RSA.

### RSA.py

The RSA public-key cryptosystem involves three integers n, e, and d that satisfy certain mathematical properties. The public key (n; e) is made public on the Internet, while the private key (n; d) is only known to Bob.
If Alice wants to send Bob a message x 2 [0; n), she encrypts it using the function
__E(x) = y = x^e mod n;__
Decrypts by
__D(y) = y^d mod n;__

### Keygen.py

accepts lo (int) and hi (int) as command-line arguments,
generates public/private keys (n; e; d), and writes the keys to standard output, separated by a space.

### encrypt.py

accepts the public-key n (int) and e (int) as
command-line arguments and a message to encrypt from standard input, encrypts each character in the message, and writes
its fixed-width binary representation to standard output.

### decrypt.py

accepts the private-key n (int) and d (int) as
command-line arguments and a message to decrypt (produced by encrypt.py) from standard input, decrypts each character
(represented as a fixed-width binary sequence) in the message, and writes the decrypted character to standard output.
