string = input("Enter a string: ")
target_letter = input("Enter the letter to count: ")

count = 0
for char in string:
    if char == target_letter:
        count += 1

print(f"The letter '{target_letter}' appears {count} times in the string.")
