# Create a set of even numbers in the range 1-10
even_numbers = set(range(2, 11, 2))

# Create a set of composite numbers in the range 1-20
composite_numbers = set([4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20])

# Demonstrate the use of functions on the sets
print("Even Numbers Set:", even_numbers)
print("Composite Numbers Set:", composite_numbers)

# Use all() to check if all elements in the set are even
all_even = all(x % 2 == 0 for x in even_numbers)
print("All elements in even_numbers are even:", all_even)

# Use issuperset() to check if even_numbers is a superset of {4, 8}
is_superset = even_numbers.issuperset({4, 8})
print("even_numbers is a superset of {4, 8}:", is_superset)

# Use issubset() to check if {6, 8} is a subset of composite_numbers
is_subset = {6, 8}.issubset(composite_numbers)
print("{6, 8} is a subset of composite_numbers:", is_subset)

# Use len() to get the length of the sets
even_len = len(even_numbers)
composite_len = len(composite_numbers)
print("Length of even_numbers:", even_len)
print("Length of composite_numbers:", composite_len)

# Use sum() to calculate the sum of elements in even_numbers
even_sum = sum(even_numbers)
print("Sum of elements in even_numbers:", even_sum)
