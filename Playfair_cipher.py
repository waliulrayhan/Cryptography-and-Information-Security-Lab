import numpy as np

# Declaring the 5x5 key matrix
key_matrix = np.array(
    [
        ['L', 'G', 'D', 'B', 'A'],
        ['Q', 'M', 'H', 'E', 'C'],
        ['U', 'R', 'N', 'J', 'F'],
        ['X', 'V', 'S', 'O', 'K'],
        ['Z', 'Y', 'W', 'T', 'P']
    ]
)

# Creating transpose matrix of the key matrix
transpose_key_matrix = np.transpose(key_matrix)

# Input Section
plaintext = input("Enter the plaintext: ")
print("Given Plaintext: ", plaintext)

# Removing all the whitespaces from the plaintext
text = plaintext.replace(" ", "")
text_len = len(text)
text = text.upper()

# Replace all "I" in the plaintext to "J"
text = text.replace("I", "J")

# Make pair of two (different) characters from plaintext
plaintextpair = []
i = 0
while i < text_len:
    char1 = text[i]
    char2 = ""
    # If the letter is the last character of the plaintext add a bogus character "X"
    if (i + 1) == len(text):
        char2 = "X"
    # Else add the next character
    else:
        char2 = text[i + 1]
    # If the two characters are different, insert them in the pair
    if char1 != char2:
        plaintextpair.append(char1 + char2)
        i = i + 2
    # Else add "X" as the second character
    else:
        plaintextpair.append(char1 + "X")
        i = i + 1

print("Pairs of plaintext: ", plaintextpair)

# Encryption Function
ciphertext = ""
ciphertextpair = []
for pair in plaintextpair:
    apply_rule = True
    # Rule 1: If the two characters are in the same row, replace them with their right character
    if apply_rule:
        for row in range(5):
            if pair[0] in key_matrix[row] and pair[1] in key_matrix[row]:
                for i in range(5):
                    if key_matrix[row][i] == pair[0]:
                        char1 = key_matrix[row][(i + 1) % 5]
                    elif key_matrix[row][i] == pair[1]:
                        char2 = key_matrix[row][(i + 1) % 5]
                apply_rule = False
                ciphertextpair.append(char1 + char2)
                ciphertext = ciphertext + char1 + char2

    # Rule 2: If the two characters are in the same column, replace them with their below character
    if apply_rule:
        for column in range(5):
            if pair[0] in transpose_key_matrix[column] and pair[1] in transpose_key_matrix[column]:
                for i in range(5):
                    if transpose_key_matrix[column][i] == pair[0]:
                        char1 = transpose_key_matrix[column][(i + 1) % 5]
                    elif transpose_key_matrix[column][i] == pair[1]:
                        char2 = transpose_key_matrix[column][(i + 1) % 5]
                apply_rule = False
                ciphertextpair.append(char1 + char2)
                ciphertext = ciphertext + char1 + char2

    # Rule 3: If the two letters are not in the same row or column, replace them with letters
    # in the same row as the other letter but in their respective columns.
    if apply_rule:
        for row in range(5):
            for column in range(5):
                if key_matrix[row][column] == pair[0]:
                    x0 = row
                    y0 = column
                elif key_matrix[row][column] == pair[1]:
                    x1 = row
                    y1 = column
        char1 = key_matrix[x0][y1]
        char2 = key_matrix[x1][y0]
        ciphertextpair.append(char1 + char2)
        ciphertext = ciphertext + char1 + char2

print("Ciphertext: ", ciphertext)

# Decryption Function
decryptedtext = ""
for pair in ciphertextpair:
    apply_rule = True
    # Rule 1: If the two characters are in the same row, replace them with their left character
    if apply_rule:
        for row in range(5):
            if pair[0] in key_matrix[row] and pair[1] in key_matrix[row]:
                for i in range(5):
                    if key_matrix[row][i] == pair[0]:
                        char1 = key_matrix[row][(i - 1) % 5]
                    elif key_matrix[row][i] == pair[1]:
                        char2 = key_matrix[row][(i - 1) % 5]
                apply_rule = False
                decryptedtext = decryptedtext + char1 + char2

    # Rule 2: If the two characters are in the same column, replace them with their upper character
    if apply_rule:
        for column in range(5):
            if pair[0] in transpose_key_matrix[column] and pair[1] in transpose_key_matrix[column]:
                for i in range(5):
                    if transpose_key_matrix[column][i] == pair[0]:
                        char1 = transpose_key_matrix[column][(i - 1) % 5]
                    elif transpose_key_matrix[column][i] == pair[1]:
                        char2 = transpose_key_matrix[column][(i - 1) % 5]
                apply_rule = False
                decryptedtext = decryptedtext + char1 + char2

    # Rule 3: If the two letters are not in the same row or column, replace them with letters
    # in the same row as the other letter but in their respective columns.
    if apply_rule:
        for row in range(5):
            for column in range(5):
                if key_matrix[row][column] == pair[0]:
                    x0 = row
                    y0 = column
                elif key_matrix[row][column] == pair[1]:
                    x1 = row
                    y1 = column
        char1 = key_matrix[x0][y1]
        char2 = key_matrix[x1][y0]
        decryptedtext = decryptedtext + char1 + char2

print("Decrypted text: ", decryptedtext.lower())