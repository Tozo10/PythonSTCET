t1 =(int(input("Enter x1 : ")),int(input("Enter y1 : ")))
t2 = (int(input("Enter x2 : ")), int (input("Enter y2 : ")))
def ed(t1, t2):
    d = ((t1[0]-t2[0])**2+(t1[1] - t2[1]**2)**0.5)
    return d
def md(t1,t2):
    d = abs(t1[0]-t2[0])+abs(t1[1]-t2[1])
    return d
print("Eucl = ",ed(t1,t2))
print("Man = ",md(t1,t2))
