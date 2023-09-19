d = {}
d2 = {}
for i in range(3):
    x = input('enter name : ')
    y = input('enter id : ')
    z = list(map(str,input('enter product : ').split()))
    d['name']= x
    d['id'] = y
    d['product'] = z
    d2[i+1]  = d
print(d2)
