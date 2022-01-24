#!/usr/bin/python3

# Dictionary list
# mini bookstore database
# Dictionary list representing books in bookstore
# Add a book
# delete
# Displaying books according to criteria
# Finding the cheapest and the most expensive book

from operator import itemgetter

def add_book(list_books, key):
    # list storing values for a single dictionary
    list = []
    while 1:
        print("Enter the Title of book:")
        title = input()
        if whether_book(list_books, title):
            print("A book with the title ", title, " is already in our collection!")
        else:
            list.append(title)
            break

    print("Enter author of book")
    author = input()
    list.append(author)
    print("Enter the year the book was published")
    year = int(input())
    list.append(year)
    print("Enter book price")
    price = input()
    list.append(price)
    print("Enter the number of pages of the book")
    number_pages = input()
    list.append(number_pages)

    # Add the book to your book list
    list_books.append(dict(zip(key, list)))


# function checks if a book is in the book list
def whether_book(list_books, title):
    for book in list_books:
        if title == book["Title"]:
            return True
    return False

# function for deleting books
def del_book(list_books, title):
    for book in list_books:
        if title == book["Title"]:
            del book
            break

# function finding the cheapest book
def cheapest(list_books):
    index = 0
    cheapest = list_books[0]["Price"]
    for i in range(1, len(list_books)):
        if list_books[i]["Price"] < cheapest:
            cheapest = list_books[i]["Price"]
            index = i
    return index

def display(list_books, key):
    i = 0
    for book in list_books:
        print("Book number ", i)
        print(" ".join(str(book[key]) for key in keys))
        print(" ")
        i += 1


# dictionary list, represents books in the bookstore
list_books= []
key = ["Title", "Author", "Year the book", "Price", "Number of pages"]

for i in range(3):
    add_book(list_books, key)

display(list_books, key)

print("List sorted by price: ")
print(sorted(list_books, key=itemgetter("Price")))
# print(sorted(lista_ksiazek, key=itemgetter('Cena'), reverse=True))

print("Cheapest book: ")
print(list_books[cheapest(list_books)])

while 1:
    print("Enter the name of the book you want to delete")
    title = input()
    if not whether_book(list_books, title):
        print("A book with the title ", title, " is not in the collection!")
    else:
        del_book(list_books, title)
        print("Correctly deleted")
        break