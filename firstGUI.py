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
    action.configure(text="** I have been Clicked! **")
    aLabel.configure(foreground='red')
    aLabel.configure(text='A Red Label')

# Adding a Button
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=1, row=0)

win.mainloop()
