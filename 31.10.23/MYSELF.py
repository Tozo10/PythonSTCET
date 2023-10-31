import tkinter as tk
def add():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    result.set(n1+n2)
def sub():
    n1 = float(entry1.get())
    n2 = float(entry2.get())
    result.set(n1 - n2)
def reset():
  entry1.delete(0,'end')
  entry2.delete(0,'end')
  result.set("0")
  
root = tk.Tk()
root.title("ADDITION & SUBTRACTION")
frame = tk.Frame(root)
frame.pack()


w4 = tk.Label(frame, text = "ADDITION & SUBTRACTION")
w4.pack()
w1 = tk.Label(frame, text="Enter Number 1 : ")
w1.pack(side=tk.LEFT)
entry1 = tk.Entry(frame)
entry1.pack(side=tk.LEFT)
w2 = tk.Label(frame, text="Enter Number 2 : ")
w2.pack(side=tk.LEFT)
entry2 = tk.Entry(frame)
entry2.pack(side=tk.LEFT)

button1 = tk.Button(frame,text="ADD", fg="brown",command=add)
button1.pack(side=tk.BOTTOM)
button2 = tk.Button(frame,text="SUBTRACT",fg="blue",command=sub)
button2.pack(side=tk.BOTTOM)
button3 = tk.Button(frame,text="QUIT",fg="red",command=quit)
button3.pack(side=tk.BOTTOM)
button4 = tk.Button(frame,text = "RESET", fg = "maroon", command = reset)
button4.pack(side=tk.BOTTOM)
result = tk.StringVar()
w3 = tk.Label(root,textvariable = result)
w3.pack()

root.mainloop()
