# myenv\Scripts\activate  # For Windows

# Import necessary modules
import base64  # Base64 is used to encode the ciphertext into a readable string format.
from Crypto.Cipher import AES  # The AES (Advanced Encryption Standard) module is imported from the pycryptodome library for encryption.
from Crypto.Random import get_random_bytes  # This is used to generate random bytes for the AES key and nonce.

# Input plaintext from the user
plaintext = input("Enter the plaintext: ").encode('utf-8')  # Convert the input string to bytes (AES requires byte data)

# Generate a random 16-byte key for AES
key = get_random_bytes(16)  # AES requires a key of 128, 192, or 256 bits. Here, we generate a random 16-byte key (128 bits).

# Create a cipher object using AES with EAX mode
cipher = AES.new(key, AES.MODE_EAX)  # AES.MODE_EAX is a secure mode that provides both encryption and authentication.
                                      # The EAX mode requires a nonce (number used once), which is automatically handled here.
                                      # EAX also provides integrity verification by generating a 'tag'.

# Encrypt the plaintext and generate an authentication tag
ciphertext, tag = cipher.encrypt_and_digest(plaintext)  # The encryption process, along with the generation of the authentication tag.
                                                        # The 'encrypt_and_digest' method returns both the ciphertext and the tag.
                                                        # The tag is used later for verifying the integrity of the data during decryption.

# Print the ciphertext and the tag in Base64 encoding
print("Ciphertext : ", base64.b64encode(ciphertext))  # The ciphertext is encoded into Base64 to make it human-readable.
print("Tag : ", tag)  # The tag is printed as is. It’s used during decryption for authentication.

# Decryption part
decrypt_cipher = AES.new(key, AES.MODE_EAX, nonce=cipher.nonce)  # A new AES cipher object is created for decryption.
                                                              # The same key and nonce (generated during encryption) are used for decryption.
                                                              # The nonce must be the same for encryption and decryption in EAX mode.

# Decrypt the ciphertext and verify its integrity using the tag
decrypted_text = decrypt_cipher.decrypt_and_verify(ciphertext, tag)  # The 'decrypt_and_verify' method decrypts the ciphertext.
                                                                   # It also verifies the authenticity of the data using the tag.
                                                                   # If the data is altered or corrupted, it will raise an error.

# Print the decrypted text
print("Decrypted text: ", decrypted_text.decode())  # The decrypted data is decoded back to a string format using UTF-8 decoding.
                                                   # In this case, the decrypted text will be "This is a secret message".
