# Dictionary of names of students and their marks in 4 subjects
student_marks = {
    'Alice': [85, 90, 78, 95],
    'Bob': [92, 88, 75, 89],
    'Charlie': [78, 85, 88, 92],
    'David': [90, 92, 84, 88]
}

# Create a new dictionary with names and total marks
student_total_marks = {}
topper = None
top_score = -1  # Initialize with a negative value

# Calculate total marks for each student and populate the new dictionary
for student, marks in student_marks.items():
    total_marks = sum(marks)
    student_total_marks[student] = total_marks

    # Check if this student has the highest total marks
    if total_marks > top_score:
        topper = student
        top_score = total_marks

# Print the new dictionary
print("Student Total Marks:", student_total_marks)

# Print the topper and their score
print(f"Topper: {topper}, Score: {top_score}")
