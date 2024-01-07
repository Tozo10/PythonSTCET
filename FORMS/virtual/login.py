import tkinter 
import tkinter.messagebox as tkmb
import subprocess
import customtkinter as ctk
from PIL import Image
ctk.set_appearance_mode("light")
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
window = ctk.CTk()
window.title("Login")
window.geometry('900x650')
window.config(bg="#EBF8FF")

my_image = ctk.CTkImage(light_image=Image.open("STCET-Logo.png"),size = (90,90))

# Create a CTkLabel with the CTkImage
p_label = ctk.CTkLabel(window, image=my_image, text=" ",bg_color="#EBF8FF")
p_label.pack(padx=20, pady=10)

college_label = ctk.CTkLabel(window,text="St. Thomas' College of Engineering & Technology",
                             font=ctk.CTkFont(family = "Old English Text MT",size=30,weight="bold"),bg_color = "#EBF8FF",text_color="#264D61")
college_label.pack(padx = 10,pady =10)
title_label = ctk.CTkLabel(window,text="Login Form",font=ctk.CTkFont(family = "Arial",size=25,weight = "bold",),bg_color="#EBF8FF",text_color="#264D61")
title_label.pack(padx = 10,pady =(10,10))

frame = ctk.CTkFrame(window,fg_color="#FEFEFE",bg_color="#EBF8FF",corner_radius=15,border_width=2,border_color="#264D61")
frame.pack(fill = "x",padx = 100,pady = (20,50))

frame1 = ctk.CTkFrame(frame,fg_color="#E3CBB1",bg_color="#FEFEFE",corner_radius=15,border_width=2,border_color="#264D61")
frame1.pack(fill = "x",padx = 50,pady = 20)

# Create username and password entry widgets
login_label = ctk.CTkLabel(frame1,text="Login Now",font=ctk.CTkFont(family = "Arial",size=25,weight = "bold"),text_color="#264d61")
login_label.grid(row = 0,column = 0,columnspan = 2,padx = 20,pady = 20,sticky = "ew")

user_entry_label = ctk.CTkLabel(frame1, text="Username   :",font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 20),text_color="#264d61")
user_entry_label.grid(row = 1,column = 0,padx = (20,10),pady = 25,sticky = "ew")
user_entry = ctk.CTkEntry(frame1,fg_color= "#EBF8FF",border_color="#264d61",text_color="#264D61",
                          font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 15),height = 30,corner_radius = 15)
user_entry.grid(row = 1,column = 1,padx = (10,50),pady = 25,sticky = "ew")

pass_entry_label = ctk.CTkLabel(frame1, text="Password   :",font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 20),text_color="#264d61")
pass_entry_label.grid(row = 2,column = 0,padx = (20,10),pady =25,sticky = "ew")
user_pass = ctk.CTkEntry(frame1, show="*",fg_color= "#EBF8FF",border_color="#264d61",text_color="#264D61",
                         font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 15),height = 30,corner_radius = 15)
user_pass.grid(row = 2,column = 1,padx = (10,50),pady = 25,sticky = "ew")

# Create login button
login_button = ctk.CTkButton(frame1, text="Login", command=login,width=300,fg_color="#264D61",hover_color="#2F5E87",
                             height=30,corner_radius = 15)
login_button.grid(row = 3,column = 0,columnspan = 2,padx = 20,pady = (30,20))

rows = 4
columns = 2
for i in range(rows):
    frame1.grid_rowconfigure(i,weight=1)
for i in range(columns):
    frame1.grid_columnconfigure(i,weight=1)

# Run the main loop
window.mainloop()
