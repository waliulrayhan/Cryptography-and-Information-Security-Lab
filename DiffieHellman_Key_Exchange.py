import random

# Function to generate a large prime p and generator g
def generate_parameters(bits=256):
    # Generate a large prime number p (a small prime for example purposes)
    p = 23  # In practice, p should be a large prime number
    g = 5   # In practice, g should be a primitive root modulo p

    return p, g

# Function to generate a private key (a random integer in the range [1, p-2])
def generate_private_key(p):
    return random.randint(2, p-2)

# Function to generate a public key based on the private key
def generate_public_key(g, private_key, p):
    return pow(g, private_key, p)

# Function to compute the shared secret
def compute_shared_secret(public_key_other, private_key_self, p):
    return pow(public_key_other, private_key_self, p)

# Example usage of the Diffie-Hellman Key Exchange
if __name__ == "__main__":
    # Step 1: Generate public parameters (p and g)
    p, g = generate_parameters()
    print(f"Public Parameters: p = {p}, g = {g}")

    # Step 2: Each party generates a private key
    private_key_A = generate_private_key(p)
    private_key_B = generate_private_key(p)

    print(f"Private Key of Party A: {private_key_A}")
    print(f"Private Key of Party B: {private_key_B}")

    # Step 3: Each party generates a public key
    public_key_A = generate_public_key(g, private_key_A, p)
    public_key_B = generate_public_key(g, private_key_B, p)

    print(f"Public Key of Party A: {public_key_A}")
    print(f"Public Key of Party B: {public_key_B}")

    # Step 4: Each party computes the shared secret
    shared_secret_A = compute_shared_secret(public_key_B, private_key_A, p)
    shared_secret_B = compute_shared_secret(public_key_A, private_key_B, p)

    print(f"Shared Secret computed by Party A: {shared_secret_A}")
    print(f"Shared Secret computed by Party B: {shared_secret_B}")

    # Check if both parties have the same shared secret
    if shared_secret_A == shared_secret_B:
        print("The shared secret is the same for both parties.")
    else:
        print("Error: The shared secrets do not match.")
