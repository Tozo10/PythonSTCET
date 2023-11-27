import pandas as pd
import tkinter as tk
from tkinter import messagebox

def add_user():
    # Get the user info from the form
    user_id = entry_user_id.get()
    name = entry_name.get()
    email = entry_email.get()
    age = entry_age.get()

    # Check if all the fields are filled
    if not all([user_id, name, email, age]):
        messagebox.showerror('Error', 'Please fill all the fields')
        return

    # Add the user info to the dataframe
    data = {'UserID': [user_id], 'Name': [name], 'Email': [email], 'Age': [age]}
    df = pd.DataFrame(data)

    # Append the new user info to the existing Excel file
    try:
        existing_df = pd.read_excel('users.xlsx')
        new_df = pd.concat([existing_df, df], ignore_index=True)
    except FileNotFoundError:
        new_df = df
    new_df.to_excel('users.xlsx', index=False)

    # Clear the form fields
    entry_user_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_age.delete(0, tk.END)

    # Display a message box to confirm successful submission
    messagebox.showinfo('Success', 'User added successfully')

# Create the main window
root = tk.Tk()
root.title('User Registration')

# Create the form fields
label_user_id = tk.Label(root, text='User ID:')
label_name = tk.Label(root, text='Name:')
label_email = tk.Label(root, text='Email:')
label_age = tk.Label(root, text='Age:')
entry_user_id = tk.Entry(root)
entry_name = tk.Entry(root)
entry_email = tk.Entry(root)
entry_age = tk.Entry(root)
button_submit = tk.Button(root, text='Register', command=add_user)

# Position the form fields
label_user_id.grid(row=0, column=0)
entry_user_id.grid(row=0, column=1)
label_name.grid(row=1, column=0)
entry_name.grid(row=1, column=1)
label_email.grid(row=2, column=0)
entry_email.grid(row=2, column=1)
label_age.grid(row=3, column=0)
entry_age.grid(row=3, column=1)
button_submit.grid(row=4, column=1)

# Run the main event loop
root.mainloop()
