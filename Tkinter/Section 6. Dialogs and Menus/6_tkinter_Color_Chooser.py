#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor


root = tk.Tk()
root.title('Tkinter Color Chooser')
root.geometry('300x150')


def change_color():
    colors = askcolor(title="Tkinter Color Chooser")
    root.configure(bg=colors[1])


ttk.Button(
    root,
    text='Select a Color',
    command=change_color).pack(expand=True)


root.mainloop()


# Summary
# Use the askcolor() function from tkinter.colorchooser module to display a color chooser dialog.
# The askcolor() function returns a tuple of the selected color or None.