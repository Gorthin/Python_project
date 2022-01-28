#!/usr/bin/python3

# polymorphism makes it possible to use methods with the same name in different classes


class shape:
    def __init__(self, name="Shape"):
        self.name = name

    def area(self):
        print("No data available on ", self.name)


class triangle(shape):
    def __init__(self, name="Triangle", a=2, h=2):
        super().__init__(name)
        self.a = a
        self.h = h

    def area(self):
        print("Figure area ", self.name)
        print(self.a * self.h / 2)


class rectangle(shape):
    def __init__(self, name="Eectangle", a=2, b=2):
        super().__init__(name)
        self.a = a
        self.b = b

    def area(self):
        print("Figure area ", self.name)
        print(self.a * self.b)


class square:
    def __init__(self, name="Square", a=3):
        self.name = name
        self.a = a

    def area(self):
        print("Figure area ", self.name)
        print(self.a ** 2)


def display_area(list):
    for x in list:
        x.area()

shape = shape()
triangle = triangle()
rectangle = rectangle()
square = square()

list = [shape, triangle, rectangle, square]
display_area(list)