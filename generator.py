#!/usr/bin/python3

# generator is a function to create an iterator


def generator():
    yield 1
    yield 2
    yield 8


print("Generator1: ")

for i in generator():
    print(i)

x = generator()
print(next(x))
print(next(x))
print(next(x))


def generator2(a, b):
    while a <= b:
        yield a
        a += 3


print("")
print("Generator2: ")

for i in generator2(2, 20):
    print(i)

print("")
print("Reverse: ")


def reverse(data):
    for i in range(len(data) - 1, -1, -1):
        yield data[i]


for i in reverse("python"):
    print(i, end="")

for i in reverse((4, 3, 9, "k", 22)):
    print(i, end="")