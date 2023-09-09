print("Armstrong numbers between 1 and 1000:")

for num in range(1, 1001):
    temp = num
    num_digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits
        temp //= 10

    if total == num:
        print(num)
