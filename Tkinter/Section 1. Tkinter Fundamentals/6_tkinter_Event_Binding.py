#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk


# def return_pressed(event):
#     print('Return key pressed.')
#
#
# root = tk.Tk()
#
# btn = ttk.Button(root, text='Save')
# btn.bind('<Return>', return_pressed)
#
#
# btn.focus()
# btn.pack(expand=True)
#
# root.mainloop()


def return_pressed(event):
    print('Return key pressed.')


def log(event):
    print(event)


root = tk.Tk()

btn = ttk.Button(root, text='Save')
#btn.bind('<Return>', return_pressed)
btn.bind('<Right>', return_pressed)

# In this statement, the third argument add='+' registered additional handler, which is the log() function.
# If you don’t specify the add='+' argument, the bind() method will replace
# the existing handler (return_pressed) by the new one (log).
#btn.bind('<Return>', log, add='+')
btn.bind('<Right>', log, add='+')


btn.focus()
btn.pack(expand=True)

root.mainloop()

# Summary
# Use the bind() method to bind an event to a widget.
# Tkinter supports both instance-level and class-level bindings.