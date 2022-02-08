#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Checkbox Demo')

agreement = tk.StringVar()


def agreement_changed():
    tk.messagebox.showinfo(title='Result',
                        message=agreement.get())


ttk.Checkbutton(root,
                text='I agree',
                command=agreement_changed,
                variable=agreement,
                onvalue='agree',
                offvalue='disagree').pack()


root.mainloop()

# Summary
# Use ttk.Checkbutton(text, variable) to create a checkbox; the variable is a tk.StringVar().
# Use command argument to specify a function that executes when the button is checked or unchecked.
# Use the onvalue and offvalue to determine what value the variable will take.