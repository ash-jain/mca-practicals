class LSFRCipher:
    def __init__(self, seed, connectors):
        self.key, self.keyLength = self.genKey(seed, connectors)

    def genKey(self, seed, connectors):
        state = list([int(char) for char in seed])
        states = set()
        bits = []

        while tuple(state) not in states:
            states.add(tuple(state))

            newBit = state[connectors[0]] ^ state[connectors[1]]

            bits.append(state[-1])

            for i in range(len(state) - 1, 0, -1):
                state[i] = state[i - 1]

            state[0] = newBit

        bits.append(state[-1])

        key = 0

        for i in range(len(bits)):
            key += bits[i] * (2 ** (len(bits) - i - 1))

        return key, len(bits)

    def encryptAndDecrypt(self, text):
        cipherText = []

        for i in range(0, len(text), self.keyLength):
            cipherText.append(
                int(text[i : i + self.keyLength].ljust(self.keyLength, "0"), 2)
                ^ self.key
            )

        return "".join([bin(element)[2:].zfill(16) for element in cipherText])


seed, connectors = '0110', [0, 3]
print(f"Seed: {seed}, Connectors: {connectors}.")
cipher = LSFRCipher(seed, connectors)
print(f"Key: {cipher.key}, {bin(cipher.key)}.")
plaintext = "01100101011000101110110001111010"
print(f"Plaintext: {plaintext}.")
cipherText = cipher.encryptAndDecrypt(plaintext)
print(f"Ciphertext: {cipherText}.")
cipherTextDecrypted = cipher.encryptAndDecrypt(cipherText)
print(f"Ciphertext Decrypted: {cipherTextDecrypted}.")
