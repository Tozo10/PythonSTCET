# Create an empty list to represent the stack
stack = []

# Function to check if the stack is empty
def is_empty(stack):
    return len(stack) == 0

# Function to push an item onto the stack
def push(stack, item):
    stack.append(item)

# Function to pop an item from the stack
def pop(stack):
    if not is_empty(stack):
        return stack.pop()
    else:
        print("Stack is empty.")
        return None

# Function to get the size of the stack
def size(stack):
    return len(stack)

# Push elements onto the stack
push(stack, 1)
push(stack, 2)
push(stack, 3)

# Check the size of the stack
print("Stack size:", size(stack))

# Pop elements from the stack
print("Popped item:", pop(stack))
print("Popped item:", pop(stack))

# Check the size again
print("Stack size after pop:", size(stack))
