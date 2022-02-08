#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.resizable(False, False)
root.title("Scrollbar Widget Example")

# apply the grid layout
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# create the text widget
text = tk.Text(root, height=10)
text.grid(row=0, column=0, sticky='ew')

# create a scrollbar widget and set its command to the text widget
scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
scrollbar.grid(row=0, column=1, sticky='ns')

#  communicate back to the scrollbar
text['yscrollcommand'] = scrollbar.set


root.mainloop()

# Summary
# Create a scrollbar with ttk.Scrollbar(orient, command)
# The orient can be 'vertical' or 'horizontal'
# The command can be yview or xview property of the scrollable widget that links to the scrollbar.
# Set the yscrollcommand property of the scrollable widget so it links to the scrollbar.
