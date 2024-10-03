from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
import base64

# Generate RSA key pair (private and public key)
key = RSA.generate(2048)

# Extract public and private keys
private_key = key.export_key()
public_key = key.publickey().export_key()

print("Private Key: ", private_key.decode('utf-8'))
print("Public Key: ", public_key.decode('utf-8'))

# Save the keys into files (optional)
with open("private.pem", "wb") as private_file:
    private_file.write(private_key)

with open("public.pem", "wb") as public_file:
    public_file.write(public_key)

# Load the public and private keys (from string for this example)
public_key_obj = RSA.import_key(public_key)
private_key_obj = RSA.import_key(private_key)

# Create RSA cipher object with the public key for encryption
cipher_rsa = PKCS1_OAEP.new(public_key_obj)

# Input plaintext
plaintext = input("Enter the plaintext: ")

# Encrypt the plaintext
ciphertext = cipher_rsa.encrypt(plaintext.encode('utf-8'))
print("Ciphertext (Base64 Encoded):", base64.b64encode(ciphertext).decode('utf-8'))

# Decryption Part
# Create RSA cipher object with the private key for decryption
cipher_rsa_decrypt = PKCS1_OAEP.new(private_key_obj)

# Decrypt the ciphertext
decryptedtext = cipher_rsa_decrypt.decrypt(ciphertext)
print("Decrypted text:", decryptedtext.decode('utf-8'))
