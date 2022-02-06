#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label

# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Label Widget Demo')
#
# # show the label here
#
# root.mainloop()

# Displaying a regular label
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Label Widget Demo')
#
# # show a label
# label = Label(root, text='This is a label')
# label.pack(ipadx=10, ipady=10)
#
# root.mainloop()


# Setting a specific font for the Label
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('Label Widget Demo')
#
# # label with a specific font
# label = ttk.Label(
#     root,
#     text='A Label with the Helvetica font',
#     font=("Helvetica", 14))
#
# label.pack(ipadx=10, ipady=10)
#
# root.mainloop()

# Displaying an image
# create the root window
# root = tk.Tk()
# root.geometry('300x300')
# root.resizable(False, False)
# root.title('Label Widget Image')
#
# # display an image label
# photo = tk.PhotoImage(file='./python.png')
# image_label = ttk.Label(
#     root,
#     image=photo,
#     padding=5
# )
# image_label.pack()
#
# root.mainloop()


# create the root window
root = tk.Tk()
root.geometry('300x300')
root.resizable(False, False)
root.title('Label Widget Image')

# display an image label
photo = tk.PhotoImage(file='./python.png')
image_label = ttk.Label(
    root,
    image=photo,
    text='Python',
    compound='top'
)
image_label.pack()

root.mainloop()