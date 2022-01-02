height = 11

for i in range(height):
    print((' ' * (height - i)) + ('*' * ((2 * i) + 1)))
print((' ' * height) + '|')

#color christmas tree

import random
height = 11
for i in range(height):
    print(' ' * (height - i), end='')
    for j in range((2 * i) + 1):
        if random.random() < 0.1:
            color = random.choice(['\033[1;31m', '\033[33m', '\033[1;34m'])
            print(color, end='')  #  the lights
        else:
            print('\033[32m', end='')  #  green
        print('*', end='')
    print()
print((' ' * height) + '|')

#christmas tree turtle
#
import turtle
screen = turtle.Screen()
screen.setup(800,600)
#
circle = turtle.Turtle()
circle.shape('circle')
circle.color('red')
circle.up()
circle.goto(0,100)
circle.stamp()
#
square = turtle.Turtle()
square.shape('square')
square.color('green')
square.up()
square.goto(0,200)
square.stamp()
#
turtle.exitonclick()