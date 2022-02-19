#!/usr/bin/env python3

def factorial1(n):
    if n == 0: return 1
    elif n == 1: return 1
    else:
        return n * (n-1)

def factorial2(n):
    if n == 0: return 1
    elif n == 1: return 1
    else:
        return n * factorial2(n-1)

def factorial3(n):
    if n > 1:
        return n*factorial3(n-1)
    return 1

def factorial4(n):
    s = 1
    for i in range(2, n+1):
        s *= i
    return s


print(factorial1(0))
print(factorial1(1))
print(factorial1(2))
print(factorial1(3))
print("="*30)
print(factorial2(0))
print(factorial2(1))
print(factorial2(2))
print(factorial2(3))
print("="*30)
print(factorial3(0))
print(factorial3(1))
print(factorial3(2))
print(factorial3(3))
print("="*30)
print(factorial4(0))
print(factorial4(1))
print(factorial4(2))
print(factorial4(3))
