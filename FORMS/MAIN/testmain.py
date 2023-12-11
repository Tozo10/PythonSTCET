import customtkinter as ctk
import tkinter
import pandas as pd
import webbrowser
from PIL import Image
from tkcalendar import DateEntry
#ctk.set_appearance_mode("dark")
#ctk.set_default_color_theme("dark-blue")
import json
class GeneratedForm(ctk.CTkToplevel):
    def __init__(self, parent):
        ctk.CTkToplevel.__init__(self, parent)
        self.title("Generated Form")
        self.geometry("400x400")

        # Load configuration
        self.config_path = "config.json"
        self.config = self.load_config()

        # Check access when the form is created
        if not self.check_access():
            # If access is not allowed, you might want to handle this case.
            # For example, you can show a message and then destroy the form.
            tkinter.messagebox.showinfo("Access Denied", "Access to the form is disabled.")
            self.destroy()

        # rest of your __init__ method...

    def load_config(self):
        try:
            with open(self.config_path, 'r') as config_file:
                config = json.load(config_file)
        except (FileNotFoundError, json.JSONDecodeError):
            # Handle the case when the file is not found or not valid JSON
            # You might want to create an initial configuration here.
            config = {"access_enabled": True}

        return config

    def check_access(self):
        return self.config.get("access_enabled", False)

    def reset_action(self):
        # Clear entry widgets
        first_name_entry.delete(0, "end")
        last_name_entry.delete(0, "end")
        gd_name_entry.delete(0, "end")
        age_spin.delete(0, "end")

        # Clear DateEntry widget
        dob_cal.delete(0, "end")

        address_entry.delete(0, "end")
        mobile_entry.delete(0, "end")
        email_entry.delete(0, "end")

        # Reset combo boxes
        title_combo.set("")
        gender_combo.set("")
        relegion_combo.set("")
        caste_combo.set("")
        dept_combo.set("")
        year_combo.set("")
        sem_combo.set("")

        # Uncheck the check box
        terms_check.deselect()

    def submit_action(self):
        if not self.check_access():
            tkinter.messagebox.showerror('Access Denied', 'Form submission is not allowed. Please contact the admin.')
            return
           # Get values from the entry widgets
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        title_value = title_combo.get()
        guardian_name = gd_name_entry.get()
        age_value = age_spin.get()
        dob_value = dob_cal.get()
        address_value = address_entry.get()
        mobile_value = mobile_entry.get()
        email_value = email_entry.get()
        gender_value = gender_combo.get()
        religion_value = relegion_combo.get()
        caste_value = caste_combo.get()
        dept_value = dept_combo.get()
        year_value = year_combo.get()
        sem_value = sem_combo.get()
        terms_accepted = terms_check.get()

    # Check if all the fields are filled
        if not all([first_name, last_name, title_value, guardian_name, age_value, dob_value, address_value, mobile_value, email_value, gender_value, religion_value, caste_value, dept_value, year_value, sem_value, terms_accepted]):
            tkinter.messagebox.showerror('Error', 'Please fill all the fields')
            return

    # Create a dictionary with the collected data
        data = {
            "First Name": [first_name],
            "Last Name": [last_name],
            "Title": [title_value],
            "Guardian's Name": [guardian_name],
            "Age": [age_value],
            "Date of Birth": [dob_value],
            "Address": [address_value],
            "Mobile No.": [mobile_value],
            "Email id": [email_value],
            "Gender": [gender_value],
            "Religion": [religion_value],
            "Caste": [caste_value],
            "Department": [dept_value],
            "Year": [year_value],
            "Semester": [sem_value],
            "Terms Accepted": [terms_accepted],
            }


    # Create a DataFrame from the dictionary
        df = pd.DataFrame(data)

    # Save the DataFrame to an Excel file
        try:
                existing_df = pd.read_excel('students.xlsx')
                new_df = pd.concat([existing_df, df], ignore_index=True)
        except FileNotFoundError:
                new_df = df
        new_df.to_excel('students.xlsx', index=False)
        self.reset_action()   
        tkinter.messagebox.showinfo('Success', 'Student information saved successfully')
    


window = ctk.CTk()
window.title("Entry Form")

my_image = ctk.CTkImage(light_image=Image.open("STCET-Logo1.png"),size = (90,90))

# Create a CTkLabel with the CTkImage
p_label = ctk.CTkLabel(window, image=my_image, text=" ")
p_label.pack(padx=20, pady=10)

college_label = ctk.CTkLabel(window,text="St. Thomas' College of Engineering & Technology",font=ctk.CTkFont(family = "Old English Text MT",size=30,weight="bold"))
college_label.pack(padx = 10,pady =10)
title_label = ctk.CTkLabel(window,text="Student Information Form",font=ctk.CTkFont(family = "Arial",size=25,weight = "bold"))
title_label.pack(padx = 10,pady =(10,10))

frame = ctk.CTkFrame(window)
frame.pack(fill = "x",padx = 100,pady = 10)

#create widgets.............

#create basic details frame.............

user_info_frame = ctk.CTkFrame(frame)
user_info_frame.grid(row = 0,column = 0,columnspan = 2,padx = 50,pady = (20,1),sticky = "news")

first_name_label = ctk.CTkLabel(user_info_frame,text="First Name",font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 15))
first_name_label.grid(row=0,column=1)
last_name_label = ctk.CTkLabel(user_info_frame,text="Last Name",font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 15))
last_name_label.grid(row=0,column=2)

first_name_entry = ctk.CTkEntry(user_info_frame)
first_name_entry.grid(row=1,column=1)
last_name_entry = ctk.CTkEntry(user_info_frame)
last_name_entry.grid(row=1,column=2)

title = ctk.CTkLabel(user_info_frame,text="Title",font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 15))
title.grid(row=0,column=0)
title_combo = ctk.CTkComboBox(user_info_frame,values=["","Mr.","Ms.","Dr.","Prof."])
title_combo.grid(row=1,column=0)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=13,pady=5)
    
rows = 2
columns = 3
for i in range(rows):
    user_info_frame.grid_rowconfigure(i,weight=1)
for i in range(columns):
    user_info_frame.grid_columnconfigure(i,weight=1)

user_frame = ctk.CTkFrame(frame)
user_frame.grid(row = 1,column = 0,padx = (50,10),pady = (20,10),sticky = "news")


gd_name = ctk.CTkLabel(user_frame,text="Gurdian's Name",font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 15))
gd_name.grid(row = 0,column = 0)
gd_name_entry = ctk.CTkEntry(user_frame)
gd_name_entry.grid(row = 1,column = 0)

age_label = ctk.CTkLabel(user_frame,text="Age",font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 15))
age_label.grid(row = 0,column = 1)
age_spin = tkinter.Spinbox(user_frame,from_=18,to=25,font=ctk.CTkFont(size=15),border = 5)
age_spin.grid(row=1,column=1)

dob_label = ctk.CTkLabel(user_frame,text="Date of Birth",font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 15))
dob_label.grid(row = 2,column = 0)
dob_cal = DateEntry(user_frame, width=20, background='lightblue', foreground='white', borderwidth=5,font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 15))
dob_cal.grid(row=3, column=0)

address_label = ctk.CTkLabel(user_frame,text="Address",font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 15))
address_label.grid(row = 2,column = 1)
address_entry = ctk.CTkEntry(user_frame)
address_entry.grid(row = 3,column = 1)

mobile_label = ctk.CTkLabel(user_frame,text="Mobile No.",font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 15))
mobile_label.grid(row = 4,column = 0)
mobile_entry = ctk.CTkEntry(user_frame)
mobile_entry.grid(row = 5,column = 0)

email_lable = ctk.CTkLabel(user_frame,text="Email id",font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 15))
email_lable.grid(row = 4,column = 1)
email_entry = ctk.CTkEntry(user_frame)
email_entry.grid(row = 5,column = 1)



for widget in user_frame.winfo_children():
    widget.grid_configure(padx=60,pady=5)
    
rows = 6
columns = 2
for i in range(rows):
    user_frame.grid_rowconfigure(i,weight=1)
for i in range(columns):
    user_frame.grid_columnconfigure(i,weight=1)

address_frame = ctk.CTkFrame(frame)
address_frame.grid(row = 1,column = 1,padx = (10,50),pady = (20,10),sticky = "news")

gender_label = ctk.CTkLabel(address_frame,text="Gender",font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 15))
gender_label.grid(row = 0,column = 0)
gender_combo = ctk.CTkComboBox(address_frame,values=[" ","Male","Female","Others"])
gender_combo.grid(row = 1,column = 0)

relegion_label = ctk.CTkLabel(address_frame,text="Religion",font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 15))
relegion_label.grid(row = 2,column = 0)
relegion_combo = ctk.CTkComboBox(address_frame,values=[" ","Hinduism","Islam", "Sikhism", "Buddhism","Jainism","Judaism"])
relegion_combo.grid(row = 3,column = 0)

caste_label = ctk.CTkLabel(address_frame,text="Caste",font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 15))
caste_label.grid(row = 4,column = 0)
caste_combo = ctk.CTkComboBox(address_frame,values=["General","SC","ST","OBC-A","OBC-B"])
caste_combo.grid(row =5,column = 0)

for widget in address_frame.winfo_children():
    widget.grid_configure(padx=13,pady=5)
    
rows1 = 6
columns1 = 1
for i in range(rows1):
    address_frame.grid_rowconfigure(i,weight=1)
for i in range(columns1):
    address_frame.grid_columnconfigure(i,weight=1)

course_frame = ctk.CTkFrame(frame)
course_frame.grid(row = 2,column =0,columnspan = 2,padx = 50,pady = (10,10),sticky = "news")

dept_label = ctk.CTkLabel(course_frame,text="Department",font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 15))
dept_label.grid(row = 0,column = 0)
dept_combo = ctk.CTkComboBox(course_frame,values=["CSE","IT","AIML","ECE","EE"])
dept_combo.grid(row = 1,column = 0)

year_label = ctk.CTkLabel(course_frame,text="Year",font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 15))
year_label.grid(row = 0,column = 1)
year_combo = ctk.CTkComboBox(course_frame,values=["1st","2nd","3rd","4th"])
year_combo.grid(row = 1,column = 1)

sem_lable = ctk.CTkLabel(course_frame,text="Semester",font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 15))
sem_lable.grid(row = 0,column = 2)
sem_combo = ctk.CTkComboBox(course_frame,values=["1st","2nd","3rd","4th","5th", "6th","7th", "8th" ])
sem_combo.grid(row = 1,column = 2)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=13,pady=5)
    
for i in range(2):
    course_frame.grid_rowconfigure(i,weight=1)
for i in range(3):
    course_frame.grid_columnconfigure(i,weight=1)

terms_frame = ctk.CTkFrame(frame)
terms_frame.grid(row = 3,column = 0,columnspan = 2,padx = 50,pady = (10,10),sticky = "news")
def open_html_file():
    html_file_path = 'TXT.html'
    webbrowser.open(html_file_path)
    # Specify the path to the text file


term_label = ctk.CTkLabel(terms_frame,text="Terms & Conditions",font=ctk.CTkFont(family = "Times New Roman" ,weight="bold",size = 15,underline = True),text_color = 'blue',cursor="hand2")
term_label.grid(row = 0,column = 0)
term_label.bind("<Button-1>", lambda event: open_html_file())

   
terms_check = ctk.CTkCheckBox(terms_frame, text="I accept the terms & conditions")
terms_check.grid(row=1, column=0)

for widget in terms_frame.winfo_children():
    widget.grid_configure(padx=13,pady=5)

r = 2
c=1

for i in range(r):
    terms_frame.grid_rowconfigure(i,weight=1)
for i in range(c):
    terms_frame.grid_columnconfigure(i,weight=1)
    



for i in range(5):
    frame.grid_rowconfigure(i,weight=1)
for i in range(2):
    frame.grid_columnconfigure(i,weight=1)


 


if __name__ == "__main__":
    form = GeneratedForm(window)
    # Add functionality to the submit button
    submit = ctk.CTkButton(frame, text="SUBMIT", command=form.submit_action)
    submit.grid(row=4, column=0, padx=(50, 10), pady=(10, 10), sticky="news")
    reset = ctk.CTkButton(frame, text="RESET", command=form.reset_action)
    reset.grid(row=4, column=1, padx=(10, 50), pady=(10, 10), sticky="news")

    window.mainloop()
