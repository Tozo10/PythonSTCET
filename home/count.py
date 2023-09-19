# Create a list of numbers
numbers = [1, 2, 3, 1, 2, 3, 1, 2, 3, 4, 5]

# Create an empty list to store number frequencies as tuples
number_frequencies = []

# Iterate through the numbers in the list
for num in numbers:
    # Check if the number is already in the list
    found = False
    for i in range(len(number_frequencies)):
        if number_frequencies[i][0] == num:
            number_frequencies[i] = (num, number_frequencies[i][1] + 1)
            found = True
            break
    if not found:
        number_frequencies.append((num, 1))

# Sort the list of tuples by the first element (numbers) in ascending order
number_frequencies.sort()

# Print the number frequencies
print("Number frequencies in ascending order:")
for number, frequency in number_frequencies:
    print(f"{number}: {frequency}")
