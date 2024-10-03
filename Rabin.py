import random
import sympy

# Function to generate keys
def generate_keys(bits):
    # Generate two large primes p and q such that p, q ≡ 3 (mod 4)
    p = sympy.randprime(2**(bits-1), 2**bits)
    while p % 4 != 3:
        p = sympy.randprime(2**(bits-1), 2**bits)

    q = sympy.randprime(2**(bits-1), 2**bits)
    while q % 4 != 3:
        q = sympy.randprime(2**(bits-1), 2**bits)
    
    N = p * q  # Public key
    return (N, p, q)

# Encryption function
def encrypt(public_key, message):
    N = public_key
    ciphertext = pow(message, 2, N)
    return ciphertext

# Extended Euclidean Algorithm
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Modular square root
def mod_sqrt(a, p):
    return pow(a, (p + 1) // 4, p)

# Decryption function
def decrypt(private_key, ciphertext):
    p, q = private_key[1], private_key[2]
    N = p * q

    # Compute square roots mod p and mod q
    r_p = mod_sqrt(ciphertext, p)
    r_q = mod_sqrt(ciphertext, q)

    # Use the extended Euclidean algorithm to find y_p and y_q
    _, y_p, y_q = extended_gcd(p, q)

    # Combine solutions using the Chinese remainder theorem
    m1 = (r_p * q * y_q + r_q * p * y_p) % N
    m2 = (r_p * q * y_q - r_q * p * y_p) % N

    # The four possible roots are m1, m2, -m1, -m2
    solutions = [(m1 % N), (-m1 % N), (m2 % N), (-m2 % N)]
    
    return solutions

# Example usage
if __name__ == "__main__":
    bits = 16  # Use small bit size for this example, increase for better security
    public_key, p, q = generate_keys(bits)
    private_key = (public_key, p, q)

    message = 42  # Sample message (must be smaller than N)
    print(f"Original message: {message}")

    ciphertext = encrypt(public_key, message)
    print(f"Encrypted message: {ciphertext}")

    possible_messages = decrypt(private_key, ciphertext)
    print(f"Decrypted possible messages: {possible_messages}")
