#!/usr/bin/env python3

# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
#
# root = tk.Tk()
# root.title('Treeview demo')
# root.geometry('620x200')
#
# # define columns
# columns = ('first_name', 'last_name', 'email')
#
# tree = ttk.Treeview(root, columns=columns, show='headings')
#
# # define headings
# tree.heading('first_name', text='First Name')
# tree.heading('last_name', text='Last Name')
# tree.heading('email', text='Email')
#
# # generate sample data
# contacts = []
# for n in range(1, 100):
#     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))
#
# # add data to the treeview
# for contact in contacts:
#     tree.insert('', tk.END, values=contact)
#
#
# def item_selected(event):
#     for selected_item in tree.selection():
#         item = tree.item(selected_item)
#         record = item['values']
#         # show a message
#         showinfo(title='Information', message=','.join(record))
#
#
# tree.bind('<<TreeviewSelect>>', item_selected)
#
# tree.grid(row=0, column=0, sticky='nsew')
#
# # add a scrollbar
# scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
# tree.configure(yscroll=scrollbar.set)
# scrollbar.grid(row=0, column=1, sticky='ns')
#
# # run the app
# root.mainloop()


#      OOP



# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         self.title('Treeview demo')
#         self.geometry('620x200')
#
#         self.tree = self.create_tree_widget()
#
#     def create_tree_widget(self):
#         columns = ('first_name', 'last_name', 'email')
#         tree = ttk.Treeview(self, columns=columns, show='headings')
#
#         # define headings
#         tree.heading('first_name', text='First Name')
#         tree.heading('last_name', text='Last Name')
#         tree.heading('email', text='Email')
#
#         tree.bind('<<TreeviewSelect>>', self.item_selected)
#         tree.grid(row=0, column=0, sticky=tk.NSEW)
#
#         # add a scrollbar
#         scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
#         tree.configure(yscroll=scrollbar.set)
#         scrollbar.grid(row=0, column=1, sticky='ns')
#
#         # generate sample data
#         contacts = []
#         for n in range(1, 100):
#             contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))
#
#         # add data to the treeview
#         for contact in contacts:
#             tree.insert('', tk.END, values=contact)
#
#         return tree
#
#     def item_selected(self, event):
#         for selected_item in self.tree.selection():
#             item = self.tree.item(selected_item)
#             record = item['values']
#             # show a message
#             showinfo(title='Information', message=','.join(record))
#
#
# if __name__ == '__main__':
#     app = App()
#     app.mainloop()



#      OOP2  add items


# import tkinter as tk
# from tkinter import ttk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         self.title('Treeview demo')
#         self.geometry('620x200')
#
#         self.tree = self.create_tree_widget()
#
#     def create_tree_widget(self):
#         columns = ('first_name', 'last_name', 'email')
#         tree = ttk.Treeview(self, columns=columns, show='headings')
#
#         # define headings
#         tree.heading('first_name', text='First Name')
#         tree.heading('last_name', text='Last Name')
#         tree.heading('email', text='Email')
#
#         tree.grid(row=0, column=0, sticky=tk.NSEW)
#
#         # adding an item
#         tree.insert('', tk.END, values=('John', 'Doe', 'john.doe@email.com'))
#
#         # insert a the end
#         tree.insert('', tk.END, values=('Jane', 'Miller', 'jane.miller@email.com'))
#
#         # insert at the beginning
#         tree.insert('', 0, values=('Alice', 'Garcia', 'alice.garcia@email.com'))
#
#         return tree
#
#
# if __name__ == '__main__':
#     app = App()
#     app.mainloop()


#    OOP 3     delete items



# import tkinter as tk
# from tkinter import ttk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#
#         self.title('Treeview demo')
#         self.geometry('620x200')
#
#         self.tree = self.create_tree_widget()
#
#     def create_tree_widget(self):
#         columns = ('first_name', 'last_name', 'email')
#         tree = ttk.Treeview(self, columns=columns, show='headings')
#
#         # define headings
#         tree.heading('first_name', text='First Name')
#         tree.heading('last_name', text='Last Name')
#         tree.heading('email', text='Email')
#
#         tree.grid(row=0, column=0, sticky=tk.NSEW)
#
#         # adding an item
#         tree.insert('', tk.END, values=('John', 'Doe', 'john.doe@email.com'))
#
#         # insert a the end
#         tree.insert('', tk.END, values=('Jane', 'Miller', 'jane.miller@email.com'))
#
#         # insert at the beginning
#         tree.insert('', 0, values=('Alice', 'Garcia', 'alice.garcia@email.com'))
#
#         tree.bind('<<TreeviewSelect>>', self.item_selected)
#
#         return tree
#
#     def item_selected(self, event):
#         for selected_item in self.tree.selection():
#             self.tree.delete(selected_item)
#
#
# if __name__ == '__main__':
#     app = App()
#     app.mainloop()


import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# create root window
root = tk.Tk()
root.title('Treeview Demo - Hierarchical Data')
root.geometry('400x200')

# configure the grid layout
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


# create a treeview
tree = ttk.Treeview(root)
tree.heading('text', text='Departments', anchor='w')


# adding data
tree.insert('', tk.END, text='Administration', iid=0, open=False)
tree.insert('', tk.END, text='Logistics', iid=1, open=False)
tree.insert('', tk.END, text='Sales', iid=2, open=False)
tree.insert('', tk.END, text='Finance', iid=3, open=False)
tree.insert('', tk.END, text='IT', iid=4, open=False)

# adding children of first node
tree.insert('', tk.END, text='John Doe', iid=5, open=False)
tree.insert('', tk.END, text='Jane Doe', iid=6, open=False)
tree.move(5, 0, 0)
tree.move(6, 0, 1)

# place the Treeview widget on the root window
tree.grid(row=0, column=0, sticky='nsew')

# run the app
root.mainloop()