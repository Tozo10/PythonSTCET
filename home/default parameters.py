# Function with default arguments
def greet(name="Guest", message="Hello"):
    print(f"{message}, {name}!")

# Calling the function with arguments
greet("Alice", "Hi")

# Calling the function without providing values for parameters
greet()  # Uses the default values

# Calling the function with only one argument
greet("Bob")  # Uses the default value for 'message'

# Calling the function with named arguments
greet(message="Hey", name="Carol")
