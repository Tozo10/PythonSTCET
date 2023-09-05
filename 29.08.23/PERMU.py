from itertools import permutations


a = "ABCD"
b= ['a','b','c']
p = permutations(b)


for j in list(p):
    print(j)

a = input("Enter string : ")
b = a[::-1]
if a in b:
    print("PALLINDROME : ")
else :
    print("NOT PALLINDROME : ")
    


h = eval(input("Enter diamond's height: "))

for x in range(h):
    print(" " * (h - x), "*" * (2*x + 1))
for x in range(h - 2, -1, -1):
    print(" " * (h - x), "*" * (2*x + 1))
