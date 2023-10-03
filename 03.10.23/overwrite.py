f = open('Intro1.txt','w')
f.write("Now It's Changed")
f.close
f = open('Intro1.txt','r')
for i in f.readlines():
    print(i)
f.close
