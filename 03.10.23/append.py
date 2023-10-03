f = open('Intro1.txt','a')
f.write("Python")
f.close()
f = open('Intro1.txt','r')
for i in f.readlines():
    print(i)
f.close()
