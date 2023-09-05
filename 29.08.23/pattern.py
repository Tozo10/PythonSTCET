n = int(input("Enter the number of rows : "));
ns = n -1
hs =  1
a = 65
for i in range (0,n):
    for j in range(ns,0,-1):
        print(' ',end = " "),
    for k in range (1,hs+1):
        if k % 2 != 0 :
            print(chr(a),end= " ")
            a = a + 1
        else:
            print(" ",end = " ")
    hs = ns + 2
    ns = ns - 1
    print()
        
        
