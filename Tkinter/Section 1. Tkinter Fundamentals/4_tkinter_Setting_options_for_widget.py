#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

# Tkinter allows you to set the options of a widget using one of the following ways:
# At widget creation, using keyword arguments.
# After widget creation, using a dictionary index.
# And use the config() method with keyword attributes.

# 1) Using keyword arguments when creating the widget
# root = tk.Tk()
# ttk.Label(root, text='Hi, there').pack()
#
# root.mainloop()

# 2) Using a dictionary index after widget creation
# root = tk.Tk()
#
# label = ttk.Label(root)
# label['text'] = 'Hi, there'
# label.pack()
#
# root.mainloop()

# 3) Using the config() method with keyword attributes
root = tk.Tk()

label = ttk.Label(root)
label.config(text='Hi, there')
label.pack()

root.mainloop()

# Ttk widgets provide you with three ways to set options:
#
# Use keyword arguments at widget creation.
# Use a dictionary index after widget creation.
# Use the config() method with keyword attributes.