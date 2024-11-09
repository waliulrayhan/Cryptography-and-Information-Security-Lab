# Function to encrypt the plaintext using additive cipher
def encrypt_additive_cipher(plaintext, key):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():  # Encrypt only alphabet characters
            shift_base = 65 if char.isupper() else 97  # Set base for upper or lower case letters
            # Encryption formula: (P + K) mod 26
            encrypted_char = chr((ord(char) - shift_base + key) % 26 + shift_base)
            ciphertext += encrypted_char
        else:
            ciphertext += char  # Non-alphabet characters remain unchanged
    return ciphertext

# Function to decrypt the ciphertext using additive cipher
def decrypt_additive_cipher(ciphertext, key):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():  # Decrypt only alphabet characters
            shift_base = 65 if char.isupper() else 97  # Set base for upper or lower case letters
            # Decryption formula: (C - K) mod 26
            decrypted_char = chr((ord(char) - shift_base - key) % 26 + shift_base)
            plaintext += decrypted_char
        else:
            plaintext += char  # Non-alphabet characters remain unchanged
    return plaintext

# Main program to accept user input
if __name__ == "__main__":
    # Input from the user
    plaintext = input("Enter the plaintext: ")
    key = int(input("Enter the shift key: "))

    # Encrypt the plaintext
    ciphertext = encrypt_additive_cipher(plaintext, key)
    print(f"Encrypted Ciphertext: {ciphertext}")

    # Decrypt the ciphertext
    decrypted_text = decrypt_additive_cipher(ciphertext, key)
    print(f"Decrypted Text (should match the original plaintext): {decrypted_text}")
