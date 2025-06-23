import random
import math
import time

# Prime number utilities
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_prime(start, end):
    while True:
        p = random.randint(start, end)
        if is_prime(p):
            return p

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# RSA Key Generation
def generate_keys(start=100, end=300):
    p = generate_prime(start, end)
    q = generate_prime(start, end)
    while q == p:
        q = generate_prime(start, end)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)
    d = modinv(e, phi)
    return (e, d, n)

# RSA Encryption/Decryption
def encrypt(message, e, n):
    return pow(message, e, n)

def decrypt(ciphertext, d, n):
    return pow(ciphertext, d, n)

# naive attack (factorization)
def factorize_n(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    return None, None

def attack(e, n, ciphertext):
    start_time = time.time()
    p, q = factorize_n(n)
    if not p or not q:
        return None, None
    phi = (p - 1) * (q - 1)
    d = modinv(e, phi)
    plaintext = pow(ciphertext, d, n)
    elapsed = time.time() - start_time
    return plaintext, elapsed
