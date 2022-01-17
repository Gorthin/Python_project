#!/usr/bin/python3

  # linear and binary search

def linear(list, x):
    for i in range(len(list)):
        if list[i] == x:
            return i
    return -1

def binary(list, x):
    first = 0
    last = len(list)
    while first <= last:
        mid = first + int((last - first)/2)

        if list[mid] == x:
            return mid
        elif list[mid] < x:
            first = mid + 1
        else:
            last = mid - 1
    return -1

list = [0, 3, 5, 7, 8, 13, 24, 35, 46, 57]
print(list)
print('Linear:')
print(linear(list, 5))
print('Binary:')
print(binary(list, 24))