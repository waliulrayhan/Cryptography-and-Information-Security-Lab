from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from Crypto.PublicKey import DSA
from Crypto.Random import get_random_bytes

# Function to generate DSA keys
def generate_keys():
    # Generate a DSA private key
    private_key = DSA.generate(2048)

    # Extract the public key
    public_key = private_key.publickey()

    return private_key, public_key

# Function to sign a message using DSA
def sign_message(private_key, message):
    # Hash the message using SHA-256
    hash_obj = SHA256.new(message.encode('utf-8'))

    # Create the signature object using the private key
    signer = DSS.new(private_key, 'fips-186-3')

    # Sign the message
    signature = signer.sign(hash_obj)

    return signature

# Function to verify a signature using DSA
def verify_signature(public_key, message, signature):
    # Hash the message using SHA-256
    hash_obj = SHA256.new(message.encode('utf-8'))

    # Create the verifier object using the public key
    verifier = DSS.new(public_key, 'fips-186-3')

    try:
        # Verify the signature
        verifier.verify(hash_obj, signature)
        print("The signature is valid.")
    except ValueError:
        print("The signature is not valid.")

# Example usage
if __name__ == "__main__":
    # Generate DSA keys
    private_key, public_key = generate_keys()

    print("Private Key:")
    print(private_key.export_key().decode('utf-8'))

    print("Public Key:")
    print(public_key.export_key().decode('utf-8'))

    # Sample message
    message = "Hello, this is a message to sign with DSA."
    print(f"\nOriginal message: {message}")

    # Sign the message
    signature = sign_message(private_key, message)
    print(f"\nSignature (in bytes): {signature}")

    # Verify the signature
    verify_signature(public_key, message, signature)
