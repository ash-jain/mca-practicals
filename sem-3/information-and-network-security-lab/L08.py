def find_primitive_root(p):
    for g in range(2, p):
        powers = set()
        for i in range(1, p):
            powers.add(pow(g, i, p))
        if len(powers) == p - 1:
            return g
    return find_primitive_root(int(input(f"Primitive element for prime number {p} does not exist, Choose another: ")))

def encryptMessage(iterable, p, generator, sender_private_key, receiver_public_key):

    res = []

    for element in iterable:
        y1 = pow(generator, sender_private_key, p)
        y2 = (ord(element) * pow(receiver_public_key, sender_private_key, p)) % p
        res.append(chr(y1) + chr(y2))

    return "".join(res)

def decryptmessage(iterable, p, receiver_private_key):

    res = []

    for i in range(0, len(iterable), 2):
        term = pow(ord(iterable[i]), receiver_private_key, p)
        decrypted_char = (ord(iterable[i + 1]) * term) % p
        res.append(chr(decrypted_char))

    return "".join(res)


if __name__ == "__main__":
    p = int(input("Input prime number: "))
    generator = find_primitive_root(p)

    bobs_private_key = int(input("Enter Bob's private key: "))
    bobs_public_key = pow(generator, bobs_private_key, p)

    alices_private_key = int(input("Enter Alice's private key: "))

    plaintext = input("Enter plaintext: ")
    ciphertext = encryptMessage(plaintext, p, generator, alices_private_key, bobs_public_key)

    print(f"Ciphertext is: {ciphertext}")

    decryptedText = decryptmessage(ciphertext, p, bobs_private_key)

    print(f"Decrypted Text is: {plaintext}")