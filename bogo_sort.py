#!/usr/bin/python3

import random

def bogo_sort(list):
    counter = 0
    while not whether_sorted(list):
        random.shuffle(list)
        counter += 1
    print("The sorting took place ", counter, " times.")


def whether_sorted(list):
    for i in range(1, len(list)):
        if list[i] < list[i - 1]:
            return False
    return True

list = []
for i in range(6):
    list.append(random.randint(0, 100))

print("Before sorting: ")
print(list)

bogo_sort(list)
print("After sorting: ")
print(list)