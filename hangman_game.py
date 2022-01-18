#!/usr/bin/python3

'''Game Rules:
The first player comes up with a word, revealing, for example,
by using horizontal dashes, the number of letters that make up the word.
The second player tries to guess the letters of the word.
Each time he succeeds, the first player puts a letter in
the right place; otherwise he draws the element of
a symbolic gallows and a man hanging on it.
If the first player draws a complete "hanging man"
before the second player guesses the word, then he wins.
Depending on the predetermined complexity of the "hanging man"
drawing (number of elements needed to draw it),
the game allows for more or less guessing mistakes'''

import random

  # welcome
print("Welcome in world of hangman! Give me Your nick: ")
nick = input()

  # list of pass
lists = ["hangman", "television", "bulding", "script", "linux"]

  # password
password = str(lists[random.randint(0, len(lists) - 1)])
table = list(password)

  # table usung to display ________
for i in range(len(password)):
    table[i] = "_"

  # variable representing number of our life
life = 6

  # loop while, in which will be realized game
while life > 0:
    print("")
    print(nick, " left ", life, " life")
    print("")
    print(" ".join(table))
    print(" ")

    # asked users about giving a letter
    print("Enter Your letter: ")
    letter = input()

    # You succeeded
    if letter in password:
        # changed sign _ on a letter
        for i in range(len(password)):
            if password[i] == letter:
                table[i] = letter
        # we check in teble is our password
        if "".join(map(str, table)) == password:
            print("")
            print(nick, " left ", life, " life")
            print("")
            print(" ".join(table))
            print(" ")
            print(nick, " YOU WIN!")
            break
    # we do not succeeded
    else:
        life -= 1