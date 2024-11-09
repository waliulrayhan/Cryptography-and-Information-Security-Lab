import numpy as np  # Import the NumPy library for matrix operations

# Function to create the plain matrix and key matrix for encryption
def encrypt_keyed_row_column_transposition(plaintext, key):
    ciphertext = ""  # Initialize the ciphertext as an empty string
    length = len(plaintext)  # Get the length of the plaintext
    key_length = len(key)  # Get the length of the key
    value = key_length  # Set the value to the key length for convenience

    # Determine the number of rows needed to fit the plaintext in the table
    if length % value == 0:
        col = int(length / value)  # Exact division if the length is divisible by key length
    else:
        col = int(length / value) + 1  # Add an extra row if there is a remainder

    # Create matrices for plaintext and key
    plainMatrix = np.array([[25] * value] * col)  # Initialize the plain matrix with a default value (e.g., 25)
    keyMatrix = np.array([[0] * value] * value)  # Initialize the key matrix with zeros

    # Fill the plain matrix with numerical values representing plaintext characters
    index = 0  # Start from the first character in the plaintext
    for i in range(col):  # Iterate over each row
        for j in range(value):  # Iterate over each column
            if index < length:  # Check if there are still characters left in the plaintext
                num = ord(plaintext[index]) - 97  # Convert the character to a number (a=0, b=1, ...)
                plainMatrix[i][j] = num  # Assign the number to the matrix
                index += 1  # Move to the next character

    # Fill the key matrix according to the provided key
    j = 0  # Initialize column index for the key matrix
    for i in range(len(key)):  # Iterate over the length of the key
        keyMatrix[key[i]][j] = 1  # Mark the position in the key matrix according to the key
        j += 1  # Move to the next column

    # Perform the matrix multiplication to create the cipher matrix
    cipherMatrix = np.matmul(plainMatrix, keyMatrix)  # Multiply the plain matrix by the key matrix

    # Convert the numerical cipher matrix to the ciphertext
    for i in range(value):  # Iterate over each column
        for j in range(col):  # Iterate over each row
            value = (cipherMatrix[j][i] % 26) + 65  # Convert the number back to a character (A=65, B=66, ...)
            ciphertext += chr(value)  # Append the character to the ciphertext

    return ciphertext  # Return the final ciphertext

# Function to decrypt the ciphertext using the key matrix
def decrypt_keyed_row_column_transposition(ciphertext, key):
    plaintext = ""  # Initialize the plaintext as an empty string
    length = len(ciphertext)  # Get the length of the ciphertext
    key_length = len(key)  # Get the length of the key
    value = key_length  # Set the value to the key length for convenience
    col = int(length / value)  # Calculate the number of rows

    # Create matrices for the ciphertext and key
    cipherMatrix = np.array([[0] * col] * value)  # Initialize the cipher matrix
    keyMatrix = np.array([[0] * value] * value)  # Initialize the key matrix

    # Fill the cipher matrix with numerical values representing ciphertext characters
    index = 0  # Start from the first character in the ciphertext
    for i in range(value):  # Iterate over each column
        for j in range(col):  # Iterate over each row
            if index < length:  # Check if there are still characters left in the ciphertext
                num = ord(ciphertext[index]) - 65  # Convert the character to a number (A=0, B=1, ...)
                cipherMatrix[i][j] = num  # Assign the number to the matrix
                index += 1  # Move to the next character

    # Fill the key matrix according to the provided key
    j = 0  # Initialize column index for the key matrix
    for i in range(len(key)):  # Iterate over the length of the key
        keyMatrix[key[i]][j] = 1  # Mark the position in the key matrix according to the key
        j += 1  # Move to the next column

    # Invert the key matrix for decryption
    keyMatrix = np.linalg.inv(keyMatrix)  # Calculate the inverse of the key matrix

    # Perform the matrix multiplication to decrypt
    plainMatrix = np.matmul(np.transpose(cipherMatrix), keyMatrix)  # Transpose and multiply by the inverted key matrix

    # Convert the numerical plain matrix back to plaintext
    for i in range(col):  # Iterate over each row
        for j in range(value):  # Iterate over each column
            result = (int(round(plainMatrix[i][j])) % 26) + 97  # Convert the number back to a character (a=97, b=98, ...)
            plaintext += chr(result)  # Append the character to the plaintext

    return plaintext.strip('z')  # Remove any padding characters added during encryption

# Example usage
if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ")  # Get the plaintext input from the user
    key = [2, 0, 3, 4, 1]  # Example key for transposition

    # Encrypt the plaintext
    encrypted_text = encrypt_keyed_row_column_transposition(plaintext, key)
    print("Encrypted Ciphertext:", encrypted_text)  # Print the encrypted ciphertext

    # Decrypt the ciphertext
    decrypted_text = decrypt_keyed_row_column_transposition(encrypted_text, key)
    print("Decrypted Text:", decrypted_text)  # Print the decrypted plaintext
