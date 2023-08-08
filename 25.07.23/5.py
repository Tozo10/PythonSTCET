import cmath
import math
a = (float)(input("Enter the value of a : "))
b = (float)(input("Enter the value of b : "))
c = (float)(input("Enter the value of c : "))
d = (b**2)-(4*a*c)
if(d < 0) :
    x1 = (-b-cmath.sqrt(d))/(2*a)
    x2 = (-b+cmath.sqrt(d))/(2*a)
    print (x1)
    print (x2)
else :
     x1 = (-b-math.sqrt(d))/(2*a)
     x2 = (-b+math.sqrt(d))/(2*a)
     print (x1)
     print (x2)
