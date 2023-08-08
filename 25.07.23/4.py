import math
n = (int)(input("Enter the value of n : "))
r = (int)(input("Enter the value of r : "))
a = (math.factorial(n))/(math.factorial(n-r) * math.factorial(r))
print (a)
