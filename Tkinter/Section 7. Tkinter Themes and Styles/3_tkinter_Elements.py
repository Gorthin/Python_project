#!/usr/bin/env python3

# import tkinter as tk
# from tkinter import ttk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         style = ttk.Style(self)
#
#         layout = style.layout('TLabel')
#         print(layout)
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()



# import tkinter as tk
# from tkinter import ttk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         style = ttk.Style(self)
#
#         # layout
#         layout = style.layout('TLabel')
#         print(layout)
#
#         # element options
#         print(style.element_options('Label.border'))
#         print(style.element_options('Label.padding'))
#         print(style.element_options('Label.label'))
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()





# import tkinter as tk
# from tkinter import ttk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         style = ttk.Style(self)
#
#         # attributes of the font, foreground, and background
#         # of the Label.label element
#         print(style.lookup('Label.label', 'font'))
#         print(style.lookup('Label.label', 'foreground'))
#         print(style.lookup('Label.label', 'background'))
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

        self.geometry('500x100')

        message = 'This is an error message!'

        label = ttk.Label(self, text=message, style='Error.TLabel')
        label.pack(expand=True)

        style = ttk.Style(self)

        style.configure('Error.TLabel', foreground='white')
        style.configure('Error.TLabel', background='red')
        style.configure('Error.TLabel', font=('Helvetica', 12))
        style.configure('Error.TLabel', padding=(10, 10))


if __name__ == "__main__":
    app = App()
    app.mainloop()


# Summary
# A ttk widget is made up of elements. The layout determines how elements assembled the widget.
# Use the Style.layout() method to retrieve the layout of a widget class.
# Use the Style.element_options() method to get the element options of an element.
# Use the Style.lookup() method to get the attributes of an element option.