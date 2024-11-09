# Function to convert characters to integer values (0-25)
def char_to_int(c):
    return ord(c.lower()) - ord('a')  # Convert the character to lowercase, get its ASCII value, and subtract the ASCII value of 'a' to get a value between 0 and 25.

# Function to convert integer values to characters
def int_to_char(i):
    return chr((i % 26) + ord('a'))  # Convert the integer (mod 26 ensures it stays within 0-25) back to a character by adding it to the ASCII value of 'a'.

# Function to encrypt using Auto Key cipher
def encrypt_auto_key(plaintext, initial_key):
    plaintext = plaintext.replace(" ", "").lower()  # Remove spaces and convert the plaintext to lowercase.
    key_stream = [initial_key]  # Initialize the key stream with the initial key.

    # Build the key stream using the plaintext characters
    for char in plaintext[:-1]:  # Iterate over the plaintext except the last character.
        key_stream.append(char_to_int(char))  # Convert each character to an integer and append to the key stream.

    # Encrypt the plaintext
    ciphertext = ""  # Initialize an empty string for the ciphertext.
    for i, char in enumerate(plaintext):  # Iterate through each character in the plaintext with its index.
        p_val = char_to_int(char)  # Convert the current character to its integer value.
        c_val = (p_val + key_stream[i]) % 26  # Add the corresponding key stream value and take modulo 26 to get the ciphertext character's value.
        ciphertext += int_to_char(c_val)  # Convert the integer value to a character, make it uppercase, and add it to the ciphertext.

    return ciphertext.upper()  # Return the final encrypted ciphertext.

# Function to decrypt using Auto Key cipher
def decrypt_auto_key(ciphertext, initial_key):
    ciphertext = ciphertext.replace(" ", "").lower()  # Remove spaces and convert the ciphertext to lowercase.
    key_stream = [initial_key]  # Initialize the key stream with the initial key.
    plaintext = ""  # Initialize an empty string for the plaintext.

    # Decrypt the ciphertext
    for i, char in enumerate(ciphertext):  # Iterate through each character in the ciphertext with its index.
        c_val = char_to_int(char)  # Convert the current character to its integer value.
        p_val = (c_val - key_stream[i]) % 26  # Subtract the key stream value from the character value and take modulo 26 to get the plaintext character's value.
        plaintext_char = int_to_char(p_val)  # Convert the integer value to a character.
        plaintext += plaintext_char  # Add the character to the plaintext.

        # Append the decrypted character value to the key stream
        key_stream.append(p_val)  # Add the integer value of the decrypted character to the key stream for use in subsequent steps.

    return plaintext.lower()  # Return the final decrypted plaintext.

# Main program to accept user input
if __name__ == "__main__":
    # Input from the user
    plaintext = input("Enter the plaintext: ")  # Prompt the user to enter the plaintext.
    initial_key = int(input("Enter the Initial key: "))  # Prompt the user to enter the initial key (as an integer).

    # Encrypt the plaintext
    ciphertext = encrypt_auto_key(plaintext, initial_key)  # Call the encryption function.
    print(f"Encrypted Ciphertext: {ciphertext}")  # Print the resulting ciphertext.

    # Decrypt the ciphertext
    decrypted_text = decrypt_auto_key(ciphertext, initial_key)  # Call the decryption function.
    print(f"Decrypted Text (should match the original plaintext): {decrypted_text}")  # Print the decrypted text and verify it matches the original plaintext.

