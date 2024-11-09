# Function to convert letter to number (A=0, B=1, ..., Z=25)
def letter_to_number(letter):
    # Convert the letter to uppercase and find its position in the alphabet by subtracting 'A'
    return ord(letter.upper()) - ord('A')

# Function to convert number to letter (0=A, 1=B, ..., 25=Z)
def number_to_letter(number):
    # Convert a number (mod 26 ensures it's within 0-25) back to a letter by adding it to 'A'
    return chr((number % 26) + ord('A'))

# Function to repeat the keyword to match the length of the plaintext
def repeat_keyword(plaintext, keyword):
    keyword = keyword.upper()  # Convert the keyword to uppercase
    keyword_repeated = ''  # Initialize an empty string for the repeated keyword
    keyword_length = len(keyword)  # Find the length of the keyword

    # Loop through each character in the plaintext
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():  # Check if the current character is an alphabetic character
            # Add the keyword character at position (i % keyword_length) to match the length
            keyword_repeated += keyword[i % keyword_length]
        else:
            # For non-alphabet characters, just copy them directly
            keyword_repeated += plaintext[i]  
    
    return keyword_repeated  # Return the repeated keyword matching the plaintext length

# Function to encrypt the plaintext using Vigenère cipher
def encrypt_vigenere(plaintext, keyword):
    plaintext = plaintext.upper()  # Convert the plaintext to uppercase for consistency
    keyword_repeated = repeat_keyword(plaintext, keyword)  # Repeat the keyword to match plaintext length
    
    ciphertext = ''  # Initialize an empty string for the ciphertext

    # Loop through each character in the plaintext
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():  # Encrypt only alphabetic characters
            P = letter_to_number(plaintext[i])  # Convert plaintext character to a number (0-25)
            K = letter_to_number(keyword_repeated[i])  # Convert keyword character to a number (0-25)
            C = (P + K) % 26  # Apply the Vigenère encryption formula: (P + K) mod 26
            ciphertext += number_to_letter(C)  # Convert the result back to a letter and add to ciphertext
        else:
            # Keep non-alphabet characters unchanged
            ciphertext += plaintext[i]  
    
    return ciphertext.upper()  # Return the ciphertext in uppercase

# Function to decrypt the ciphertext using Vigenère cipher
def decrypt_vigenere(ciphertext, keyword):
    ciphertext = ciphertext.upper()  # Convert the ciphertext to uppercase for consistency
    keyword_repeated = repeat_keyword(ciphertext, keyword)  # Repeat the keyword to match ciphertext length
    
    plaintext = ''  # Initialize an empty string for the plaintext

    # Loop through each character in the ciphertext
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():  # Decrypt only alphabetic characters
            C = letter_to_number(ciphertext[i])  # Convert ciphertext character to a number (0-25)
            K = letter_to_number(keyword_repeated[i])  # Convert keyword character to a number (0-25)
            P = (C - K + 26) % 26  # Apply the Vigenère decryption formula: (C - K + 26) mod 26
            plaintext += number_to_letter(P)  # Convert the result back to a letter and add to plaintext
        else:
            # Keep non-alphabet characters unchanged
            plaintext += ciphertext[i]  
    
    return plaintext.lower()  # Return the plaintext in lowercase for readability

# Main program to accept user input
if __name__ == "__main__":
    # Input from the user for plaintext
    plaintext = input("Enter the plaintext: ")
    # Input from the user for the keyword
    keyword = input("Enter the keyword: ")

    # Encrypt the plaintext using the Vigenère cipher
    ciphertext = encrypt_vigenere(plaintext, keyword)
    # Print the encrypted ciphertext
    print(f"Encrypted Ciphertext: {ciphertext}")

    # Decrypt the ciphertext back to the original plaintext
    decrypted_text = decrypt_vigenere(ciphertext, keyword)
    # Print the decrypted text for verification
    print(f"Decrypted Text (should match the original plaintext): {decrypted_text}")
