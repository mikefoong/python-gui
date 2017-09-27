import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Python GUI")
#win.resizable(0,0)

# Labels in the app
aLabel = ttk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

# Button Click Event Function
def clickMe():
    action.configure(text='Hello ' + name.get())

# Change the Label
ttk.Label(win, text="Enter a name: ").grid(column=0, row=0)

# Adding a TextBox Entry Widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)
# action.configure(state='disabled') # Disable the Button Widget

ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

nameEntered.focus()  # Place cursorinto name Entry


win.mainloop()
