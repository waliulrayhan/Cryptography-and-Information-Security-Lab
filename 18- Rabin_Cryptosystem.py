import random
import sympy

# Function to generate keys
def generate_keys(bits):
    # Generate two large primes p and q such that p, q ≡ 3 (mod 4)
    # Rabin Cryptosystem requires both p and q to be congruent to 3 modulo 4
    p = sympy.randprime(2**(bits-1), 2**bits)  # Generate random prime p of size bits
    while p % 4 != 3:  # Ensure that p ≡ 3 (mod 4)
        p = sympy.randprime(2**(bits-1), 2**bits)

    q = sympy.randprime(2**(bits-1), 2**bits)  # Generate random prime q of size bits
    while q % 4 != 3:  # Ensure that q ≡ 3 (mod 4)
        q = sympy.randprime(2**(bits-1), 2**bits)
    
    N = p * q  # N is the public key, N = p * q
    return (N, p, q)  # Return the public key (N) and private keys (p, q)

# Encryption function
def encrypt(public_key, message):
    N = public_key  # Get the public key N
    ciphertext = pow(message, 2, N)  # Encrypt the message m by squaring it modulo N (ciphertext = m^2 mod N)
    return ciphertext  # Return the ciphertext

# Extended Euclidean Algorithm to find modular inverses
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1  # Base case: gcd(a, b) = b, with coefficients 0 and 1
    gcd, x1, y1 = extended_gcd(b % a, a)  # Recursive step
    x = y1 - (b // a) * x1  # Update x
    y = x1  # Update y
    return gcd, x, y  # Return gcd and coefficients

# Modular square root using Tonelli-Shanks algorithm
def mod_sqrt(a, p):
    return pow(a, (p + 1) // 4, p)  # Return the modular square root of a modulo p (since p ≡ 3 (mod 4))

# Decryption function
def decrypt(private_key, ciphertext):
    p, q = private_key[1], private_key[2]  # Extract the private keys p and q
    N = p * q  # Compute N (same as in the public key)

    # Compute the square roots of the ciphertext modulo p and modulo q
    r_p = mod_sqrt(ciphertext, p)  # Compute square root modulo p
    r_q = mod_sqrt(ciphertext, q)  # Compute square root modulo q

    # Use the extended Euclidean algorithm to find coefficients for the Chinese Remainder Theorem
    _, y_p, y_q = extended_gcd(p, q)  # Find the coefficients y_p and y_q

    # Combine solutions using the Chinese Remainder Theorem
    # m1 and m2 are the potential solutions
    m1 = (r_p * q * y_q + r_q * p * y_p) % N  # Combine the roots for m1
    m2 = (r_p * q * y_q - r_q * p * y_p) % N  # Combine the roots for m2

    # The four possible roots of the ciphertext are m1, m2, -m1, -m2
    solutions = [(m1 % N), (-m1 % N), (m2 % N), (-m2 % N)]  # The four solutions modulo N
    
    return solutions  # Return the possible decrypted messages

# Example usage
if __name__ == "__main__":
    bits = 16  # Use a small bit size for this example; increase for better security
    public_key, p, q = generate_keys(bits)  # Generate the public and private keys
    private_key = (public_key, p, q)  # Create the private key tuple (public_key, p, q)

    message = 15  # Sample message (must be smaller than N)
    print(f"Original message: {message}")  # Print the original message

    ciphertext = encrypt(public_key, message)  # Encrypt the message
    print(f"Encrypted message: {ciphertext}")  # Print the encrypted message (ciphertext)

    possible_messages = decrypt(private_key, ciphertext)  # Decrypt the ciphertext
    print(f"Decrypted possible messages: {possible_messages}")  # Print the possible decrypted messages
