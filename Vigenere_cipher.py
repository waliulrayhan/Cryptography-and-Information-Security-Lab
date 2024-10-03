# Function to convert letter to number (A=0, B=1, ..., Z=25)
def letter_to_number(letter):
    return ord(letter.upper()) - ord('A')

# Function to convert number to letter (0=A, 1=B, ..., 25=Z)
def number_to_letter(number):
    return chr((number % 26) + ord('A'))

# Function to repeat the keyword to match the length of the plaintext
def repeat_keyword(plaintext, keyword):
    keyword = keyword.upper()
    keyword_repeated = ''
    keyword_length = len(keyword)
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            keyword_repeated += keyword[i % keyword_length]
        else:
            keyword_repeated += plaintext[i]  # Keep non-alphabet characters unchanged
    return keyword_repeated

# Function to encrypt the plaintext using Vigenère cipher
def encrypt_vigenere(plaintext, keyword):
    plaintext = plaintext.upper()
    keyword_repeated = repeat_keyword(plaintext, keyword)
    
    ciphertext = ''
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():  # Encrypt only alphabetic characters
            P = letter_to_number(plaintext[i])
            K = letter_to_number(keyword_repeated[i])
            C = (P + K) % 26  # Vigenère encryption formula
            ciphertext += number_to_letter(C)
        else:
            ciphertext += plaintext[i]  # Keep non-alphabet characters unchanged

    return ciphertext

# Function to decrypt the ciphertext using Vigenère cipher
def decrypt_vigenere(ciphertext, keyword):
    ciphertext = ciphertext.upper()
    keyword_repeated = repeat_keyword(ciphertext, keyword)
    
    plaintext = ''
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():  # Decrypt only alphabetic characters
            C = letter_to_number(ciphertext[i])
            K = letter_to_number(keyword_repeated[i])
            P = (C - K + 26) % 26  # Vigenère decryption formula
            plaintext += number_to_letter(P)
        else:
            plaintext += ciphertext[i]  # Keep non-alphabet characters unchanged

    return plaintext

# Main program to accept user input
if __name__ == "__main__":
    # Input from the user
    plaintext = input("Enter the plaintext: ")
    keyword = input("Enter the keyword: ")

    # Encrypt the plaintext
    ciphertext = encrypt_vigenere(plaintext, keyword)
    print(f"Encrypted Ciphertext: {ciphertext}")

    # Decrypt the ciphertext
    decrypted_text = decrypt_vigenere(ciphertext, keyword)
    print(f"Decrypted Text (should match the original plaintext): {decrypted_text}")
