# myenv\Scripts\activate  # For Windows

# Import necessary modules
import base64  # Base64 is used to encode the ciphertext into a readable string format.
from Crypto.Cipher import DES  # The DES module is imported from the pycryptodome library for encryption.
from Crypto.Random import get_random_bytes  # This is used to generate random bytes for the DES key.

# Input plaintext
plaintext = input("Enter the plaintext: ");  # Takes input from the user (plaintext message to encrypt).

# Padding the plaintext
while len(plaintext) % 8 != 0:  # DES works with 64-bit blocks (8 bytes). If the plaintext is not a multiple of 8, it needs to be padded.
    plaintext = plaintext + " "  # Adds a space character to the plaintext until its length becomes a multiple of 8.

# Create a random key
key = get_random_bytes(8)  # Generates a random 8-byte (64-bit) key for encryption. DES requires a 56-bit key, but it's represented as 8 bytes.

# Create model of the cipher
des = DES.new(key, DES.MODE_ECB)  # Creates a DES cipher object using the key and specifying the mode of operation.
                                  # DES.MODE_ECB stands for Electronic Codebook, one of the simplest modes.
                                  # In this mode, each block is encrypted independently.

# Encryption Part
ciphertext = des.encrypt(plaintext.encode('utf-8'))  # Encrypts the padded plaintext using the DES cipher object.
                                                     # The plaintext is first encoded into bytes using UTF-8 before encryption.

print("Ciphertext: ", base64.b64encode(ciphertext))  # The ciphertext (encrypted data) is outputted.
                                                     # Base64 encoding is used to convert binary ciphertext into a readable string.
                                                     # This step is necessary because the ciphertext is not printable in its raw form.

# Decryption Part
decryptedtext = des.decrypt(ciphertext)  # The DES cipher object is used to decrypt the ciphertext back into the original plaintext.

print("Decrypted text : ", decryptedtext.decode())  # The decrypted data is decoded back from bytes to a string.
                                                   # UTF-8 decoding is used to return it to its original string form.
