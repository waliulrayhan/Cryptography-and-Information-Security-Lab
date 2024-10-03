# Function to encrypt using Auto Key cipher
def encrypt_auto_key(plaintext, keyword):
    plaintext = plaintext.upper().replace(" ", "")  # Remove spaces and make uppercase
    keyword = keyword.upper()
    
    # Generate the key by appending the plaintext after the keyword
    key = keyword + plaintext[:len(plaintext) - len(keyword)]
    
    ciphertext = ''
    for i in range(len(plaintext)):
        # Encryption formula: (P + K) mod 26
        P = ord(plaintext[i]) - 65
        K = ord(key[i]) - 65
        C = (P + K) % 26
        ciphertext += chr(C + 65)  # Convert back to letter
    return ciphertext

# Function to decrypt using Auto Key cipher
def decrypt_auto_key(ciphertext, keyword):
    ciphertext = ciphertext.upper().replace(" ", "")  # Remove spaces and make uppercase
    keyword = keyword.upper()
    
    # The key starts with the keyword and is extended by the decrypted text
    key = keyword
    plaintext = ''
    
    for i in range(len(ciphertext)):
        # Decryption formula: (C - K) mod 26
        C = ord(ciphertext[i]) - 65
        K = ord(key[i]) - 65
        P = (C - K + 26) % 26
        decrypted_char = chr(P + 65)  # Convert back to letter
        plaintext += decrypted_char
        # Append decrypted character to key to extend it
        key += decrypted_char
    
    return plaintext

# Main program to accept user input
if __name__ == "__main__":
    # Input from the user
    plaintext = input("Enter the plaintext: ")
    keyword = input("Enter the keyword: ")

    # Encrypt the plaintext
    ciphertext = encrypt_auto_key(plaintext, keyword)
    print(f"Encrypted Ciphertext: {ciphertext}")

    # Decrypt the ciphertext
    decrypted_text = decrypt_auto_key(ciphertext, keyword)
    print(f"Decrypted Text (should match the original plaintext): {decrypted_text}")
