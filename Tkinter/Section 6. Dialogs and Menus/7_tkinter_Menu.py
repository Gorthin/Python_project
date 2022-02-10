#!/usr/bin/env python3

# import tkinter as tk
# from tkinter import Menu
#
# # root window
# root = tk.Tk()
# root.title('Menu Demo')
#
# # create a menubar
# menubar = Menu(root)
# root.config(menu=menubar)
#
# # create a menu
# file_menu = Menu(menubar, tearoff=False)
#
# # add a menu item to the menu
# file_menu.add_command(
#     label='Exit',
#     command=root.destroy
# )
#
#
# # add the File menu to the menubar
# menubar.add_cascade(
#     label="File",
#     menu=file_menu
# )
#
# root.mainloop()




# from tkinter import Tk, Frame, Menu
#
#
# # root window
# root = Tk()
# root.geometry('320x150')
# root.title('Menu Demo')
#
#
# # create a menubar
# menubar = Menu(root)
# root.config(menu=menubar)
#
# # create the file_menu
# file_menu = Menu(
#     menubar,
#     tearoff=0
# )
#
# # add menu items to the File menu
# file_menu.add_command(label='New')
# file_menu.add_command(label='Open...')
# file_menu.add_command(label='Close')
# file_menu.add_separator()
#
# # add Exit menu item
# file_menu.add_command(
#     label='Exit',
#     command=root.destroy
# )
#
# # add the File menu to the menubar
# menubar.add_cascade(
#     label="File",
#     menu=file_menu
# )
# # create the Help menu
# help_menu = Menu(
#     menubar,
#     tearoff=0
# )
#
# help_menu.add_command(label='Welcome')
# help_menu.add_command(label='About...')
#
# # add the Help menu to the menubar
# menubar.add_cascade(
#     label="Help",
#     menu=help_menu
# )
#
# root.mainloop()





from tkinter import Tk, Menu


# root window
root = Tk()
root.geometry('320x150')
root.title('Menu Demo')


# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create the file_menu
file_menu = Menu(
    menubar,
    tearoff=0
)

# add menu items to the File menu
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Close')
file_menu.add_separator()

# add a submenu
sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label='Keyboard Shortcuts')
sub_menu.add_command(label='Color Themes')

# add the File menu to the menubar
file_menu.add_cascade(
    label="Preferences",
    menu=sub_menu
)

# add Exit menu item
file_menu.add_separator()
file_menu.add_command(
    label='Exit',
    command=root.destroy
)


menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)
# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

# add the Help menu to the menubar
menubar.add_cascade(
    label="Help",
    menu=help_menu,
    underline=0
)

root.mainloop()




Summary
# Use Menu() to create a new menu,
# Use menu.add_command() method to add a menu item to the menu.
# Use menubar.add_cascade(menu_title, menu) to add a menu to the menubar.
# Use menu.add(submenu_title, submenu) to add a submenu to the menu.