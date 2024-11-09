# myenv\Scripts\activate  # For Windows

# # Import necessary modules for RSA encryption
# from Crypto.PublicKey import RSA  # This imports the RSA module from PyCryptodome for generating RSA keys.
# from Crypto.Cipher import PKCS1_OAEP  # This imports the PKCS1_OAEP cipher module for RSA encryption/decryption.
# from Crypto.Random import get_random_bytes  # This module is used to generate random bytes for secure operations.
# import base64  # Base64 is used for encoding and decoding binary data in ASCII text.

# # Generate RSA key pair (private and public key)
# key = RSA.generate(2048)  # This generates a new RSA key pair with a 2048-bit key size.

# # Extract public and private keys
# private_key = key.export_key()  # Export the private key in PEM format (used for decryption).
# public_key = key.publickey().export_key()  # Export the public key in PEM format (used for encryption).

# # Print the private and public keys
# print("Private Key: ", private_key.decode('utf-8'))  # Decode and print the private key as a UTF-8 string.
# print("Public Key: ", public_key.decode('utf-8'))  # Decode and print the public key as a UTF-8 string.

# # Load the public and private keys (from string for this example)
# public_key_obj = RSA.import_key(public_key)  # Import the public key from the previously exported string.
# private_key_obj = RSA.import_key(private_key)  # Import the private key from the previously exported string.

# # Create RSA cipher object with the public key for encryption
# cipher_rsa = PKCS1_OAEP.new(public_key_obj)  # Create a cipher object using the public key with OAEP padding (optimal asymmetric encryption padding).

# # Input plaintext
# plaintext = input("Enter the plaintext: ")  # Take the message from the user that needs to be encrypted.

# # Encrypt the plaintext
# ciphertext = cipher_rsa.encrypt(plaintext.encode('utf-8'))  # Encrypt the plaintext (converted to bytes) using the RSA cipher object.
# print("Ciphertext (Base64 Encoded):", base64.b64encode(ciphertext).decode('utf-8'))  # Print the ciphertext in Base64 encoding to make it readable.

# # Decryption Part
# # Create RSA cipher object with the private key for decryption
# cipher_rsa_decrypt = PKCS1_OAEP.new(private_key_obj)  # Create a cipher object using the private key for decryption with OAEP padding.

# # Decrypt the ciphertext
# decryptedtext = cipher_rsa_decrypt.decrypt(ciphertext)  # Decrypt the ciphertext using the RSA cipher object.
# print("Decrypted text:", decryptedtext.decode('utf-8'))  # Decode the decrypted bytes back into a string and print it.


from sympy import randprime
import random
import math

# Generate two random prime numbers
prime1 = randprime(2, 10**2)  # Generates a random prime number in the range (2, 100)
prime2 = randprime(2, 10**2)  # Generates another random prime number in the range (2, 100)

# n = p * q where p and q are prime numbers (the product n will be used in public and private key calculations)
n = prime1 * prime2

# phi(n) = (p-1) * (q-1) for ElGamal-like key generation
phi_n = (prime1 - 1) * (prime2 - 1)

# Generating the public key (e) such that gcd(e, phi(n)) = 1
e = randprime(1, phi_n)  # Public exponent e, chosen randomly in the range (1, phi(n))
while math.gcd(phi_n, e) != 1:  # Check if gcd(e, phi(n)) = 1 (necessary for e to be valid)
    e = random.randint(1, phi_n)  # If not, choose another e

# Generating the private key (d) using the modular inverse of e
d = pow(e, -1, phi_n)  # Calculate d, which is the modular inverse of e modulo phi(n)

# Set the plaintext to be encrypted
plaintext = input("Enter the plaintext message: ")  # Take the message from the user that needs to be encrypted

# Encryption Algorithm
i = 0  # Initialize counter
ciphertext = ""  # String to store the encrypted message
length = len(plaintext)  # Length of the plaintext message
while i < length:
    value = ord(plaintext[i])  # Get the ASCII value of the ith character
    num = pow(value, e) % n  # Encrypt the character (m^e) mod n
    ciphertext += chr(num + 32)  # Add 32 to get the correct ASCII value for encryption
    i += 1  # Move to the next character

# Print the encrypted message
print("The cipher text of the plaintext:", plaintext, "is:", ciphertext)

# Decryption Algorithm
i = 0  # Initialize counter
decrypted_text = ""  # String to store the decrypted message
length = len(ciphertext)  # Length of the ciphertext message
while i < length:
    value = ord(ciphertext[i]) - 32  # Subtract 32 to get the original numerical value
    num = pow(value, d) % n  # Decrypt the character (c^d) mod n
    decrypted_text += chr(num)  # Convert the decrypted number back to the original character
    i += 1  # Move to the next character

# Print the decrypted message
print("The plaintext of the ciphertext:", decrypted_text)
