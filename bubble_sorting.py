#!/usr/bin/python3
import random

def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                swap(list, j, j + 1)
        printList(list)

def swap(list, i, j):
    list[i], list[j] = list[j], list[i]
    return list

def printList(list):
    for x in list:
        print(x, end=", ")
    print("")

list1 = [5, 7, 9, 3, 5, 8, 2, 12, 10]
list2 = list(range(1, 100, 1))
random.shuffle(list2)

print("LIST 1:")
printList(list1)
bubble_sort(list1)
print("=============")
print("LIST 2:")
print(list2)
bubble_sort(list2)