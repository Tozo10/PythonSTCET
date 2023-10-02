def factors_except_self(number):
    factors = []
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)
    return factors

# Example usage:
num = 12  # Replace with the number for which you want to find the factors
factor_list = factors_except_self(num)
print(f"Factors of {num} except itself: {factor_list}")
