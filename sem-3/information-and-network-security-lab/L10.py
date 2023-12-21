from random import choice

def euclid(m, n):
    if n == 0:
        return m
    else:
        r = m % n
        return euclid(n, r)

def extended_euclid(a, b):

    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1

    while r2 > 0:
        q = r1 // r2
        r = r1 - q * r2
        r1 = r2
        r2 = r
        s = s1 - q * s2
        s1 = s2
        s2 = s
        t = t1 - q * t2
        t1 = t2
        t2 = t

    if t1 < 0:
        t1 = t1 % a

    return (r1, t1)

p, q = list(map(int, input("Enter two large prime numbers: ").split())) # 823, 953
n = p * q
Pn = (p - 1) * (q - 1)

key = []

for i in range(2, Pn):
    gcd = euclid(Pn, i)
    if gcd == 1:
        key.append(i)

r, d = -1, -1
while r != 1:
    e = choice(key)
    r, d = extended_euclid(Pn, e)

print(f"Alice's Public Key: {e}")
print(f"Alice's Private Key: {d}")

M = int(input("Enter a message to be sent in numeric form: "))
S = (M ** d) % n

print(f"Alice's digital signature is: {S}")

M1 = (S ** e) % n

print(f"Bob verifies: {M1}")
 
if M == M1:
    print("Message is verified.")
else:
    print("Message is rejected.")
