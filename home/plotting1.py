import matplotlib.pyplot as plt

def draw_multiple_points():
    x_number_list = [1, 4, 9, 16, 25]
    y_number_list = [1, 2, 3, 4, 5]
    plt.scatter(x_number_list, y_number_list, s=10)
    plt.title("Extract Number Root")
    plt.xlabel("Number")
    plt.ylabel("Extract Root of Number")
    plt.show()

if __name__ == '__main__':
    draw_multiple_points()
