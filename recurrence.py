#!/usr/bin/python3
def sum_loop(list):
    sum = 0
    for x in list:
        sum += x
    return sum


# every recursive function has two cases: a base case and a recursive case

def sum_recurrence(list):
    # base case
    if list == []:
        return 0
    # recursive case
    else:
        return list[0] + sum_recurrence(list[1:])


list = [4, 5, 6, 7]
print("Sum for loop: ")
print(sum_loop(list))
print("")
print("Sum for recurrence: ")
print(sum_recurrence(list))

# Factorial n = n*(n-1)*(n-2)...
# Factorial 3 = 3*2*1 = 6

def factorial_loop(x):
    factorial = 1
    for i in range(1, x + 1):
        factorial *= i
    return factorial

def factorial_recurrence(x):
    # base case
    if x <= 1:
        return 1
    # recursive case
    else:
        return x * factorial_recurrence(x - 1)


print("")
print("Factorial for loop: ")
print(factorial_loop(3))
print("")
print("Factorial for recurrence: ")
print(factorial_recurrence(3))