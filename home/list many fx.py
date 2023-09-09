# Create two lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

# Append an item to list1
list1.append(4)
print("List 1 after appending 4:", list1)

# Append an item of length two to list2
list2.append('de')
print("List 2 after appending 'de':", list2)

# Use extend to concatenate two lists
list1.extend(list2)
print("Concatenated list using extend:", list1)

# Find the index of an item
index = list1.index(2)
print("Index of 2:", index)

# Insert 'six' at index 5
list1.insert(5, 'six')
print("List after inserting 'six' at index 5:", list1)

# Delete the last item
del list1[-1]
print("List after deleting the last item:", list1)

# Delete the item with index 4
del list1[4]
print("List after deleting item at index 4:", list1)

# Remove the item 'six'
list1.remove('six')
print("List after removing 'six':", list1)

# Reverse the list
list1.reverse()
print("Reversed list:", list1)

# Sort the list
list1.sort()
print("Sorted list:", list1)
