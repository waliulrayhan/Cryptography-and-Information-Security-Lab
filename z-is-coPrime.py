import math

def are_coprime(a, b):
    # Two numbers are co-prime if their greatest common divisor (GCD) is 1
    return math.gcd(a, b) == 1

# Example usage
num1 = 7
num2 = 26

# Print the result with a formatted message
print(f"Are {num1} and {num2} co-prime?\n{'Yes' if are_coprime(num1, num2) else 'No'}")
