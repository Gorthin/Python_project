#!/usr/bin/env python3

import tkinter as tk


# root = tk.Tk()
# root.title('Tkinter Window Demo')
# root.geometry('400x600+50+50')
#
# root.mainloop()

root = tk.Tk()
root.title('Flashcards - Center')

window_width = 400
window_height = 600

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
# The resizable() method has two parameters that specify whether the width and height of the window can be resizable.
root.resizable(False, False)

# Tkinter allows you to specify the transparency of a window by setting its alpha channel ranging from 0.0 (fully transparent) to 1.0 (fully opaque):
#root.attributes('-alpha', 0.5)

# The window stack order refers to the order of windows placed on the screen from bottom to top. The closer window is on the top of the stack and it overlaps the one lower.
#
# To ensure that a window is always at the top of the stacking order, you can use the -topmost attribute like this:
root.attributes('-topmost', 1)


#Tkinter window displays a default icon. To change this default icon, you follow these steps:
# Prepare an image in the .ico format. If you have the image in other formats like png or jpg, you can
# convert it to the .ico format. There are many online tools that allow you to do it quite easily.
# Place the icon in a folder that can be accessible from the program.
# Call the iconbitmap() method of the window object.
root.iconbitmap('./1.ico')



root.mainloop()

# Summary
# Use the title() method to change the title of the window.
# Use the geometry() method to change the size and location of the window.
# Use the resizable() method to specify whether a window can be resizable horizontally or vertically.
# Use the window.attributes('-alpha',0.5) to set the transparency for the window.
# Use the window.attributes('-topmost', 1) to make the window always on top.
# Use lift() and lower() methods to move the window up and down of the window stacking order.
# Use the iconbitmap() method to change the default icon of the window.