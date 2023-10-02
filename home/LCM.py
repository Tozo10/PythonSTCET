import math

# Function to find the LCM of two numbers
def find_lcm(x, y):
    return x * y // math.gcd(x, y)

# Function to find the LCM of a list of numbers
def find_lcm_of_list(numbers):
    lcm_result = numbers[0]
    for num in numbers[1:]:
        lcm_result = find_lcm(lcm_result, num)
    return lcm_result

# Example usage:
numbers = [12, 18, 24, 36]  # Replace with the list of numbers for which you want to find the LCM
lcm = find_lcm_of_list(numbers)
print(f"LCM of {numbers} is {lcm}")
