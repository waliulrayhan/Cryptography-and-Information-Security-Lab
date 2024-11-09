import numpy as np

# Function to convert a character to a number (A=0, B=1, ..., Z=25)
def char_to_number(char):
    return ord(char.upper()) - ord('A')

# Function to convert a number to a character (0=A, 1=B, ..., 25=Z)
def number_to_char(number):
    return chr((number % 26) + ord('A'))

# Function to preprocess the plaintext (removes spaces and adds padding if needed)
def preprocess_plaintext(plaintext, block_size):
    plaintext = plaintext.replace(" ", "").upper()  # Remove spaces and convert to uppercase
    while len(plaintext) % block_size != 0:  # Add 'X' to make the length a multiple of block size
        plaintext += 'X'
    return plaintext

# Function to split the text into blocks of a given size
def create_blocks(text, block_size):
    blocks = []  # Initialize an empty list to store the blocks
    for i in range(0, len(text), block_size):  # Iterate over the text with a step of block_size
        block = text[i:i + block_size]  # Extract a block of the given size
        blocks.append(block)  # Add the block to the list
    return blocks  # Return the list of blocks

# Function to convert a block of text to a numeric vector
def text_to_vector(block):
    vector = []  # Initialize an empty list to store numeric values
    for char in block:  # Iterate over each character in the block
        num = char_to_number(char)  # Convert the character to a number (A=0, B=1, ..., Z=25)
        vector.append(num)  # Add the number to the vector
    return vector  # Return the numeric vector

# Function to convert a numeric vector to a block of text
def vector_to_text(vector):
    text_block = ""  # Initialize an empty string to store the text block
    for num in vector:  # Iterate over each number in the vector
        char = number_to_char(num)  # Convert the number back to a character
        text_block += char  # Append the character to the text block
    return text_block  # Return the text block

# Function to encrypt the plaintext using the Hill cipher
def hill_cipher_encrypt(plaintext, key_matrix):
    block_size = key_matrix.shape[0]  # Get the size of the block from the key matrix
    plaintext = preprocess_plaintext(plaintext, block_size)  # Preprocess the plaintext
    blocks = create_blocks(plaintext, block_size)  # Split plaintext into blocks

    ciphertext = ""
    for block in blocks:
        vector = text_to_vector(block)  # Convert block to numeric vector
        encrypted_vector = np.dot(key_matrix, vector) % 26  # Matrix multiplication and mod 26
        ciphertext += vector_to_text(encrypted_vector)  # Convert back to text and append
    
    return ciphertext.upper()

# Function to decrypt the ciphertext using the Hill cipher
def hill_cipher_decrypt(ciphertext, key_matrix):
    block_size = key_matrix.shape[0]  # Get the size of the block from the key matrix
    blocks = create_blocks(ciphertext, block_size)  # Split ciphertext into blocks

    # Calculate the modular inverse of the key matrix
    det = int(np.round(np.linalg.det(key_matrix)))  # Determinant of the key matrix
    det_inv = pow(det, -1, 26)  # Modular inverse of the determinant in mod 26
    adjugate = np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26  # Adjugate matrix
    key_matrix_inv = (det_inv * adjugate) % 26  # Modular inverse matrix

    plaintext = ""
    for block in blocks:
        vector = text_to_vector(block)  # Convert block to numeric vector
        decrypted_vector = np.dot(key_matrix_inv, vector) % 26  # Matrix multiplication and mod 26
        plaintext += vector_to_text(decrypted_vector)  # Convert back to text and append
    
    return plaintext.lower()

# Main function to run the Hill cipher
if __name__ == "__main__":
    # Define a simple 2x2 key matrix for easy understanding
    key_matrix = np.array([
        [9, 7, 11, 13],
        [4, 7, 5, 6],
        [2, 21, 14, 9],
        [3, 23, 21, 8]
    ])

    # Input plaintext
    plaintext = input("Enter the plaintext: ")

    # Encrypt the plaintext
    ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
    print(f"Encrypted Ciphertext: {ciphertext}")

    # Decrypt the ciphertext
    decrypted_text = hill_cipher_decrypt(ciphertext, key_matrix)
    print(f"Decrypted Text (should match the original plaintext): {decrypted_text}")
