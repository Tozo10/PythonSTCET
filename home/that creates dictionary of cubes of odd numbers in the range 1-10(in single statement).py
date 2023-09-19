# Create a dictionary of cubes of odd numbers in the range 1-10
odd_cubes_dict = {num: num**3 for num in range(1, 11) if num % 2 != 0}

# Print the resulting dictionary
print(odd_cubes_dict)
