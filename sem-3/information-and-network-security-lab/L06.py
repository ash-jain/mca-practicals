import random

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def generate_random_prime(start, end):
    while True:
        candidate = random.randint(start, end)
        if is_prime(candidate):
            return candidate

def is_primitive_root(g, p):
    factors = prime_factors(p - 1)
    for factor in factors:
        if pow(g, (p - 1) // factor, p) == 1:
            return False
    return True

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def find_primitive_root(p):
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    return None

p = generate_random_prime(1000, 10000)
g = find_primitive_root(p)

print(f"Random prime generated: {p}.")
print(f"Its primitive root: {g}.")

alicesSecretKey = random.randint(1, 100)
bobsSecretKey = random.randint(1, 100)

print(f"Alice's secret key: {alicesSecretKey}.")
print(f"Bob's secret key: {bobsSecretKey}.")

alicesPublicKey = (g ** alicesSecretKey) % p
bobsPublicKey = (g ** bobsSecretKey) % p

print(f"Alice's public key: {alicesPublicKey}.")
print(f"Bob's public key: {bobsPublicKey}.")

aliceReceives = bobsPublicKey ** alicesSecretKey % p
bobReceives = alicesPublicKey ** bobsSecretKey % p

print(f"Alice Receives: {aliceReceives}.")
print(f"Bob Receives: {bobReceives}.")

if aliceReceives == bobReceives:
    print(f"Keys Validated.")
else:
    raise SystemError()
