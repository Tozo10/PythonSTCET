import math
a = (float)(input("Enter a : "))
b = (float)(input("Enter b : "))
c = (float)(input("Enter c : "))
s = 0.5*(a+b+c)
d = s*(s-a)*(s-b)*(s-c)
a = math.sqrt(d)
print(a)
