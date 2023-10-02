import math

# Function to calculate the GCD of a set of numbers using recursion
def gcd_of_set(numbers):
    if len(numbers) == 2:
        return math.gcd(numbers[0], numbers[1])
    else:
        # Calculate GCD of the first two numbers
        gcd_result = math.gcd(numbers[0], numbers[1])
        # Recursively calculate GCD with the rest of the numbers
        return gcd_of_set([gcd_result] + numbers[2:])

# Example usage:
num_set = {12, 18, 24, 36}  # Replace with your set of numbers
gcd_result = gcd_of_set(list(num_set))
print(f"GCD of {num_set} is {gcd_result}")
