import math

# Function to calculate combinations (nCr)
def calculate_combination(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

# Function to generate Pascal's Triangle using combinations
def generate_pascals_triangle_with_ncr(rows):
    triangle = []
    for n in range(rows):
        row = [calculate_combination(n, r) for r in range(n + 1)]
        triangle.append(row)
    return triangle

# Function to print Pascal's Triangle
def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)).center(len(triangle[-1]) * 3))

# Example usage:
num_rows = 5  # Replace with the number of rows you want in Pascal's Triangle
pascals_triangle = generate_pascals_triangle_with_ncr(num_rows)
print_pascals_triangle(pascals_triangle)
