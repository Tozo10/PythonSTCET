num = [12,23,43,(12,23),40]
c = 0
for n in num :
    if isinstance(n,tuple):
        break
    c+=1
print(c)
