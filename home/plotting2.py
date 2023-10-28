import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [2, 4, 1]
plt.plot(x, y, label='l1')

x = [1, 2, 3]
y = [8, 6, 9]
plt.plot(x, y, label='l2')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()
