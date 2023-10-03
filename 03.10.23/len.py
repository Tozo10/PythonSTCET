f = open('test.py','r')

c = 0
d = 0
for i in f.readlines():
    print(i)
    c+=1
    
print(c)
f.close()
f = open('test.py','r')
for i in f.readlines():
    for j in i.split():
        print(j,", ",end =" ")
        d+=1
    print()
print(d)
