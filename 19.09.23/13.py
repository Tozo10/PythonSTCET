import random
f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0
for r in range(1,6001):
    f = random.randrange(1,7)
    if f == 1:
        f1 += 1
    elif f == 2 :
        f2 += 1
    elif f == 3 :
        f3 += 1
    elif f == 4:
        f4 += 1
    elif f == 5:
        f5 += 1
    elif f == 6:
        f6 += 1
print(f"f1 : {f1}, f2 : {f2}, f3 : {f3}, f4 : {f4}, f5 : {f5}, f6 : {f6}")
