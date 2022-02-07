#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk

# # root window
# root = tk.Tk()
# root.geometry("240x100")
# root.title('Login')
# root.resizable(0, 0)
#
# # configure the grid
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=3)
#
#
# # username
# username_label = ttk.Label(root, text="Username:")
# username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
#
# username_entry = ttk.Entry(root)
# username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
#
# # password
# password_label = ttk.Label(root, text="Password:")
# password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
#
# password_entry = ttk.Entry(root,  show="*")
# password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)
#
# # login button
# login_button = ttk.Button(root, text="Login")
# login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
#
#
# root.mainloop()


#      OOP



class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("240x100")
        self.title('Login')
        self.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.create_widgets()

    def create_widgets(self):
        # username
        username_label = ttk.Label(self, text="Username:")
        username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        username_entry = ttk.Entry(self)
        username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # password
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        password_entry = ttk.Entry(self,  show="*")
        password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # login button
        login_button = ttk.Button(self, text="Login")
        login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


if __name__ == "__main__":
    app = App()
    app.mainloop()


# Summary
# Use the columnconfigure() and rowconfigure() methods to specify the weight of a column and a row of a grid.
# Use grid() method to position a widget on a grid.
# Use sticky option to align the position of the widget on a cell and define how the widget will be stretched.
# Use ipadx, ipady and padx, pady to add internal and external paddings.