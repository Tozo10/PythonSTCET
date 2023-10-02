# star_patterns.py

def print_square(rows):
    for i in range(rows):
        print('* ' * rows)

def print_triangle(rows):
    for i in range(1, rows + 1):
        print('* ' * i)

def print_reverse_triangle(rows):
    for i in range(rows, 0, -1):
        print('* ' * i)


def print_left_sided_right_triangle(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '*' * i)

def print_pyramid(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)

def print_diamond(rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + '* ' * i)
    for i in range(rows - 1, 0, -1):
        print(' ' * (rows - i) + '* ' * i)

def print_alternating(rows):
    for i in range(1, rows + 1):
        if i % 2 == 0:
            print(' ' * (rows - i) + '* ' * i)
        else:
            print('* ' * i)

# Example usage:
if __name__ == "__main__":
    rows = 5  # Replace with the number of rows you want in the patterns
    print("Square:")
    print_square(rows)
    
    print("\nTriangle:")
    print_triangle(rows)
    
    print("\nReverse Triangle:")
    print_reverse_triangle(rows)
    
    print("\nLeft-Sided Right Triangle:")
    print_left_sided_right_triangle(rows)
    
    print("\nPyramid:")
    print_pyramid(rows)
    
    print("\nDiamond:")
    print_diamond(rows)
    
    print("\nAlternating Rows:")
    print_alternating(rows)
