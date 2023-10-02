import math

# Function to calculate permutations (nPr)
def calculate_permutation(n, r):
    if n < r:
        return 0  # Return 0 if n < r
    else:
        return math.factorial(n) // math.factorial(n - r)

# Function to calculate combinations (nCr)
def calculate_combination(n, r):
    if n < r:
        return 0  # Return 0 if n < r
    else:
        return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# Example usage:
n = 5  # Replace with the values of n and r for which you want to calculate nPr and nCr
r = 2
permutation_result = calculate_permutation(n, r)
combination_result = calculate_combination(n, r)
print(f"{n}P{r} = {permutation_result}")
print(f"{n}C{r} = {combination_result}")
