import numpy as np  # Import NumPy, though it's not used in this code. It can be removed if not needed.

# Function to encrypt the plaintext using a keyed row transposition cipher
def encrypt_keyed_row_transposition(plaintext, blockSize, key):
    # Initialize the ciphertext as an empty string
    ciphertext = ""
    
    # Calculate the number of extra characters needed to pad the plaintext to a multiple of blockSize
    value = len(plaintext) % blockSize
    if value != 0:
        # Add 'z' as padding to make the length of plaintext a multiple of blockSize
        plaintext += 'z' * (blockSize - value)
    
    # Calculate the number of complete rows needed for the given blockSize
    num_rows = len(plaintext) // blockSize
    
    # Create a 2D array (table) to hold the plaintext characters
    table = [[''] * blockSize for _ in range(num_rows)]
    
    # Fill the table with characters from the plaintext row by row
    index = 0  # Start at the first character in the plaintext
    for i in range(num_rows):  # Iterate over each row
        for j in range(blockSize):  # Iterate over each column
            if index < len(plaintext):  # Check if there are characters left in the plaintext
                table[i][j] = plaintext[index]  # Place the character in the current cell
                index += 1  # Move to the next character

    # Perform the transposition using the provided key
    for col_index in key:  # Iterate over the columns in the order specified by the key
        for row in range(num_rows):  # Iterate over each row
            ciphertext += table[row][col_index]  # Append the character from the specified column to the ciphertext
    
    return ciphertext  # Return the final ciphertext

# Function to decrypt the ciphertext using a keyed row transposition cipher
def decrypt_keyed_row_transposition(ciphertext, blockSize, key):
    # Calculate the number of rows needed for the given blockSize
    num_rows = len(ciphertext) // blockSize

    # Create a 2D array (table) to hold the ciphertext characters
    table = [[''] * blockSize for _ in range(num_rows)]
    
    # Create an inverted key that maps the transposition key back to the original column positions
    inverted_key = sorted(range(len(key)), key=lambda k: key[k])

    # Fill the table column by column based on the original key order (inverted key)
    index = 0  # Start at the first character in the ciphertext
    for col_index in inverted_key:  # Iterate over the columns in the inverted key order
        for row in range(num_rows):  # Iterate over each row
            if index < len(ciphertext):  # Check if there are characters left in the ciphertext
                table[row][col_index] = ciphertext[index]  # Place the character in the current cell
                index += 1  # Move to the next character

    # Read the table row by row to reconstruct the plaintext
    plaintext = ""  # Initialize the plaintext as an empty string
    for i in range(num_rows):  # Iterate over each row
        for j in range(blockSize):  # Iterate over each column
            plaintext += table[i][j]  # Append the character to the plaintext

    # Remove any padding characters ('z') added during encryption
    plaintext = plaintext.rstrip('z')
    
    return plaintext  # Return the final plaintext

# Example usage
if __name__ == "__main__":
    blockSize = 4  # Block size for the transposition (can be adjusted)
    key = [1, 0, 2, 3]  # Key used for transposition; this specifies the column order

    plaintext = input("Enter the plaintext: ")  # Get the plaintext input from the user

    # Encrypt the plaintext
    encrypted_text = encrypt_keyed_row_transposition(plaintext, blockSize, key)
    print("Encrypted Ciphertext:", encrypted_text)  # Print the encrypted text

    # Decrypt the ciphertext
    decrypted_text = decrypt_keyed_row_transposition(encrypted_text, blockSize, key)
    print("Decrypted Text:", decrypted_text)  # Print the decrypted text to verify correctness
