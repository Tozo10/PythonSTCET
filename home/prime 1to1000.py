print("Prime numbers between 1 and 1000:")

for num in range(2, 1001):
    factor_count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            factor_count += 1

    if factor_count == 2:
        print(num)
