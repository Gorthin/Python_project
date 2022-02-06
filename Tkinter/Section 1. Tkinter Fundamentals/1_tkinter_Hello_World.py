#!/usr/bin/env python3

import tkinter as tk
from ctypes import windll

root = tk.Tk()

# place a label on the root window
message = tk.Label(root, text="Hello, World!")
message.pack()

windll.shcore.SetProcessDpiAwareness(1)
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()
# keep the window displaying
root.mainloop()

# Import tkinter module to create a Tkinter desktop application.
# Use Tk class to create the main window and call the mainloop() method to keep the window displays.
# In Tkinter, components are called widgets.