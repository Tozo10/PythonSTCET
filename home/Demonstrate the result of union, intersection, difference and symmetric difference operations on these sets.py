# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Generate sets of prime, even, and odd numbers
prime_numbers = set(x for x in range(2, 101) if is_prime(x))
even_numbers = set(x for x in range(2, 101) if x % 2 == 0)
odd_numbers = set(x for x in range(2, 101) if x % 2 != 0)

# Demonstrate set operations
print("Prime Numbers:", prime_numbers)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)

# Union of prime_numbers and even_numbers
union_result = prime_numbers.union(even_numbers)
print("Union of Prime Numbers and Even Numbers:", union_result)

# Intersection of prime_numbers and odd_numbers
intersection_result = prime_numbers.intersection(odd_numbers)
print("Intersection of Prime Numbers and Odd Numbers:", intersection_result)

# Difference between even_numbers and odd_numbers
difference_result = even_numbers.difference(odd_numbers)
print("Difference between Even Numbers and Odd Numbers:", difference_result)

# Symmetric difference between even_numbers and prime_numbers
symmetric_difference_result = even_numbers.symmetric_difference(prime_numbers)
print("Symmetric Difference between Even Numbers and Prime Numbers:", symmetric_difference_result)
