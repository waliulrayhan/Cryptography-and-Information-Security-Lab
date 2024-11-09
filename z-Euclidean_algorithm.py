import pandas as pd

# Function for the Extended Euclidean Algorithm to find GCD and coefficients s and t
def extended_euclidean(a, b):
    # Initialize variables to keep track of the coefficients
    steps = []
    s_prev, s_curr = 1, 0
    t_prev, t_curr = 0, 1
    r_prev, r_curr = a, b

    while r_curr != 0:
        quotient = r_prev // r_curr
        r_next = r_prev - quotient * r_curr
        s_next = s_prev - quotient * s_curr
        t_next = t_prev - quotient * t_curr

        # Append the current state to the steps list
        steps.append([quotient, r_prev, r_curr, r_next, s_prev, s_curr, s_next, t_prev, t_curr, t_next])

        # Update variables for the next iteration
        r_prev, r_curr = r_curr, r_next
        s_prev, s_curr = s_curr, s_next
        t_prev, t_curr = t_curr, t_next

    # Append the final step where r_curr becomes 0
    steps.append([None, r_prev, r_curr, None, s_prev, s_curr, None, t_prev, t_curr, None])

    # Create a DataFrame to display the steps
    columns = ['q', 'r1', 'r2', 'r', 's1', 's2', 's', 't1', 't2', 't']
    df = pd.DataFrame(steps, columns=columns)

    # Return the results
    return df, r_prev, s_prev, t_prev

# # Example usage
# a = 161
# b = 28
# df, gcd, s, t = extended_euclidean(a, b)
# print("\nExtended Euclidean Algorithm Table:")
# print(df)
# print(f"\nGCD: {gcd}")
# print(f"s: {s}")
# print(f"t: {t}")

# Function to find the multiplicative inverse using the Extended Euclidean Algorithm
def multiplicative_inverse(a, mod):
    _, gcd, s, _ = extended_euclidean(a, mod)

    if gcd != 1:
        # No multiplicative inverse exists if GCD is not 1
        print(f"\nNo multiplicative inverse exists for {a} modulo {mod}.")
        return None
    else:
        # Ensure the result is positive by using modulo operation
        inverse = s % mod
        print(f"\nThe multiplicative inverse of {a} modulo {mod} is: {inverse}")
        return inverse

# Example usage for finding the multiplicative inverse
a = 3
mod = 26
inverse = multiplicative_inverse(a, mod)
