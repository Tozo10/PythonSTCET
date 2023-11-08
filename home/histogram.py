import matplotlib.pyplot as plt

# Example data (replace with your own data)
x = [1, 2, 3, 4, 5]  # Data values
y = [5, 12, 8, 17, 22]  # Frequencies

# Create a histogram
plt.bar(x, y, width=0.8, color='blue', alpha=0.7)

# Add labels and a title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Custom Histogram Example')

# Show the plot
plt.show()
