import filecmp

f1 = "test.py"
f2 = "Intro1.txt"

# shallow comparison
result = filecmp.cmp(f1, f2)
print(result)
# deep comparison
result = filecmp.cmp(f1, f2, shallow=False)
print(result)
