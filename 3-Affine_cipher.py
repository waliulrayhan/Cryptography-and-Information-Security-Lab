# Function to find multiplicative inverse of K1 under mod 26
def multiplicative_inverse(K1):
    for i in range(26):
        if (K1 * i) % 26 == 1:
            return i
    return None  # No inverse if none found

# Function to calculate the greatest common divisor (GCD)
def gcd(a, b):  # Define a function named 'gcd' that takes two parameters 'a' and 'b'
    while b != 0:  # Start a loop that continues as long as 'b' is not zero
        a, b = b, a % b  # Simultaneously update 'a' to the value of 'b' and 'b' to the remainder of 'a' divided by 'b'
    return a  # Once 'b' becomes zero, return 'a' as the GCD

# Function to encrypt using affine cipher
def encrypt_affine_cipher(plaintext, K1, K2):
    if gcd(K1, 26) != 1:
        raise ValueError("Multiplicative key K1 must be coprime with 26.")
    
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():  # Encrypt only alphabet characters
            shift_base = 65 if char.isupper() else 97  # Set base for upper or lower case letters
            # Encryption formula: (P * K1 + K2) mod 26
            encrypted_char = chr(((ord(char) - shift_base) * K1 + K2) % 26 + shift_base)
            ciphertext += encrypted_char
        else:
            ciphertext += char  # Non-alphabet characters remain unchanged
    return ciphertext

# Function to decrypt using affine cipher
def decrypt_affine_cipher(ciphertext, K1, K2):
    inverse_K1 = multiplicative_inverse(K1)
    if inverse_K1 is None:
        raise ValueError("Multiplicative inverse not found. Invalid K1.")
    
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():  # Decrypt only alphabet characters
            shift_base = 65 if char.isupper() else 97  # Set base for upper or lower case letters
            # Decryption formula: ((C - K2) * K1^-1) mod 26
            decrypted_char = chr(((ord(char) - shift_base - K2) * inverse_K1) % 26 + shift_base)
            plaintext += decrypted_char
        else:
            plaintext += char  # Non-alphabet characters remain unchanged
    return plaintext

# Main program to accept user input
if __name__ == "__main__":
    # Input from the user
    plaintext = input("Enter the plaintext: ")
    K1 = int(input("Enter the multiplicative key (K1): "))
    K2 = int(input("Enter the additive key (K2): "))

    # Encrypt the plaintext
    try:
        ciphertext = encrypt_affine_cipher(plaintext, K1, K2)
        print(f"Encrypted Ciphertext: {ciphertext}")

        # Decrypt the ciphertext
        decrypted_text = decrypt_affine_cipher(ciphertext, K1, K2)
        print(f"Decrypted Text (should match the original plaintext): {decrypted_text}")
    except ValueError as e:
        print(f"Error: {e}")
