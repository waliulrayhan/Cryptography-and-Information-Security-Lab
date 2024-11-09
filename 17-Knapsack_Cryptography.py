import random
import math
from sympy import randprime

# Generate a superincreasing knapsack
def generate_superincreasing_knapsack(n):
    knapsack = [1]  # Start with the first element as 1
    for _ in range(n - 1):
        knapsack.append(sum(knapsack) + 1)  # Add elements to make the knapsack superincreasing
    return knapsack

# Generate a superincreasing knapsack
knapsack = generate_superincreasing_knapsack(7)  # For demonstration, we use knapsack size of 7

# Choose a value for n (which is used in public/private key generation)
n = sum(knapsack) + 5  # Sum of all knapsack elements + 5

# Generate the public key (e) such that gcd(e, phi(n)) = 1
r = randprime(1, n - 1)  # Random number chosen for encryption
while math.gcd(n, r) != 1:  # Ensure r is coprime with n
    r = random.randint(1, n - 1)

# Perform the random permutation of knapsack elements for the public key
random_permutation = random.sample(range(7), 7)  # Shuffle the knapsack for security
print("Random Permutation:", random_permutation)

# Now generate the public key as the transformed knapsack values under modulus
public_key = [(r * value) % n for value in knapsack]
print("Public Key:", public_key)

# Generating the private key (which is the inverse of r modulo n)
private_key = pow(r, -1, n)

# Encrypting a message
plaintext = "R"  # Example plaintext character
binary = format(ord(plaintext), '08b')  # Convert the character to binary
print("The binary form of the character is:", binary)

ciphertext = 0
for i in range(len(knapsack)):  # Iterate through the knapsack
    bit = int(binary[i])  # Convert the bit at position i in binary to an integer
    term = public_key[i] * bit  # Multiply public key with the bit
    ciphertext += term  # Add the term to the ciphertext

print("The corresponding ciphertext is:", ciphertext)

# Decrypting the ciphertext
sprime = (pow(r, -1, n) * ciphertext) % n  # Apply modular inverse and decrypt

# Reconstruct the original message using the private key
xi = []
for i in range(len(knapsack)-1, -1, -1):
    if sprime >= knapsack[i]:
        xi.insert(0, 1)
        sprime -= knapsack[i]
    else:
        xi.insert(0, 0)

# Perform reverse random permutation on the decrypted bits
new_temp = [0] * len(xi)
for i in range(len(xi)):
    new_temp[i] = xi[random_permutation[i]]

# Convert binary back to decimal
binary = ''.join([str(bit) for bit in new_temp])
decimal = int(binary, 2)  # Convert binary to decimal
character = chr(decimal)  # Convert decimal to character
print("The corresponding plaintext is:", character)
