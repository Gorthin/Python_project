#!/usr/bin/python3

import random

def findMinIndex(list):
    min = list[0]
    minIndex = 0
    for i in range(1, len(list)):
        if min > list[i]:
            min = list[i]
            minIndex = i
    return minIndex

def sortBySelection(list):
    for i in range(len(list)):
        temp = list[i]
        minIndex = findMinIndex(list[i : len(list)]) + i
        list[i] = list[minIndex]
        list[minIndex] = temp
    return list

list = []
for i in range(10):
    list.append(random.randint(0, 100))

print("List before sorting: ")
print(list)
print("List after sorting: ")
print(sortBySelection(list))