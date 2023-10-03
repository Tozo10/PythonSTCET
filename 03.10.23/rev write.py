f1 = open('test.py','r')
f2 = open('test1.py','w')
c = f1.read()
r = c[::-1]
f2.write(r)
f2.close()
f2 = open('test1.py','r')
for i in f2.readlines():
   print(i)
f1.close()
f2.close()
