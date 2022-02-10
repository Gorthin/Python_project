#!/usr/bin/env python3

# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog as fd
# from tkinter.messagebox import showinfo
#
# # create the root window
# root = tk.Tk()
# root.title('Tkinter Open File Dialog')
# root.resizable(False, False)
# root.geometry('300x150')
#
#
# def select_file():
#     filetypes = (
#         ('text files', '*.txt'),
#         ('All files', '*.*')
#     )
#
#     filename = fd.askopenfilename(
#         title='Open a file',
#         initialdir='/',
#         filetypes=filetypes)
#
#     showinfo(
#         title='Selected File',
#         message=filename
#     )
#
#
# # open button
# open_button = ttk.Button(
#     root,
#     text='Open a File',
#     command=select_file
# )
#
# open_button.pack(expand=True)
#
#
# # run the application
# root.mainloop()


# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog as fd
# from tkinter.messagebox import showinfo
#
# # create the root window
# root = tk.Tk()
# root.title('Tkinter File Dialog')
# root.resizable(False, False)
# root.geometry('300x150')
#
#
# def select_files():
#     filetypes = (
#         ('text files', '*.txt'),
#         ('All files', '*.*')
#     )
#
#     filenames = fd.askopenfilenames(
#         title='Open files',
#         initialdir='/',
#         filetypes=filetypes)
#
#     showinfo(
#         title='Selected Files',
#         message=filenames
#     )
#
#
# # open button
# open_button = ttk.Button(
#     root,
#     text='Open Files',
#     command=select_files
# )
#
# open_button.pack(expand=True)
#
# root.mainloop()




import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd

# Root window
root = tk.Tk()
root.title('Display a Text File')
root.resizable(False, False)
root.geometry('550x250')

# Text editor
text = tk.Text(root, height=12)
text.grid(column=0, row=0, sticky='nsew')


def open_text_file():
    # file type
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    f = fd.askopenfile(filetypes=filetypes)
    # read the text file and show its content on the Text
    text.insert('1.0', f.readlines())


# open file button
open_button = ttk.Button(
    root,
    text='Open a File',
    command=open_text_file
)

open_button.grid(column=0, row=1, sticky='w', padx=10, pady=10)


root.mainloop()



# Summary
# Use the askopenfilename() function to display an open file dialog that allows users to select one file.
# Use the askopenfilenames() function to display an open file dialog that allows users to select multiple files.
# Use the askopenfile() or askopenfiles() function to display an open file dialog that allows users to select one or multiple files and receive a file or multiple file objects.