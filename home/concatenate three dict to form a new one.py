# Three dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

# Initialize a new empty dictionary
concatenated_dict = {}

# Loop through each dictionary and add its items to the concatenated_dict
for d in (dict1, dict2, dict3):
    concatenated_dict.update(d)

# Print the concatenated dictionary
print("Concatenated Dictionary (Using Loop):", concatenated_dict)
