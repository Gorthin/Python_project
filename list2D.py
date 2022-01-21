#!/usr/bin/python3

import random


# display list 2D
def print_2D(list):
    for i in range(len(list)):
        for j in range(len(list)):
            print(list[i][j], end=", ")
        print("")


# static list 2D
list2D = [[4, 7, 1, 44], [6, 0, 33], [23, 92, 1010]]

# how to refer to a specific element
print(list2D[1][1])
list2D[1][2] = "777"

# display all list 2D
print_2D(list2D)

# a two-dimensional list consisting of random numbers between 0 and 10
list1D = []
list2D.clear()

for j in range(10):
    for i in range(10):
        list1D.append(random.randint(0, 100))
    list2D.append(list1D)
    list1D = []

print_2D(list2D)

# multiplication table
table_multiplication = []
row = []

for i in range(1, 11):
    for j in range(1, 11):
        row.append(i * j)
    table_multiplication.append(row)
    row = []

print_2D(table_multiplication)
