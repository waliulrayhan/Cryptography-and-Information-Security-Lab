import random
import sympy
from sympy import mod_inverse

# Function to generate ElGamal keys
def generate_keys(bits):
    # Generate a large prime p
    p = sympy.randprime(2**(bits-1), 2**bits)
    g = random.randint(2, p-2)  # Generator g, such that 1 < g < p-1

    # Private key x (randomly chosen from [1, p-2])
    x = random.randint(1, p-2)

    # Public key h = g^x mod p
    h = pow(g, x, p)

    # Public key (p, g, h) and private key x
    return (p, g, h), x

# Function to encrypt a message using the ElGamal cryptosystem
def encrypt(public_key, message):
    p, g, h = public_key

    # Random value k (chosen for each encryption, from [1, p-2])
    k = random.randint(1, p-2)

    # Calculate the two parts of the ciphertext
    c1 = pow(g, k, p)  # c1 = g^k mod p
    c2 = (message * pow(h, k, p)) % p  # c2 = m * h^k mod p

    # Ciphertext is (c1, c2)
    return c1, c2

# Function to decrypt the ciphertext using the ElGamal cryptosystem
def decrypt(private_key, public_key, ciphertext):
    p, g, h = public_key
    c1, c2 = ciphertext
    x = private_key

    # Compute the shared secret: s = c1^x mod p
    s = pow(c1, x, p)

    # Compute the inverse of s modulo p
    s_inv = mod_inverse(s, p)

    # Recover the original message: m = c2 * s_inv mod p
    message = (c2 * s_inv) % p

    return message

# Example usage
if __name__ == "__main__":
    bits = 16  # Use small bit size for this example, increase for better security
    public_key, private_key = generate_keys(bits)

    print(f"Public Key (p, g, h): {public_key}")
    print(f"Private Key (x): {private_key}")

    # Sample message (must be smaller than p)
    message = 42
    print(f"Original message: {message}")

    # Encrypt the message
    ciphertext = encrypt(public_key, message)
    print(f"Ciphertext: {ciphertext}")

    # Decrypt the ciphertext
    decrypted_message = decrypt(private_key, public_key, ciphertext)
    print(f"Decrypted message: {decrypted_message}")
