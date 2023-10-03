f = open('test.py','w')
f.writelines(["a = 5\n","b = 2\n","c = a + b\n","print(c)"])
f.close()
f = open('test.py','r')

print(f.read())
f.close()
