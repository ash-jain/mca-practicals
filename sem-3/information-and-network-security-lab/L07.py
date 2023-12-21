import math

def euclids_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_prime(n):
    if n <= 1:
        return False
    elif n % 2 == 0:
        return True
    i = 3
    while (i * i) <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while euclids_algorithm(e, phi) != 1:
        e += 1

    d = pow(e, -1, phi)

    return (e, n), (d, n)

def encrypt(message, public_key):
    e, n = public_key
    ciphertext = [chr(pow(ord(char), e, n)) for char in message]
    return "".join(ciphertext)

def decrypt(ciphertext, private_key):
    d, n = private_key
    decryptedCiphertext = [chr(pow(ord(c), d, n)) for c in ciphertext]
    return "".join(decryptedCiphertext)

if __name__ == "__main__":
    p = 17
    q = 19

    public_key, private_key = generate_keys(p, q)

    plaintext = input("Enter plaintext: ")

    ciphertext = encrypt(plaintext, public_key)
    print(f"Encrypted message: {ciphertext}")

    decryptedCiphertext = decrypt(ciphertext, private_key)
    print(f"Decrypted message: {decryptedCiphertext}")
