#!/usr/bin/env python3

# import tkinter as tk
# from tkinter.scrolledtext import ScrolledText
#
#
# root = tk.Tk()
# root.title("ScrolledText Widget")
#
#
# st = ScrolledText(root, width=50,  height=10)
# st.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
#
# root.mainloop()


#    OOP


import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ScrolledText Widget")
        st = ScrolledText(self, width=50, height=10)
        st.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()

# Summary
# Use the Tkinter ScrolledText widget to create a Text widget with a vertical Scrollbar.