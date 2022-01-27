#!/usr/bin/python3

import random
from time import sleep


class warrior:
    def __init__(self, name="John", life=0, p_attack=0, p_defend=0):
        self.name = name
        self.life = life
        self.p_attack = p_attack
        self.p_defend = p_defend

    def attack(self):
        return random.randint(0, self.p_attack) * random.randint(2, 5)

    def defend(self):
        return random.randint(0, self.p_defend)

    def lost_life(self, quantity):
        self.life -= quantity
        if self.life <= 0:
            print(self.name, " fallen in battle")

    def is_alive(self):
        if self.life <= 0:
            return False
        else:
            return True

    def __str__(self):
        return self.name


def fight(dragon, knight):

    i = 1
    while dragon.is_alive() and knight.is_alive():
        print("Round nr: ", i)
        display_stat(dragon, knight)

        if random.randint(0, 1) == 0:
            duel(dragon, knight)
        else:
            duel(dragon, knight)

        print("")
        sleep(1)
        i += 1

    if knight.is_alive():
        print("The knight won the fight")
    else:
        print("The dragon won the fight")


def duel(x, y):
    print(x, " was attacked by ", y)
    injuries = y.attack() - x.defend()
    if injuries >= 0:
        print(x, " loss ", injuries, " life points.")
    else:
        print(x, "defended himself from attack")
    x.lost_life(injuries)


def display_stat(x, y):
    for i in (x, y):
        print(i, " has ", i.life, " life points.")


knight = warrior(
    "Knight", random.randint(100, 1000),
    random.randint(10, 50),
    random.randint(5, 30)
)
dragon = warrior(
    "Dragon",
    random.randint(100, 1000),
    random.randint(10, 50),
    random.randint(5, 30),
)

fight(dragon,knight)