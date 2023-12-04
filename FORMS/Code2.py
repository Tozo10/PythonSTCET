import tkinter as tk
import pandas as pd
import tkinter.messagebox as messagebox

class StudentInfoSystem(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Information System")
        self.configure(bg='lightblue')  # Set background color
        self.create_widgets()

    def create_widgets(self):
        # Heading
        heading_label = tk.Label(self, text='Student Information System', font=('Arial', 16, 'bold'), bg='lightblue')
        heading_label.pack(pady=10)

        # Labels and Entry widgets
        labels = ['Name:', 'Dept:', 'Address:', 'DOB (YYYY-MM-DD):', 'Guardian Name:', 'Gender:', 'Email:', 'Phone:']
        entries = {}

        for label_text in labels:
            frame = tk.Frame(self, bg='lightblue')
            frame.pack(fill=tk.X, padx=10, pady=5)

            label = tk.Label(frame, text=label_text, font=('Arial', 12), bg='lightblue')
            label.pack(side=tk.LEFT, padx=5)

            if label_text == 'Gender:':
                gender_var = tk.StringVar(value='Male')  # Default to Male
                gender_options = ['Male', 'Female']
                gender_menu = tk.OptionMenu(frame, gender_var, *gender_options)
                gender_menu.config(bg='lightblue')
                gender_menu.pack(side=tk.LEFT, padx=5)
                entries[label_text] = gender_var
            else:
                entry = tk.Entry(frame)
                entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
                entries[label_text] = entry

        # Submit and Reset buttons
        button_submit = tk.Button(self, text='Save Information', command=lambda: self.add_student(entries))
        button_submit.pack(pady=10)

        button_reset = tk.Button(self, text='Reset', command=lambda: self.reset_form(entries))
        button_reset.pack(pady=10)

    def add_student(self, entries):
        # Get the user info from the form
        name = entries['Name:'].get()
        dept = entries['Dept:'].get()
        address = entries['Address:'].get()
        dob = entries['DOB (YYYY-MM-DD):'].get()
        guardian_name = entries['Guardian Name:'].get()
        gender = entries['Gender:'].get()
        email = entries['Email:'].get()
        phone = entries['Phone:'].get()

        # Check if all the fields are filled
        if not all([name, dept, address, dob, guardian_name, gender, email, phone]):
            messagebox.showerror('Error', 'Please fill all the fields')
            return

        # Add the student info to the dataframe
        data = {'Name': [name], 'Dept': [dept], 'Address': [address], 'DOB': [dob],
                'Guardian Name': [guardian_name], 'Gender': [gender], 'Email': [email], 'Phone': [phone]}
        df = pd.DataFrame(data)

        # Append the new student info to the existing Excel file
        try:
            existing_df = pd.read_excel('students.xlsx')
            new_df = pd.concat([existing_df, df], ignore_index=True)
        except FileNotFoundError:
            new_df = df
        new_df.to_excel('students.xlsx', index=False)

        # Clear the form fields
        self.reset_form(entries)

        # Display a message box to confirm successful submission
        messagebox.showinfo('Success', 'Student information saved successfully')

    def reset_form(self, entries):
        for entry in entries.values():
            if isinstance(entry, tk.Entry):
                entry.delete(0, 'end')
            elif isinstance(entry, tk.StringVar):
                entry.set('Male')  # Reset gender to Male

if __name__ == '__main__':
    app = StudentInfoSystem()
    app.mainloop()
