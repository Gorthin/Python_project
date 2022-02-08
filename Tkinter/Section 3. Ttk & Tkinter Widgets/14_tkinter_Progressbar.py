#!/usr/bin/env python3

#    1) Tkinter Progressbar in the indeterminate mode example


import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('300x120')
root.title('Progressbar Demo')

root.grid()

# progressbar
pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='indeterminate',
    length=280
)
# place the progressbar
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)


# start button
start_button = ttk.Button(
    root,
    text='Start',
    command=pb.start
)
start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)

# stop button
stop_button = ttk.Button(
    root,
    text='Stop',
    command=pb.stop
)
stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)


root.mainloop()



#            2) Tkinter Progressbar in the determinate mode example


# from tkinter import ttk
# import tkinter as tk
# from tkinter.messagebox import showinfo
#
#
# # root window
# root = tk.Tk()
# root.geometry('300x120')
# root.title('Progressbar Demo')
#
#
# def update_progress_label():
#     return f"Current Progress: {pb['value']}%"
#
#
# def progress():
#     if pb['value'] &lt; 100:
#         pb['value'] += 20
#         value_label['text'] = update_progress_label()
#     else:
#         showinfo(message='The progress completed!')
#
#
# def stop():
#     pb.stop()
#     value_label['text'] = update_progress_label()
#
#
# # progressbar
# pb = ttk.Progressbar(
#     root,
#     orient='horizontal',
#     mode='determinate',
#     length=280
# )
# # place the progressbar
# pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)
#
# # label
# value_label = ttk.Label(root, text=update_progress_label())
# value_label.grid(column=0, row=1, columnspan=2)
#
# # start button
# start_button = ttk.Button(
#     root,
#     text='Progress',
#     command=progress
# )
# start_button.grid(column=0, row=2, padx=10, pady=10, sticky=tk.E)
#
# stop_button = ttk.Button(
#     root,
#     text='Stop',
#     command=stop
# )
# stop_button.grid(column=1, row=2, padx=10, pady=10, sticky=tk.W)
#
#
# root.mainloop()

# Summary
# Use the ttk.Progressbar(container, orient, length, mode) to create a progressbar.
# Use the indeterminate mode when the program cannot accurately know the relative progress to display.
# Use the determinate mode if you know how to measure the progress accurately.
# Use the start(), step(), and stop() methods to control the current value of the progressbar.