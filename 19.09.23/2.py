#recursive
x = int(input("Enter a number : "))
p = 1
def fact(x):
    pr = 1
    for i in range (1,x+1):
        pr*= i
    return pr
def factrec(x):
    pr = 1
    if x == 1:
        return 1
    pr = pr * x * factrec(x-1)
    return pr
pr = factrec(x)
print(pr)
