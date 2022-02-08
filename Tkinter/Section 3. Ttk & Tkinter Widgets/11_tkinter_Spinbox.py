#!/usr/bin/env python3

#     1) A simple Tkinter Spinbox widget example

# import tkinter as tk
# # from tkinter import ttk
# #
# #
# # # root window
# # root = tk.Tk()
# # root.geometry('300x200')
# # root.resizable(False, False)
# # root.title('Spinbox Demo')
# #
# # # Spinbox
# # current_value = tk.StringVar(value=0)
# # spin_box = ttk.Spinbox(
# #     root,
# #     from_=0,
# #     to=30,
# #     textvariable=current_value,
# #     wrap=True)
# #
# # spin_box.pack()
# #
# # root.mainloop()



#     2) Tkinter Spinbox with discrete steps


import tkinter as tk
from tkinter import ttk


# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Spinbox Demo')


# spinbox
current_value = tk.StringVar()
spin_box = ttk.Spinbox(
    root,
    from_=0,
    to=50,
    values=(0, 10, 20, 30, 40, 50),
    textvariable=current_value,
    wrap=True)

spin_box.pack()

root.mainloop()


# Summary
# Use ttk.Spinbox(container, **options) to create a Spinbox.
# Set wrap=True to set the current value to the minimum value when it reaches the maximum value and vice versa.