# myenv\Scripts\activate  # For Windows

# Import the necessary libraries
import random  # For generating random integers
from sympy import primitive_root, randprime  # sympy for symbolic mathematics to find primitive roots and generate random primes

# Function to generate ElGamal keys
def generate_keys():
    # Generate a random large prime number p
    prime = randprime(124, 10**3)  # Generate a prime number between 124 and 1000 using sympy's randprime function
    
    # Find the primitive root of p
    root = primitive_root(prime)  # This function returns a primitive root of the prime number p
    
    # Choose a random private key d (in range 1 to p-2)
    d = random.randint(1, prime-2)  # Randomly generate the private key d, which is an integer between 1 and p-2
    
    # Calculate public key e = (root^d) % p
    e = pow(root, d, prime)  # The public key e is calculated as root raised to the power of d, modulo p

    # Return the public key (prime, root, e) and the private key d
    return (prime, root, e), d

# Function to encrypt the message using ElGamal
def encrypt(public_key, plaintext):
    prime, root, e = public_key  # Unpack the public key components (prime p, root g, public key e)
    ciphertext = []  # List to store the ciphertext pairs
    
    # Loop over each character in the plaintext
    for char in plaintext:
        r = random.randint(1, 10)  # Choose a random integer r for each encryption
        
        # Calculate the first part of the ciphertext: c1 = (root^r) % p
        ciphertext1 = pow(root, r, prime)
        
        # Calculate the second part of the ciphertext: c2 = (m * (e^r)) % p
        # where m is the ASCII value of the character and e^r is the public key raised to the power of r
        ciphertext2 = (ord(char) * pow(e, r, prime)) % prime
        
        # Append the pair (c1, c2) to the ciphertext list
        ciphertext.append((ciphertext1, ciphertext2))
    
    # Return the complete ciphertext as a list of tuples (c1, c2)
    return ciphertext

# Function to decrypt the ciphertext using ElGamal
def decrypt(private_key, public_key, ciphertext):
    prime, root, e = public_key  # Unpack the public key components
    d = private_key  # The private key d
    plaintext = ""  # Initialize an empty string to store the decrypted message
    
    # Loop through each pair (c1, c2) in the ciphertext
    for pair in ciphertext:
        ciphertext1, ciphertext2 = pair  # Unpack the pair into ciphertext1 and ciphertext2
        
        # Calculate the shared secret value: s = (c1^d) % p
        value = pow(ciphertext1, d, prime)
        
        # Calculate the multiplicative inverse of the value modulo p
        # This will be used to "undo" the effect of the public key's encryption
        multinv = pow(value, -1, prime)
        
        # Decrypt the character: m = (c2 * multiplicative inverse of value) % p
        decrypt_char = (ciphertext2 * multinv) % prime
        
        # Convert the decrypted integer back into a character and append it to the plaintext
        plaintext += chr(decrypt_char)
    
    # Return the decrypted plaintext string
    return plaintext

# Main logic to run the encryption and decryption
if __name__ == "__main__":
    # Generate public and private keys
    public_key, private_key = generate_keys()
    
    # Print the generated public and private keys
    print(f"Public Key (p, g, e): {public_key}")
    print(f"Private Key (d): {private_key}")
    
    # Example message to encrypt
    message = input("Enter the message: ")  # Take the message input from the user
    print(f"Original message: {message}")
    
    # Encrypt the message using the public key
    encrypted_message = encrypt(public_key, message)
    print(f"Encrypted message: {encrypted_message}")
    
    # Decrypt the encrypted message using the private key
    decrypted_message = decrypt(private_key, public_key, encrypted_message)
    print(f"Decrypted message: {decrypted_message}")
