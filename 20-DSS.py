from Crypto.Signature import DSS  # Import the DSS module for Digital Signature Algorithm (DSA) from PyCryptodome.
from Crypto.Hash import SHA256  # Import SHA256 hash function for creating message digests.
from Crypto.PublicKey import DSA  # Import DSA for generating private and public keys for signing and verifying.
from Crypto.Random import get_random_bytes  # Import for generating random bytes, though it's not used in this code.

# Function to generate DSA keys
def generate_keys():
    # Step 1: Generate a DSA private key
    private_key = DSA.generate(2048)  # Generate a private key using the DSA algorithm with a 2048-bit key length.

    # Step 2: Extract the public key from the private key
    public_key = private_key.publickey()  # The public key is derived from the private key.

    return private_key, public_key  # Return the generated private and public keys.

# Function to sign a message using DSA
def sign_message(private_key, message):
    # Step 1: Hash the message using SHA-256
    hash_obj = SHA256.new(message.encode('utf-8'))  # Hash the message with SHA-256. The message is encoded as bytes before hashing.

    # Step 2: Create the signature object using the private key
    signer = DSS.new(private_key, 'fips-186-3')  # DSS.new() initializes a signing object with the private key and the FIPS-186-3 standard.

    # Step 3: Sign the hashed message
    signature = signer.sign(hash_obj)  # The signature is generated by signing the hash of the message.

    return signature  # Return the generated signature.

# Function to verify a signature using DSA
def verify_signature(public_key, message, signature):
    # Step 1: Hash the message using SHA-256
    hash_obj = SHA256.new(message.encode('utf-8'))  # Hash the message using SHA-256 to create the message digest.

    # Step 2: Create the verifier object using the public key
    verifier = DSS.new(public_key, 'fips-186-3')  # Create a verifier object using the public key and FIPS-186-3 standard.

    try:
        # Step 3: Verify the signature
        verifier.verify(hash_obj, signature)  # The verifier object checks if the signature matches the hash of the message.
        print("The signature is valid.")  # If the signature is valid, print a confirmation message.
    except ValueError:
        # Step 4: Handle the case where the signature is invalid
        print("The signature is not valid.")  # If the signature doesn't match, print an invalid signature message.

# Example usage
if __name__ == "__main__":
    # Step 1: Generate DSA keys (private and public)
    private_key, public_key = generate_keys()  # Generate the private and public keys.

    # Print out the private key in PEM format
    print("Private Key:")
    print(private_key.export_key().decode('utf-8'))  # The private key is exported and decoded to UTF-8 string for readability.

    # Print out the public key in PEM format
    print("Public Key:")
    print(public_key.export_key().decode('utf-8'))  # The public key is exported and decoded to UTF-8 string.

    # Step 2: Define the message to be signed
    message = input("\nEnter the message to sign: ")  # Input the message to be signed.
    print(f"\nOriginal message: {message}")  # Print the original message.

    # Step 3: Sign the message using the private key
    signature = sign_message(private_key, message)  # Sign the message using the private key.
    print(f"\nSignature (in bytes): {signature}")  # Print the signature generated by DSA.

    # Step 4: Verify the signature using the public key
    verify_signature(public_key, message, signature)  # Verify the signature using the public key.
