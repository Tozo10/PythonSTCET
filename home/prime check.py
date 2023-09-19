num = int(input("Enter a number: "))
factor_count = 0

if num <= 1:
    print(num," Not a prime number")
else:
    for i in range(1, num + 1):
        if num % i == 0:
            factor_count += 1
        if factor_count > 2:
            break

    if factor_count == 2:
       print(num," a prime number")
    else:
       print(num," Not a prime number")
