import functools
import sympy

cry_len = 2
dec_len = 3

def solution(arr, mods):
    res = 0
    prod = functools.reduce(lambda acc, elem: acc * elem, mods)

    for el, mod in zip(arr, mods):
        p = prod // mod
        res = res + el * p * mul_inv(p, mod)

    res = res % prod

    return res


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1

    if b == 1:
        return 1

    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0

    if x1 < 0:
        x1 += b0

    return x1


def generate_primes():
    min = 27 ** (cry_len // 2)
    max = 27 ** (dec_len // 2 + 1)
    prime1 = sympy.randprime(min, max)
    prime2 = sympy.randprime(min, max)

    while prime1 == prime2 or prime1 % 4 != 3 or prime2 % 4 != 3 or \
            not (27 ** dec_len > prime1 * prime2 > 27 ** cry_len):
        prime1 = sympy.randprime(min, max)
        prime2 = sympy.randprime(min, max)

    return prime1, prime2


def get_solutions(res, m):
    for i in range(m):
        if i * i % m == res:
            return i, -i

    return None, None


class Rabin:
    def __init__(self):
        self.__prime1, self.__prime2 = generate_primes()
        self.__pub_key = self.__prime1 * self.__prime2
        self.__messages = []
        self.__cry_map = {}

    def __extended_euclid(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, y, x = self.__extended_euclid(b % a, a)
            return gcd, x - (b // a) * y, y

    def __return_ascii(self, ch):
        if ch == ' ':
            return 0
        else:
            return ord(ch) - ord('A') + 1

    def check_message(self, message):
        if len(message) == 0:
                raise ValueError("Length of message should be greater than 0")
        for ch in message:
            if ch not in " abcdefghijklmnopqrstuvwxyz":
                raise ValueError("Message should contain only lower case letters and spaces")

    def encrypter(self, message):
        self.check_message(message)
        if message not in self.__messages:
            self.__messages.append(message)
        encrypted_msg = ""

        for i in range(0, len(message), cry_len):
            for idx in range(cry_len):
                if i + idx >= len(message):
                    message += ' '
            m = 0
            for idx in range(cry_len):
                m += self.__return_ascii(message[i + idx]) * (27 ** (cry_len - idx - 1))
            c = (m ** 2) % self.__pub_key

            current_str = ""
            p = dec_len - 1
            while c and p >= 0:
                if c < 27 ** p:
                    current_str += " "
                    p -= 1
                    continue

                q = c // (27 ** p)

                if q == 0:
                    current_str += " "

                else:
                    current_str += str(chr(q + ord('a') - 1))

                c -= (27 ** p) * q
                p -= 1

            while len(current_str) < dec_len:
                current_str += " "

            encrypted_msg += current_str

        return encrypted_msg

    def __decode(self):
        messages = []
        good_messages = []
        for index in self.__cry_map:
            new_messages = []
            for el in self.__cry_map[index]:
                new_messages.append(el)
                messages.append(el)
                for ms in messages:
                    new_messages.append(ms + el)
                messages.extend(new_messages.copy())

        for ms in messages:
            ms = ms.rstrip(' ')
            if ms in self.__messages and ms not in good_messages:
                good_messages.append(ms)

        return good_messages

    def __one_solution(self, sol_p, sol_n, mod, index):
        while sol_p < 27 ** cry_len:
            c_sol_p = sol_p
            current_str = ""
            p = cry_len - 1
            while c_sol_p and p >= 0:
                if c_sol_p < 27 ** p:
                    current_str += " "
                    p -= 1
                    continue

                q = c_sol_p // (27 ** p)

                current_str += str(chr(q + ord('a') - 1))

                c_sol_p -= 27 ** p * q
                p -= 1
            while len(current_str) < cry_len:
                current_str += " "
            self.__cry_map[index // 3].append(current_str)

            sol_p += mod

        sol_n += mod

        while sol_n < 27 ** cry_len:
            c_sol_n = sol_n
            current_str = ""
            p = cry_len - 1
            while c_sol_n and p >= 0:
                if c_sol_n < 27 ** p:
                    current_str += " "
                    p -= 1
                    continue

                q = c_sol_n // (27 ** p)

                current_str += str(chr(q + ord('a') - 1))

                c_sol_n -= 27 ** p * q
                p -= 1
            while len(current_str) < cry_len:
                current_str += " "
            self.__cry_map[index // 3].append(current_str)

            sol_n += mod


    def decrypter(self, c_message):
        for i in range(0, len(c_message), dec_len):
            ch = 0
            for p in range(dec_len):
                ch += self.__return_ascii(c_message[i + p]) * (27 ** (dec_len - p - 1))

            s1_p, s1_n = get_solutions(ch % self.__prime1, self.__prime1)
            s2_p, s2_n = get_solutions(ch % self.__prime2, self.__prime2)

            self.__cry_map[i // 3] = []

            if s1_p is None:
                self.__one_solution(s2_p, s2_n, self.__prime1, i // 3)
                continue
            if s2_p is None:
                self.__one_solution(s1_p, s1_n, self.__prime2, i // 3)
                continue

            r = solution([s1_p, s2_p], [self.__prime1, self.__prime2])
            neg_r = solution([s1_n, s2_p], [self.__prime1, self.__prime2])
            s = solution([s1_p, s2_n], [self.__prime1, self.__prime2])
            neg_s = solution([s1_n, s2_n], [self.__prime1, self.__prime2])

            if r < 27 ** cry_len:
                current_str = ""
                p = cry_len - 1
                while r and p >= 0:
                    if r < 27 ** p:
                        current_str += " "
                        p -= 1
                        continue

                    q = r // (27 ** p)

                    current_str += str(chr(q + ord('a') - 1))

                    r -= 27 ** p * q
                    p -= 1
                while len(current_str) < cry_len:
                    current_str += " "
                self.__cry_map[i // 3].append(current_str)

            if neg_r < 27 ** cry_len:
                current_str = ""
                p = cry_len - 1
                while neg_r and p >= 0:
                    if neg_r < 27 ** p:
                        current_str += " "
                        p -= 1
                        continue

                    q = neg_r // (27 ** p)

                    current_str += str(chr(q + ord('a') - 1))

                    neg_r -= 27 ** p * q
                    p -= 1
                while len(current_str) < cry_len:
                    current_str += " "
                self.__cry_map[i // 3].append(current_str)

            if s < 27 ** cry_len:
                current_str = ""
                p = cry_len - 1
                while s and p >= 0:
                    if s < 27 ** p:
                        current_str += " "
                        p -= 1
                        continue

                    q = s // (27 ** p)

                    current_str += str(chr(q + ord('a') - 1))

                    s -= 27 ** p * q
                    p -= 1
                while len(current_str) < cry_len:
                    current_str += " "
                self.__cry_map[i // 3].append(current_str)

            if neg_s < 27 ** cry_len:
                current_str = ""
                p = cry_len - 1
                while neg_s and p >= 0:
                    if neg_s < 27 ** p:
                        current_str += " "
                        p -= 1
                        continue

                    q = neg_s // (27 ** p)

                    current_str += str(chr(q + ord('a') - 1))

                    neg_s -= 27 ** p * q
                    p -= 1
                while len(current_str) < cry_len:
                    current_str += " "
                self.__cry_map[i // 3].append(current_str)

        return self.__decode()


rb = Rabin()
ciphertext = rb.encrypter(input('Enter message to encrypt: '))
print(f"Encrypted message: {ciphertext}")
decryptedText = rb.decrypter(ciphertext)
print(f"Decrypted message: {decryptedText}")
