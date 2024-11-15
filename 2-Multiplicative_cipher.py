# Function to find multiplicative inverse of key under mod 26
def multiplicative_inverse(key):
    for i in range(26):
        if (key * i) % 26 == 1:
            return i
    return None  # No inverse if none found

# Function to calculate the greatest common divisor (GCD)
def gcd(a, b):  # Define a function named 'gcd' that takes two parameters 'a' and 'b'
    while b != 0:  # Start a loop that continues as long as 'b' is not zero
        a, b = b, a % b  # Simultaneously update 'a' to the value of 'b' and 'b' to the remainder of 'a' divided by 'b'
    return a  # Once 'b' becomes zero, return 'a' as the GCD

# Function to encrypt using multiplicative cipher
def encrypt_multiplicative_cipher(plaintext, key):
    if gcd(key, 26) != 1:
        raise ValueError("Key is not valid. It must be coprime with 26.")
    
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():  # Encrypt only alphabet characters
            shift_base = 65 if char.isupper() else 97  # Set base for upper or lower case letters
            # Encryption formula: (P * K) mod 26
            encrypted_char = chr(((ord(char) - shift_base) * key) % 26 + shift_base)
            ciphertext += encrypted_char
        else:
            ciphertext += char  # Non-alphabet characters remain unchanged
    return ciphertext.upper()

# Function to decrypt using multiplicative cipher
def decrypt_multiplicative_cipher(ciphertext, key):
    inverse_key = multiplicative_inverse(key)
    if inverse_key is None:
        raise ValueError("Multiplicative inverse not found. Invalid key.")
    
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():  # Decrypt only alphabet characters
            shift_base = 65 if char.isupper() else 97  # Set base for upper or lower case letters
            # Decryption formula: (C * K^-1) mod 26
            decrypted_char = chr(((ord(char) - shift_base) * inverse_key) % 26 + shift_base)
            plaintext += decrypted_char
        else:
            plaintext += char  # Non-alphabet characters remain unchanged
    return plaintext.lower()

# Main program to accept user input
if __name__ == "__main__":
    # Input from the user
    plaintext = input("Enter the plaintext: ")
    key = int(input("Enter the multiplicative key: "))
    # key = 7; Ensure that the key is coprime with 26

    # Encrypt the plaintext
    try:
        ciphertext = encrypt_multiplicative_cipher(plaintext, key)
        print(f"Encrypted Ciphertext: {ciphertext}")

        # Decrypt the ciphertext
        decrypted_text = decrypt_multiplicative_cipher(ciphertext, key)
        print(f"Decrypted Text (should match the original plaintext): {decrypted_text}")
    except ValueError as e:
        print(f"Error: {e}")
