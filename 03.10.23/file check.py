import os.path

path = input("Enter the path of the file : ")

check_file = os.path.isfile(path)

print(check_file)
