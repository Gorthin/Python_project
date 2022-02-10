#!/usr/bin/env python3

# import tkinter as tk
# from tkinter import ttk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         self.geometry('300x110')
#         self.resizable(0, 0)
#         self.title('Login')
#
#         # UI options
#         paddings = {'padx': 5, 'pady': 5}
#         entry_font = {'font': ('Helvetica', 11)}
#
#         # configure the grid
#         self.columnconfigure(0, weight=1)
#         self.columnconfigure(1, weight=3)
#
#         username = tk.StringVar()
#         password = tk.StringVar()
#
#         # username
#         username_label = ttk.Label(self, text="Username:")
#         username_label.grid(column=0, row=0, sticky=tk.W, **paddings)
#
#         username_entry = ttk.Entry(self, textvariable=username, **entry_font)
#         username_entry.grid(column=1, row=0, sticky=tk.E, **paddings)
#
#         # password
#         password_label = ttk.Label(self, text="Password:")
#         password_label.grid(column=0, row=1, sticky=tk.W, **paddings)
#
#         password_entry = ttk.Entry(
#             self, textvariable=password, show="*", **entry_font)
#         password_entry.grid(column=1, row=1, sticky=tk.E, **paddings)
#
#         # login button
#         login_button = ttk.Button(self, text="Login")
#         login_button.grid(column=1, row=3, sticky=tk.E, **paddings)
#
#         # configure style
#         self.style = ttk.Style(self)
#         self.style.configure('TLabel', font=('Helvetica', 11))
#         self.style.configure('TButton', font=('Helvetica', 11))
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()





import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('300x150')
        self.resizable(0, 0)
        self.title('Login')

        # UI options
        paddings = {'padx': 5, 'pady': 5}
        entry_font = {'font': ('Helvetica', 11)}

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        username = tk.StringVar()
        password = tk.StringVar()

        # heading
        heading = ttk.Label(self, text='Member Login', style='Heading.TLabel')
        heading.grid(column=0, row=0, columnspan=2, pady=5, sticky=tk.N)

        # username
        username_label = ttk.Label(self, text="Username:")
        username_label.grid(column=0, row=1, sticky=tk.W, **paddings)

        username_entry = ttk.Entry(self, textvariable=username, **entry_font)
        username_entry.grid(column=1, row=1, sticky=tk.E, **paddings)

        # password
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(column=0, row=2, sticky=tk.W, **paddings)

        password_entry = ttk.Entry(
            self, textvariable=password, show="*", **entry_font)
        password_entry.grid(column=1, row=2, sticky=tk.E, **paddings)

        # login button
        login_button = ttk.Button(self, text="Login")
        login_button.grid(column=1, row=3, sticky=tk.E, **paddings)

        # configure style
        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=('Helvetica', 11))
        self.style.configure('TButton', font=('Helvetica', 11))

        # heading style
        self.style.configure('Heading.TLabel', font=('Helvetica', 12))


if __name__ == "__main__":
    app = App()
    app.mainloop()


# Summary
# A theme of a collection of styles. A style is a description of the appearance of a widget.
# Use the widget.winfo_class() method to get the widget class of a widget. The widget class defines the default style for the widget.
# Use the style.configure() method to modify the style of the widget.
# To customize the built-in style, you can extend it using the style name new_style.builtin_style.