import random  # Importing the random module to generate random numbers, which will be used for private keys.

# Function to generate a large prime p and generator g
def generate_parameters(bits=256):
    # Generate a large prime number p (a small prime for example purposes)
    p = 23  # In practice, p should be a large prime number (typically hundreds of digits long)
    g = 5   # In practice, g should be a primitive root modulo p. A small value for demonstration purposes.

    return p, g  # Return the prime number p and the generator g

# Function to generate a private key (a random integer in the range [1, p-2])
def generate_private_key(p):
    return random.randint(2, p-2)  # Randomly select a private key from the range [2, p-2] (inclusive)

# Function to generate a public key based on the private key
def generate_public_key(g, private_key, p):
    return pow(g, private_key, p)  # Public key = g^private_key mod p (using modular exponentiation)

# Function to compute the shared secret
def compute_shared_secret(public_key_other, private_key_self, p):
    return pow(public_key_other, private_key_self, p)  # Shared secret = (public_key_other)^private_key_self mod p

# Example usage of the Diffie-Hellman Key Exchange
if __name__ == "__main__":
    # Step 1: Generate public parameters (p and g)
    p, g = generate_parameters()  # Generate the prime p and the generator g
    print(f"Public Parameters: p = {p}, g = {g}")  # Print the generated public parameters

    # Step 2: Each party generates a private key
    private_key_A = generate_private_key(p)  # Generate a private key for Party A
    private_key_B = generate_private_key(p)  # Generate a private key for Party B

    print(f"Private Key of Party A: {private_key_A}")  # Print the private key of Party A
    print(f"Private Key of Party B: {private_key_B}")  # Print the private key of Party B

    # Step 3: Each party generates a public key
    public_key_A = generate_public_key(g, private_key_A, p)  # Party A generates their public key
    public_key_B = generate_public_key(g, private_key_B, p)  # Party B generates their public key

    print(f"Public Key of Party A: {public_key_A}")  # Print Party A's public key
    print(f"Public Key of Party B: {public_key_B}")  # Print Party B's public key

    # Step 4: Each party computes the shared secret
    shared_secret_A = compute_shared_secret(public_key_B, private_key_A, p)  # Party A computes the shared secret
    shared_secret_B = compute_shared_secret(public_key_A, private_key_B, p)  # Party B computes the shared secret

    print(f"Shared Secret computed by Party A: {shared_secret_A}")  # Print the shared secret computed by Party A
    print(f"Shared Secret computed by Party B: {shared_secret_B}")  # Print the shared secret computed by Party B

    # Check if both parties have the same shared secret
    if shared_secret_A == shared_secret_B:
        print("The shared secret is the same for both parties.")  # If both parties' secrets match, print success
    else:
        print("Error: The shared secrets do not match.")  # If the secrets don't match, print error
