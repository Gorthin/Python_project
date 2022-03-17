#!/usr/bin/python3

import tkinter as tk

COLOR = "#24ad27"

def window_app():
    root = tk.Tk()
    root.configure(bg=COLOR)
    root.geometry("330x480")
    root.title("Flashcards")

    return root

def screen(root):

    screen = [
        tk.Label(root, bg="#C0CBCB", width=55, anchor="w", borderwidth=2)
        for i in range(3)
    ]

    for i in range(len(screen)):
        screen[i].grid(row=i, columnspan=6, ipady=15, ipadx=1)

    return screen

if __name__ == "__main__":

    root = window_app()

    screen = screen(root)

    root.mainloop()