p = float(input("Enter the total amount : "))
r = float(input("Enter the interest : "))
t = int(input("Enter the time : "))
si = float((p*r*t)/100)
print("Total Interest = ",si)
to = p + si
print("Total Amount : ", to)
