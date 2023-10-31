f =open("demofile.txt", "r")
print(f.read())
f.seek(0)
print(f.readline())
print(f.readline())
f.seek(0)
print(f.read(5))
f.seek(0)
for x in f:
  print(x)
f.close()
#Append content in the above mentioned file.
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
#Check whether a file exists or not. Delete it.
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
 print("The file does not exist")
#Count the number of words in a file.
words=0
with open("demo.txt”,"r") as f:
 for line in f:
    w=line.split()
    words+=len(words)
 max_len=len(max(w,key=len))
 print(words)