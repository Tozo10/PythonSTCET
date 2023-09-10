# Create an empty list to represent the queue
queue = []

# Function to check if the queue is empty
def is_empty(queue):
    return len(queue) == 0

# Function to enqueue an item to the queue
def enqueue(queue, item):
    queue.append(item)

# Function to dequeue an item from the queue
def dequeue(queue):
    if not is_empty(queue):
        return queue.pop(0)
    else:
        print("Queue is empty.")
        return None

# Function to get the size of the queue
def size(queue):
    return len(queue)

# Enqueue elements
enqueue(queue, 1)
enqueue(queue, 2)
enqueue(queue, 3)

# Check the size of the queue
print("Queue size:", size(queue))

# Dequeue elements
print("Dequeued item:", dequeue(queue))
print("Dequeued item:", dequeue(queue))

# Check the size again
print("Queue size after dequeue:", size(queue))
