import matplotlib.pyplot as plt

# Example data (replace with your own data)
labels = ['A', 'B', 'C', 'D']
sizes = [25, 30, 15, 30]  # Proportions

# Create a pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=['blue', 'green', 'orange', 'red'])

# Add a title
plt.title('Custom Pie Chart')

# Show the plot
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
