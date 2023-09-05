l = []
print("Enter 5 favourite.\n")
for i in range(5):
    n = input(f"Play :{i+1} ")
    l.append(n)
print ("\n Subscript Value")
for i in range (len (l)):
    print("%9d %-25s"%(i+1,l[i]))
