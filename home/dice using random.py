import random

# Initialize a dictionary to store the count of each dice number
dice_counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# Simulate rolling the dice 10,000 times
rolls = 10000
for _ in range(rolls):
    # Generate a random number between 1 and 6 (inclusive) to simulate a dice roll
    dice_number = random.randint(1, 6)
    
    # Increment the count for the corresponding dice number
    dice_counts[dice_number] += 1

# Print the results
print(f"Results after {rolls} rolls:")
for number, count in dice_counts.items():
    print(f"Number {number}: {count} times")
