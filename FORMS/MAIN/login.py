import tkinter as tk
import tkinter.messagebox as tkmb
import subprocess

# Dictionaries to store username-password pairs and corresponding Python files
users_set1 = {
    "Admin": "12345",
    "User1": "password1",
}

users_set2 = {
    "Sayantan": "54321",
    "User2": "password2",
}

# Dictionary to store username-file mappings
python_files = {
    "Admin": "test.py",
    "User1": "file_set1.py",
    "Sayantan": "testmain.py",
    "User2": "file_set2.py",
}

# Function to execute a Python file
def execute_python_file(filename):
    try:
        # Replace 'path/to/your/file.py' with the actual path to your Python file
        subprocess.run(['python', filename])
    except Exception as e:
        tkmb.showerror(title="Error", message=f"Failed to execute Python file: {str(e)}")

# defining the login function
def login():
    # Check if the entered username and password match the predefined values
    username = user_entry.get()
    password = user_pass.get()

    if username in users_set1 and password == users_set1[username]:
        tkmb.showinfo(title="Login Successful", message="You have logged in Successfully")

        # Execute the Python file after successful login
        execute_python_file(python_files.get(username, ''))

    elif username in users_set2 and password == users_set2[username]:
        tkmb.showinfo(title="Login Successful", message="You have logged in Successfully")

        # Execute the Python file after successful login
        execute_python_file(python_files.get(username, ''))

    elif username in users_set1 and password != users_set1[username]:
        tkmb.showwarning(title='Wrong password', message='Please check your password')

    elif username in users_set2 and password != users_set2[username]:
        tkmb.showwarning(title='Wrong password', message='Please check your password')

    elif username not in users_set1 and username not in users_set2:
        tkmb.showwarning(title='Wrong username', message='Please check your username')

    else:
        tkmb.showerror(title="Login Failed", message="Invalid Username and password")

# Create the main application window
app = tk.Tk()
app.title("Login Example")

# Create username and password entry widgets
user_entry_label = tk.Label(app, text="Username:")
user_entry_label.pack()
user_entry = tk.Entry(app)
user_entry.pack()

pass_entry_label = tk.Label(app, text="Password:")
pass_entry_label.pack()
user_pass = tk.Entry(app, show="*")
user_pass.pack()

# Create login button
login_button = tk.Button(app, text="Login", command=login)
login_button.pack()

# Run the main loop
app.mainloop()
