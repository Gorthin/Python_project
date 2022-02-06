#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

tk.Label(root, text='Classic Label').pack()
ttk.Label(root, text='Themed Label').pack()

root.mainloop()

# Tkinter has both classic and themed widgets. The Tk themed widgets are also known as ttk widgets.
# The tkinter.ttk module contains all the ttk widgets.
# Do use ttk widgets whenever they’re available.