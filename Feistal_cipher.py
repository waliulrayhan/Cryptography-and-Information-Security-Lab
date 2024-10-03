# Example round function: simple XOR with the key
def round_function(data, key):
    return data ^ key

# Function to encrypt using the Feistel cipher
def feistel_encrypt(plaintext, keys, num_rounds):
    # Split the plaintext into two halves
    L = plaintext >> 8  # Left half (upper 8 bits)
    R = plaintext & 0xFF  # Right half (lower 8 bits)

    # Apply the Feistel rounds
    for i in range(num_rounds):
        new_L = R
        new_R = L ^ round_function(R, keys[i])
        L = new_L
        R = new_R

    # Combine the two halves and return the ciphertext
    ciphertext = (L << 8) | R
    return ciphertext

# Function to decrypt using the Feistel cipher
def feistel_decrypt(ciphertext, keys, num_rounds):
    # Split the ciphertext into two halves
    L = ciphertext >> 8  # Left half (upper 8 bits)
    R = ciphertext & 0xFF  # Right half (lower 8 bits)

    # Apply the Feistel rounds in reverse order
    for i in range(num_rounds - 1, -1, -1):
        new_R = L
        new_L = R ^ round_function(L, keys[i])
        L = new_L
        R = new_R

    # Combine the two halves and return the decrypted plaintext
    plaintext = (L << 8) | R
    return plaintext

# Main program to accept user input
if __name__ == "__main__":
    # Example usage with 16-bit block and 8-bit keys
    num_rounds = 4
    keys = [0x3, 0x7, 0xF, 0xA]  # Example round keys (4 rounds)

    # Input plaintext (16-bit)
    plaintext = int(input("Enter a 16-bit plaintext (as a number): "))

    # Encrypt the plaintext
    ciphertext = feistel_encrypt(plaintext, keys, num_rounds)
    print(f"Ciphertext (in hexadecimal): {ciphertext:04x}")

    # Decrypt the ciphertext
    decrypted_text = feistel_decrypt(ciphertext, keys, num_rounds)
    print(f"Decrypted Text (in decimal, should match original): {decrypted_text}")
