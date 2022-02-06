#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

# root = tk.Tk()
#
#
# def button_clicked():
#     print('Button clicked')
#
#
# button = ttk.Button(root, text='Click Me', command=button_clicked)
# button.pack()
#
# root.mainloop()

# Tkinter button command arguments
root = tk.Tk()


def select(option):
    print(option)


ttk.Button(root, text='Rock', command=lambda: select('Rock')).pack()
ttk.Button(root, text='Paper',command=lambda: select('Paper')).pack()
ttk.Button(root, text='Scissors', command=lambda: select('Scissors')).pack()

root.mainloop()

# Summary
# Assign a function name to the command option of a widget is called command binding in Tkinter.
# The assigned function will be invoked automatically when the corresponding event occurs on the widget.
# Only few widgets support the command option.
