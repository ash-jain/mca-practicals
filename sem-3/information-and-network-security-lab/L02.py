class PlayfairCipher:
    def __init__(self, key):
        self.table = [["" for _ in range(5)] for _ in range(5)]
        self.lookup = dict()

        i, j = 0, 0

        for char in key:
            self.table[i][j] = char
            self.lookup[char] = (i, j)
            j += 1
            if j == 5:
                i += 1
                j = 0

        for char in "abcdefghiklmnopqrstuvwxyz":
            if char in self.lookup:
                continue
            self.table[i][j] = char
            self.lookup[char] = (i, j)
            j += 1
            if j == 5:
                i += 1
                j = 0

    def partition(self, text):
        partition = []
        text = "".join(text.split(" "))

        i = 0
        while i < len(text):
            if i + 1 < len(text) and text[i] != text[i + 1]:
                partition.append(text[i] + text[i + 1])
                i += 2
            elif i + 1 < len(text) or i == len(text) - 1:
                partition.append(text[i] + "x")
                i += 1

        return partition

    def encrypt(self, text):
        text = self.partition(text)
        res = []

        for chars in text:
            i1, j1 = self.lookup[chars[0]]
            i2, j2 = self.lookup[chars[1]]

            if i1 == i2:
                res.append(self.table[i1][(j1 + 1) % 5] + self.table[i2][(j2 + 1) % 5])
            elif j1 == j2:
                res.append(self.table[j1 + 1] + self.table[j2 + 1])
            else:
                res.append(self.table[i1][j2] + self.table[i2][j1])

        return res


key, plaintext = "charles", "meet me at the bridge"
pf = PlayfairCipher(key)
ciphertext = pf.encrypt(plaintext)
print(f"Plaintext: \"{plaintext}\", Key: \"{key}\".")
print("Ciphertext:", ciphertext)
