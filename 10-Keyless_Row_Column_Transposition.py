# keyless row column transposition 
import numpy as np  # Import the NumPy library for creating and handling arrays

# Function to encrypt the plaintext using keyless row-column transposition
def encrypt_row_column(plaintext, col):
    ciphertext = ""  # Initialize an empty string to store the ciphertext
    length = len(plaintext)  # Get the length of the plaintext
    remainder = length % col  # Calculate the remainder to check if padding is needed

    # Determine the number of rows needed for the given number of columns
    if remainder == 0:
        row = length // col  # Exact division if no remainder
    else:
        row = (length // col) + 1  # Add an extra row if there is a remainder

    # Create a dynamic array (table) filled with 'z' as padding
    table = np.array([['z'] * col for _ in range(row)])

    # Fill the table with characters from the plaintext
    index = 0  # Initialize the index to start filling the table from the beginning of the plaintext
    for i in range(row):  # Iterate over each row
        for j in range(col):  # Iterate over each column
            if index < len(plaintext):  # Check if there are still characters left to fill
                table[i][j] = plaintext[index]  # Place the character in the current cell
                index += 1  # Move to the next character in the plaintext

    # Create the ciphertext by reading the table column by column
    for j in range(col):  # Iterate over each column
        for i in range(row):  # Iterate over each row in the current column
            ciphertext += table[i][j]  # Append the character to the ciphertext

    return ciphertext  # Return the final ciphertext

# Function to decrypt the ciphertext using keyless row-column transposition
def decrypt_row_column(ciphertext, col):
    plaintext = ""  # Initialize an empty string to store the plaintext
    length = len(ciphertext)  # Get the length of the ciphertext
    remainder = length % col  # Calculate the remainder to check if padding is needed

    # Determine the number of rows needed for the given number of columns
    if remainder == 0:
        row = length // col  # Exact division if no remainder
    else:
        row = (length // col) + 1  # Add an extra row if there is a remainder

    # Create a dynamic array (table) filled with 'z' as padding
    table = np.array([['z'] * col for _ in range(row)])

    # Fill the table with characters from the ciphertext column by column
    index = 0  # Initialize the index to start filling the table from the beginning of the ciphertext
    for j in range(col):  # Iterate over each column
        for i in range(row):  # Iterate over each row in the current column
            if index < len(ciphertext):  # Check if there are still characters left to fill
                table[i][j] = ciphertext[index]  # Place the character in the current cell
                index += 1  # Move to the next character in the ciphertext

    # Create the plaintext by reading the table row by row
    for i in range(row):  # Iterate over each row
        for j in range(col):  # Iterate over each column in the current row
            plaintext += table[i][j]  # Append the character to the plaintext

    # Strip any padding characters (e.g., 'z') that were added during encryption
    plaintext = plaintext.rstrip('z')

    return plaintext  # Return the final plaintext

# Example usage
if __name__ == "__main__":
    col = 4  # Number of columns for the transposition (can be adjusted)
    plaintext = input("Enter the plaintext: ")  # Get plaintext input from the user

    # Encrypt the plaintext
    encrypted_text = encrypt_row_column(plaintext, col)
    print("Encrypted Ciphertext:", encrypted_text)  # Print the encrypted ciphertext

    # Decrypt the ciphertext
    decrypted_text = decrypt_row_column(encrypted_text, col)
    print("Decrypted Text:", decrypted_text)  # Print the decrypted plaintext
