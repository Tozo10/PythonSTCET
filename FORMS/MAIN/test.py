import customtkinter as ctk
import tkinter
from tkinter import ttk
import openpyxl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
import subprocess
from testmain import GeneratedForm
import json

def enable_access():
    config_path = "config.json"
    try:
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
    except json.JSONDecodeError:
        # If the file is empty or not valid JSON, create an initial configuration
        config = {"access_enabled": False}

    config["access_enabled"] = True

    with open(config_path, 'w') as config_file:
        json.dump(config, config_file, indent=2)

def disable_access():
    config_path = "config.json"
    try:
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
    except json.JSONDecodeError:
        # If the file is empty or not valid JSON, create an initial configuration
        config = {"access_enabled": False}

    config["access_enabled"] = False

    with open(config_path, 'w') as config_file:
        json.dump(config, config_file, indent=2)


def load():
    list_values = list(sheet.values)
    #print(list_values)
    for col_name in list_values[0]:
        treeview.heading(col_name,text=col_name)
    for value_tuple in list_values[1:]:
        treeview.insert('',tkinter.END,values=value_tuple)

def count_dept(path,  column_name2):
    df = pd.read_excel(path)
    return df[column_name2].value_counts()

def count_year(path,  column_name1):
    df = pd.read_excel(path)
    return df[column_name1].value_counts()

path = "students.xlsx"
workbook = openpyxl.load_workbook(path)
sheet = workbook.active

column_name1 = 'Year'
column_name2 = 'Department'

plt.rcParams["axes.prop_cycle"] = plt.cycler(
    color=["#1E90FF", "#AFEEEE", "#48D1CC", "#87CEFA", "#00BFFF"])

        
#create bar.....
year_counts = count_year(path, column_name1)
year = {}
for element, count in year_counts.items():
    #print(f"{element}: {count}")
    year[element] = count
    
fig1, ax1 = plt.subplots(figsize = (4,3))
ax1.bar(year.keys(), year.values())
ax1.set_title("Year")
#ax1.set_xlabel("Year")
ax1.set_ylabel("No. of students")
#plt.show()

#create pie chart .....
dept_counts = count_dept(path, column_name2)
dept = {}
for element, count in dept_counts.items():
    #print(f"{element}: {count}")
    dept[element] = count
    
fig2, ax3 = plt.subplots(figsize = (4,2.5))
ax3.pie(dept.values(), labels=dept.keys(), autopct='%1.1f%%')
ax3.set_title("Department")
# plt.show()

window = ctk.CTkToplevel()
window.title("Admin")
window.state('zoomed')
s = ttk.Style()
s.theme_use('clam')

my_image = ctk.CTkImage(light_image=Image.open("STCET-Logo1.png"),size = (70,70))

# Create a CTkLabel with the CTkImage
p_label = ctk.CTkLabel(window, image=my_image, text=" ")
p_label.pack(padx=20, pady=5)

college_label = ctk.CTkLabel(window,text="St. Thomas' College of Engineering & Technology",font=ctk.CTkFont(family = "Old English Text MT",size=30,weight="bold"))
college_label.pack(padx = 10,pady =5)
title_label = ctk.CTkLabel(window,text="Admin Page",font=ctk.CTkFont(family = "Arial",size=25,weight = "bold"))
title_label.pack(padx = 10,pady =5)

frame = ctk.CTkFrame(window)
frame.pack(fill = "x",padx = 100,pady = (5,10))

tree_label = ctk.CTkLabel(frame,text="Data Sheet of Students Information",font=ctk.CTkFont(family = "Arial",size=25,weight = "bold"))
tree_label.grid(row = 0,column = 1,padx = 5,pady = (10,5),sticky = "news")

treeFrame = ttk.Frame(frame)
treeFrame.grid(row=1,column=1,pady=(10,5),padx=(10,20))
treescy = ttk.Scrollbar(treeFrame)
treescy.pack(side="right",fill="y")
#treescx = ttk.Scrollbar(treeFrame,orient='horizontal')
#treescx.pack(side="bottom",fill="x")

cols = ("First Name","Last Name","Title","Guardian's Name","Age","Date of Birth","Address","Mobile No.","Email id","Gender","Religion","Caste","Department","Year","Semester","Terms Accepted")
treeview = ttk.Treeview(treeFrame,show="headings",yscrollcommand=treescy.set,columns=cols,height=30)
for col in cols:
    treeview.column(col,width=65)
treeview.pack()
#s.configure("Treeview",background = "#AFEEEE",fieldbackground = "AFEEEE")
s.configure("Treeview.Heading",background = "#48D1CC")
treescy.config(command=treeview.yview)
#treescx.config(command=treeview.xview)
load()

mat_label = ctk.CTkLabel(frame,text="Dashboard",font=ctk.CTkFont(family = "Arial",size=25,weight = "bold"))
mat_label.grid(row = 0,column = 0,padx = (20,10),pady = (10,5),sticky = "news")

mat_frame = ctk.CTkFrame(frame,height=100,width=50)
mat_frame.grid(row = 1,column = 0,rowspan = 2,sticky = "news",padx = (20,10))

canvas1 = FigureCanvasTkAgg(fig1, mat_frame)
canvas1.draw()
canvas1.get_tk_widget().grid(row=0,column=0,padx=5,pady=5)

canvas2 = FigureCanvasTkAgg(fig2, mat_frame)
canvas2.draw()
canvas2.get_tk_widget().grid(row = 1,column=0,padx=5,pady=5)

for i in range(2):
    mat_frame.grid_rowconfigure(i,weight=1)
for i in range(1):
    mat_frame.grid_columnconfigure(i,weight=1)

button_frame = ctk.CTkFrame(frame)
button_frame.grid(row = 2,column = 1,padx = 10,pady = 5,sticky = "news")

def open_generated_form():
    # Run the form_generator.py script to generate the form
    subprocess.Popen(['python', 'main.py'], shell=True)

    
    
Edit_button = ctk.CTkButton(button_frame, text="Edit Form", command=open_generated_form)
Edit_button.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="news")

def open_excel_sheet():
    subprocess.Popen(['start', 'excel', path], shell=True)

Excel_button = ctk.CTkButton(button_frame, text="View Excel Sheet", command=open_excel_sheet)
Excel_button.grid(row=0, column=1, padx=(5, 10), pady=10, sticky="news")

# Add buttons to enable and disable access
enable_button = ctk.CTkButton(button_frame, text="Enable Form Access", command=enable_access)
enable_button.grid(row=1, column=0, padx=(10, 5), pady=10, sticky="news")

disable_button = ctk.CTkButton(button_frame, text="Disable Form Access", command=disable_access)
disable_button.grid(row=1, column=1, padx=(5, 10), pady=10, sticky="news")

for i in range(1):
    button_frame.grid_rowconfigure(i,weight=1)
for i in range(2):
    button_frame.grid_columnconfigure(i,weight=1)

for i in range(3):
    frame.grid_rowconfigure(i,weight=1)
for i in range(2):
    frame.grid_columnconfigure(i,weight=1)

window.mainloop()
