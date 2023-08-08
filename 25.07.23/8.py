import math
p = (float)(input("Enter the principal amt : "))
r = (float)(input("Enter the rate : "))
n = (float)(input("Enter the number of times rate applied : "))
t = (float)(input("Enter the time : "))
a = p *math.pow((1+(r/n)),(n*t))
print (a)
