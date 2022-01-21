#!/usr/bin/python3

import random

def find_min_index(list):
    minimum = list[0]
    min_index = 0
    for i in range(1, len(list)):
        if minimum > list[i]:
            minimum = list[i]
            min_index = i
    return min_index

def sort_by_selection(list):
    for i in range(len(list)):
        temp = list[i]
        min_index = find_min_index(list[i : len(list)]) + i
        list[i] = list[min_index]
        list[min_index] = temp
    return list

list = []
for i in range(10):
    list.append(random.randint(0, 100))

print("List before sorting: ")
print(list)
print("List after sorting: ")
print(sort_by_selection(list))