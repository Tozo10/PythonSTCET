with open('test.py', 'r') as data_file:
    with open('test1.py', 'w') as output_file:
        for line in data_file:
            output_file.write(line.upper())
with open('test1.py', 'r') as output_file:
    for l in output_file.readlines():
            print(l)
