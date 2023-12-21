class ShiftCipher:
    @classmethod
    def encrypt(cls, plaintext, key):
        if not all([char.islower() or char.isspace() for char in plaintext]):
            raise ValueError("Plaintext should only consist of lowercase alphabets.")

        chars = []

        for char in plaintext:
            if char.isspace():
                chars.append(char)
            else:
                chars.append(chr((ord(char) - 97 + key) % 26 + 97))

        return "".join(chars)

    @classmethod
    def decrypt(cls, ciphertext, key):
        if not all([char.islower() or char.isspace() for char in ciphertext]):
            raise ValueError("Ciphertext should only consist of lowercase alphabets.")

        chars = []

        for char in ciphertext:
            if char.isspace():
                chars.append(char)
            else:
                chars.append(chr((ord(char) - 97 - key) % 26 + 97))

        return "".join(chars)

    @classmethod
    def attack(cls, ciphertext):
        res = []

        for key in range(26):
            res.append(cls.decrypt(ciphertext, key))

        return res


print("---SHIFT CIPHER---")
choice = -1

while choice != 4:
    print("\n1. Encrypt Text\n2. Decrypt Text.\n3. Mount an Attack.\n4. Quit.")
    choice = int(input("Enter choice: "))
    print()
    match choice:
        case 1:
            plaintext = input("Enter text to be encrypted: ")
            key = int(input("Enter key: "))
            ciphertext = ShiftCipher.encrypt(plaintext, key)
            print("Ciphered text:", ciphertext)
        case 2:
            ciphertext = input("Enter text to be decrypted: ")
            key = int(input("Enter key: "))
            plaintext = ShiftCipher.decrypt(ciphertext, key)
            print("Plaintext:", plaintext)
        case 3:
            ciphertext = input("Enter text to be cracked: ")
            for key in range(0, 26):
                print(f"Plaintext with key {key}:", ShiftCipher.decrypt(ciphertext, key))
        case 4:
            break
        case _:
            print("Enter a valid choice.")
