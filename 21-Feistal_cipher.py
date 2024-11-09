# Example round function: simple XOR with the key
def round_function(data, key):
    # Perform XOR operation between the data and the key
    return data ^ key

# Function to encrypt using the Feistel cipher
def feistel_encrypt(plaintext, keys, num_rounds):
    # Split the plaintext into two halves: left and right (upper 8 bits and lower 8 bits)
    L = plaintext >> 8  # Left half (upper 8 bits)
    R = plaintext & 0xFF  # Right half (lower 8 bits)

    # Apply the Feistel rounds for the specified number of rounds
    for i in range(num_rounds):
        new_L = R  # The new left half for the next round is the current right half
        # The new right half is the XOR of the current left half and the output of the round function
        new_R = L ^ round_function(R, keys[i])
        # Update L and R for the next round
        L = new_L
        R = new_R

    # Combine the final left and right halves to form the 16-bit ciphertext
    ciphertext = (L << 8) | R  # Shift L left by 8 bits and OR it with R to combine them
    return ciphertext  # Return the encrypted ciphertext

# Function to decrypt using the Feistel cipher
def feistel_decrypt(ciphertext, keys, num_rounds):
    # Split the ciphertext into two halves: left and right (upper 8 bits and lower 8 bits)
    L = ciphertext >> 8  # Left half (upper 8 bits)
    R = ciphertext & 0xFF  # Right half (lower 8 bits)

    # Apply the Feistel rounds in reverse order (from last to first)
    for i in range(num_rounds - 1, -1, -1):
        new_R = L  # The new right half for the next round is the current left half
        # The new left half is the XOR of the current right half and the output of the round function
        new_L = R ^ round_function(L, keys[i])
        # Update L and R for the next round
        L = new_L
        R = new_R

    # Combine the final left and right halves to form the 16-bit plaintext
    plaintext = (L << 8) | R  # Shift L left by 8 bits and OR it with R to combine them
    return plaintext  # Return the decrypted plaintext

# Main program to accept user input and demonstrate encryption and decryption
if __name__ == "__main__":
    # Example usage with a 16-bit block size and 8-bit keys
    num_rounds = 4  # Number of Feistel rounds to apply
    keys = [0x3, 0x7, 0xF, 0xA]  # Example round keys for the encryption process

    # Input the plaintext from the user (as a 16-bit number, max value 65535)
    plaintext = int(input("Enter a 16-bit plaintext max 65535 (as a number): "))

    # Encrypt the plaintext using the feistel_encrypt function
    ciphertext = feistel_encrypt(plaintext, keys, num_rounds)
    # Print the resulting ciphertext in hexadecimal format (4 digits)
    print(f"Ciphertext (in hexadecimal): {ciphertext:04x}")

    # Decrypt the ciphertext using the feistel_decrypt function
    decrypted_text = feistel_decrypt(ciphertext, keys, num_rounds)
    # Print the decrypted text in decimal format (should match the original plaintext)
    print(f"Decrypted Text (in decimal, should match original): {decrypted_text}")
