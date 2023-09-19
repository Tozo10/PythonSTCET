# Sample lists of color names and color codes
color_names = ["Red", "Green", "Blue", "Yellow"]
color_codes = ["#FF0000", "#008000", "#0000FF", "#FFFF00"]

# Create an empty dictionary to store the mapping
color_dict = {}

# Check if the lengths of both lists are the same
if len(color_names) == len(color_codes):
    # Iterate through the lists and map them into the dictionary
    for i in range(len(color_names)):
        color_dict[color_names[i]] = color_codes[i]
    print("Color Dictionary:", color_dict)
else:
    print("Lists have different lengths. Cannot map into a dictionary.")
