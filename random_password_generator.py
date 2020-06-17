import random
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo

win = tk.Tk()
win.title("Password Generator")


def generate():
    string = entry.get()
    length = int(entry2.get())
    password = ''
    for i in range(length):
        password = password + random.choice(string)
    showinfo("Generated password", f" Your password :{password}")


label = tk.Label(win, text="Enter String: ")
label.grid(row=0, column=0, padx=8, pady=8)

entry = tk.Entry(win)
entry.grid(row=0, column=1, padx=8)

label1 = tk.Label(win, text="Enter length: ")
label1.grid(row=1, column=0, padx=8, pady=8)

entry2 = tk.Entry(win)
entry2.grid(row=1, column=1, padx=8)

button = ttk.Button(win, text="Generate", command=generate)
button.grid(row=2, column=0, columnspan=2, padx=8)

win.mainloop()
