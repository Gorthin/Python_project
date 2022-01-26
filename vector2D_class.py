#!/usr/bin/python3

# class representing a 2D vector (x,y)
import math

class vector:
    # initialize method that is called when a new object is created
    # I used the word 'bike' to make it clear that you do not need to use the keyword self
    def __init__(bike, x=0.0, y=0.0):
        bike.x = x
        bike.y = y

    # we want our facilities to have +
    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)

    # we want += to work for our objects
    def __isadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    # we want our facilities to work -
    def __sub__(self, other):
        return vector(self.x - other.x, self.y - other.y)

    # we want our facilities to work *
    def __mul__(self, other):
        return vector(self.x * other.x, self.y * other.y)

    # / We want our facilities to work /
    def __div__(self, other):
        return vector(self.x / other.x, self.y / other.y)

    # we count the length
    def length(self):
        return int(math.sqrt(self.x ** 2 + self.y ** 2))

    # we count the angle
    def angle(self):
        return int(math.degrees(math.atan2(self.y, self.x)))

    # display info
    def display(self):
        return (
            "Coordinate x is "
            + str(self.x)
            + " Coordinate y is "
            + str(self.y)
            + " Length vector is "
            + str(self.length())
            + " Angle vector is "
            + str(self.angle())
        )

vector1 = vector(6, 2)
vector2 = vector(4, 8)
vector3 = vector1 + vector2
vector3 += vector2
vector4 = vector1 * vector2

print("Vector1: ", vector1.display())
print("Vector2: ", vector2.display())
print("Vector3: ", vector3.display())
print("Vector4: ", vector4.display())