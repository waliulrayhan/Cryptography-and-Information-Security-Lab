import numpy as np  # Import the NumPy library for creating and handling arrays

# The 5x5 key matrix for the Playfair cipher
key_matrix = np.array(
    # The matrix is initialized with a specific keyword-derived arrangement of letters
    [
        ['P', 'L', 'A', 'Y', 'F'],
        ['I', 'R', 'B', 'C', 'D'],
        ['E', 'G', 'H', 'K', 'M'],
        ['N', 'O', 'Q', 'S', 'T'],
        ['U', 'V', 'W', 'X', 'Z']
    ]
)

# Function to preprocess the plaintext
def preprocess_plaintext(plaintext):
    plaintext = plaintext.replace(" ", "").upper()  # Remove spaces and convert to uppercase
    processed_text = ""  # Initialize an empty string to store processed text
    i = 0  # Start iterating from the first character

    # Iterate through the plaintext to handle duplicate letters and spacing
    while i < len(plaintext):
        processed_text += plaintext[i]  # Add the current character to the processed text
        # If two consecutive characters are the same, insert 'X' between them
        if i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]:
            processed_text += 'X'  # Insert a bogus letter 'X'
        i += 1  # Move to the next character
        # Add the next character if it exists
        if i < len(plaintext):
            processed_text += plaintext[i]
            i += 1

    # If the length of the processed text is odd, add a trailing 'X'
    if len(processed_text) % 2 != 0:
        processed_text += 'X'
    
    return processed_text  # Return the processed text ready for encryption

# Function to find the position of a letter in the key matrix
def find_position(letter, matrix):
    # Iterate over the matrix to find the letter's position
    for i in range(5):
        for j in range(5):
            if matrix[i, j] == letter:
                return i, j  # Return the row and column indices if found
    return None  # Return None if the letter is not found

# Function to encrypt a pair of characters
def encrypt_pair(pair, matrix):
    r1, c1 = find_position(pair[0], matrix)  # Find the position of the first character
    r2, c2 = find_position(pair[1], matrix)  # Find the position of the second character

    # Rule a: If the characters are in the same row, shift to the right
    if r1 == r2:
        return matrix[r1, (c1 + 1) % 5] + matrix[r2, (c2 + 1) % 5]
    # Rule b: If the characters are in the same column, shift down
    elif c1 == c2:
        return matrix[(r1 + 1) % 5, c1] + matrix[(r2 + 1) % 5, c2]
    # Rule c: If the characters form a rectangle, swap their columns
    else:
        return matrix[r1, c2] + matrix[r2, c1]

# Function to encrypt the plaintext using the Playfair cipher
def encrypt_playfair(plaintext, matrix):
    plaintext = preprocess_plaintext(plaintext)  # Preprocess the plaintext
    ciphertext = ""  # Initialize an empty string for the ciphertext

    # Encrypt each pair of characters
    for i in range(0, len(plaintext), 2):
        pair = plaintext[i:i + 2]  # Get the current pair of characters
        ciphertext += encrypt_pair(pair, matrix)  # Encrypt the pair and add to the ciphertext
    
    return ciphertext.upper()  # Return the ciphertext in uppercase

# Function to decrypt a pair of characters
def decrypt_pair(pair, matrix):
    r1, c1 = find_position(pair[0], matrix)  # Find the position of the first character
    r2, c2 = find_position(pair[1], matrix)  # Find the position of the second character

    # Rule a: If the characters are in the same row, shift to the left
    if r1 == r2:
        return matrix[r1, (c1 - 1) % 5] + matrix[r2, (c2 - 1) % 5]
    # Rule b: If the characters are in the same column, shift up
    elif c1 == c2:
        return matrix[(r1 - 1) % 5, c1] + matrix[(r2 - 1) % 5, c2]
    # Rule c: If the characters form a rectangle, swap their columns
    else:
        return matrix[r1, c2] + matrix[r2, c1]

# Function to decrypt the ciphertext using the Playfair cipher
def decrypt_playfair(ciphertext, matrix):
    ciphertext = ciphertext.replace(" ", "").upper()  # Remove spaces and convert to uppercase
    plaintext = ""  # Initialize an empty string for the plaintext

    # Decrypt each pair of characters
    for i in range(0, len(ciphertext), 2):
        pair = ciphertext[i:i + 2]  # Get the current pair of characters
        plaintext += decrypt_pair(pair, matrix)  # Decrypt the pair and add to the plaintext
    
    return plaintext.lower()  # Return the plaintext in lowercase

# Main function to get user input and perform encryption and decryption
if __name__ == "__main__":
    plaintext = input("Enter the plaintext: ")  # Get plaintext input from the user

    # Encrypt the plaintext
    ciphertext = encrypt_playfair(plaintext, key_matrix)  # Call the encryption function
    print(f"Encrypted Ciphertext: {ciphertext}")  # Print the resulting ciphertext

    # Decrypt the ciphertext
    decrypted_text = decrypt_playfair(ciphertext, key_matrix)  # Call the decryption function
    print(f"Decrypted Text (should match the original plaintext): {decrypted_text}")  # Print the decrypted text and verify it matches the original plaintext
