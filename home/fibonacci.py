print("Fibonacci numbers between 1 and 1000:")

a, b = 0, 1
while a <= 1000:
    print(a)
    a, b = b, a + b
