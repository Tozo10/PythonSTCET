# Prompt the user to enter a string
user_input = input("Enter a string: ")

# Convert the input string to lowercase to treat uppercase and lowercase letters as the same
user_input = user_input.lower()

# Create an empty list to store letter frequencies as tuples
letter_frequencies = []

# Iterate through the characters in the string
for char in user_input:
    # Check if the character is a letter
    if char.isalpha():
        # Check if the letter is already in the list
        found = False
        for i in range(len(letter_frequencies)):
            if letter_frequencies[i][0] == char:
                letter_frequencies[i] = (char, letter_frequencies[i][1] + 1)
                found = True
                break
        if not found:
            letter_frequencies.append((char, 1))

# Sort the list of tuples by the first element (letters) in alphabetical order
letter_frequencies.sort()

# Print the letter frequencies
print("Letter frequencies in alphabetical order:")
for letter, frequency in letter_frequencies:
    print(f"{letter}: {frequency}")
