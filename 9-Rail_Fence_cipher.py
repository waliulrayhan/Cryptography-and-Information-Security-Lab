# Function to encrypt the plaintext using Rail Fence Cipher
def encrypt_rail_fence(plaintext, depth):
    ciphertext = ""  # Initialize an empty string to store the ciphertext
    cycle = 2 * depth - 2  # The complete cycle length for the zigzag pattern

    # Iterate over each row (rail)
    for row in range(depth):
        index = 0  # Start at the beginning of the plaintext

        # Encrypt the first and last rails differently from the middle rails
        if row == 0 or row == (depth - 1):  # Check if it is the top or bottom rail
            index = row  # Start from the current row index
            while index < len(plaintext):
                ciphertext += plaintext[index]  # Add the character to the ciphertext
                index += cycle  # Move by the cycle length to the next character in the same rail
        else:
            # Middle rails use two indices in the cycle to form the zigzag pattern
            left_index = row  # Start from the current row
            right_index = cycle - row  # Calculate the other index for the zigzag

            while left_index < len(plaintext):
                ciphertext += plaintext[left_index]  # Add character from the left index

                if right_index < len(plaintext):
                    ciphertext += plaintext[right_index]  # Add character from the right index

                # Update indices to move to the next cycle in the zigzag
                left_index += cycle
                right_index += cycle

    return ciphertext.upper()  # Return the complete ciphertext

# Function to decrypt the ciphertext using Rail Fence Cipher
def decrypt_rail_fence(ciphertext, depth):
    cycle = 2 * depth - 2  # The complete cycle length for the zigzag pattern
    length = len(ciphertext)  # Get the length of the ciphertext
    plaintext = [""] * length  # Initialize the plaintext with placeholders (empty strings)

    # Determine how many characters are in each rail
    units = length // cycle  # Number of complete cycles in the ciphertext
    rails_length = [0] * depth  # Array to store the length of each rail

    # Top rail length (first row)
    rails_length[0] = units

    # Intermediate rail lengths (middle rows)
    for i in range(1, depth - 1):
        rails_length[i] = 2 * units  # Each middle rail contains two characters per cycle

    # Bottom rail length (last row)
    rails_length[depth - 1] = units

    # Add one extra character to each rail if needed (for incomplete cycles)
    for i in range(length % cycle):
        if i < depth:
            rails_length[i] += 1
        else:
            rails_length[cycle - i] += 1

    # Replace the characters of each rail into the plaintext
    index = 0  # Index to keep track of the position in the plaintext
    rail_offset = 0  # Offset to track the current position in the ciphertext

    # Place characters for the top rail
    for c in range(rails_length[0]):
        plaintext[index] = ciphertext[rail_offset]  # Place the character in the correct position
        index += cycle  # Move to the next cycle position
        rail_offset += 1  # Move to the next character in the ciphertext

    # Place characters for the intermediate rails
    for row in range(1, depth - 1):
        left_index = row  # Start index for the left character
        right_index = cycle - row  # Start index for the right character
        left_char = True  # Boolean to toggle between left and right

        for c in range(rails_length[row]):
            if left_char:
                plaintext[left_index] = ciphertext[rail_offset]  # Place left character
                left_index += cycle  # Move to the next cycle position for left
                left_char = not left_char  # Toggle to right character
            else:
                plaintext[right_index] = ciphertext[rail_offset]  # Place right character
                right_index += cycle  # Move to the next cycle position for right
                left_char = not left_char  # Toggle to left character

            rail_offset += 1  # Move to the next character in the ciphertext

    # Place characters for the bottom rail (last row)
    index = depth - 1  # Start index for the bottom rail
    for c in range(rails_length[depth - 1]):
        plaintext[index] = ciphertext[rail_offset]  # Place the character
        index += cycle  # Move to the next cycle position
        rail_offset += 1  # Move to the next character in the ciphertext

    return ''.join(plaintext).lower()  # Return the plaintext as a string

# Example usage
if __name__ == "__main__":
    depth = 2  # Number of rails
    plaintext = input("Enter the plaintext: ")

    # Encrypt the plaintext
    encrypted_text = encrypt_rail_fence(plaintext, depth)
    print("Encrypted Ciphertext:", encrypted_text)

    # Decrypt the ciphertext
    decrypted_text = decrypt_rail_fence(encrypted_text, depth)
    print("Decrypted Text:", decrypted_text)
