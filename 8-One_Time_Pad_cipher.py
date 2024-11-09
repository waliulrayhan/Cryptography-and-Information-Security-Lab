import random

# Function to generate a random key of the specified length
def generate_key(length):
    """Generate a random key with the same length as the plaintext."""
    key = ""
    for _ in range(length):
        key += chr(random.randint(0, 255))  # Generates a random ASCII character in the full range (0-255)
        # key += chr(random.randint(32, 126))  # Generates a random ASCII character in the printable range (32-126)
    return key

# Function to encrypt the plaintext using the one-time pad cipher
def encrypt_one_time_pad(plaintext, key):
    """Encrypt the plaintext using the provided key."""
    ciphertext = ""
    for i in range(len(plaintext)):
        # XOR operation between the ASCII values of the plaintext and key characters
        encrypted_char = chr((ord(plaintext[i]) ^ ord(key[i])) % 256)
        ciphertext += encrypted_char
    return ciphertext

# Function to decrypt the ciphertext using the one-time pad cipher
def decrypt_one_time_pad(ciphertext, key):
    """Decrypt the ciphertext using the provided key."""
    plaintext = ""
    for i in range(len(ciphertext)):
        # XOR operation to revert to the original plaintext
        decrypted_char = chr((ord(ciphertext[i]) ^ ord(key[i])) % 256)
        plaintext += decrypted_char
    return plaintext.lower()

# Main program to demonstrate encryption and decryption
if __name__ == "__main__":
    # Input from the user
    plaintext = input("Enter the plaintext: ")

    # Generate a random key with the same length as the plaintext
    key = generate_key(len(plaintext))
    
    # Print the key used for encryption and decryption
    print("Key Used:", key)

    # Encrypt the plaintext
    encrypted_text = encrypt_one_time_pad(plaintext, key)
    print("Encrypted Text:", encrypted_text)

    # Decrypt the ciphertext
    decrypted_text = decrypt_one_time_pad(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)
