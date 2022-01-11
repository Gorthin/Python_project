#!/usr/bin/python3

'''War (also known as Battle in the United Kingdom) is a simple card game,
typically played by two players using a standard playing card deck —
and often played by children. There are many variations, as well as related
games such as the German 32-card Tod und Leben ("Life and Death").

GAMEPLAY:
The objective of the game is to win all of the cards.
The deck is divided evenly among the players, giving each a down stack.
In unison, each player reveals the top card of their deck—this is
a "battle"—and the player with the higher card takes both of the cards
played and moves them to their stack. Aces are high, and suits are ignored.
If the two cards played are of equal value, then there is a "war".
Both players place the next three cards face down and then another card face-up.
The owner of the higher face-up card wins the war and adds all the cards on the
table to the bottom of their deck. If the face-up cards are again equal then
the battle repeats with another set of face-down/up cards. This repeats until
one player's face-up card is higher than their opponent's

Automatic War
Laying down a two of any suit causes a War to be declared.
'''

import random
colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]
print("Colors cards: ", colors)
print("Figures cards: ", figures)
print("======================================================================")
allCards = []
for c in colors:
    for f in figures:
        aCard = f.copy()
        aCard['Color'] = c
        allCards.append(aCard)

random.shuffle(allCards)
print("All card is shuffle: ", allCards)

print("======================================================================")

player1 = []
player2 = []
max = len(allCards)
for i in range(max):
    if i % 2 == 0:
        player1.append(allCards[i])
    else:
        player2.append(allCards[i])
print('-------PLAYER 1--------')
print(player1)

print('-------PLAYER 2--------')
print(player2)

print("======================================================================")

while len(player1) > 0 and len(player2) >0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    stack = []

    if card1['Power'] == card2['Power']:
        while card1["Power"] == card2["Power"]:

            print('WAR!', 'Figure power Player 1:', card1['Power'], '\t', 'Figure power Player 1:', card2['Power'])
            stack.append(card1)
            stack.append(card2)

            if len(player1) < 2:
                player2.extend(stack)
                player2.extend(player1)
                player1 = []
                print("PLAY -2 \t %d \t %d \t" % (card1['Power'], card2['Power']) + len(player2) * '*')
                break
            elif len(player2) < 2:
                player1.extend(stack)
                player1.extend(player2)
                player2 = []
                print("PLAY -1 \t %d \t %d \t" % (card1['Power'], card2['Power']) + len(player1) * '*')
                break
            else:
                card1 = player1.pop(0)
                card2 = player2.pop(0)
                stack.append(card1)
                stack.append(card2)
                card1 = player1.pop(0)
                card2 = player2.pop(0)
        else:
            if card1['Power'] > card2['Power']:
                stack.append(card1)
                stack.append(card2)
                player1.extend(stack)
                print("PLAY #1 Figure power from Player 1: %d \t Figure power from Player 2: %d \t" % (card1['Power'], card2['Power']), 'Player 1 win war!', 'Lenght card Player 1:', len(player1))
            else:
                stack.append(card1)
                stack.append(card2)
                player2.extend(stack)
                print("PLAY #2 Figure power from Player 1: %d \t Figure power from Player 2: %d \t" % (card1['Power'], card2['Power']), 'Player 2 win war!!', 'Lenght card Player 2:', len(player2))

    elif card1['Power'] > card2['Power']:
        player1.append(card1)
        player1.append(card2)
        print('PLAY=1 Figure power Player 1: %d Figure power Player 2: %d #Player 1 win!# Quantity card Player 1: %d Quantity card Player 2: %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        # print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')
    elif card1['Power'] < card2['Power']:
        player2.append(card2)
        player2.append(card1)
        print('PLAY=2 Figure power Player 1: %d Figure power Player 2: %d #Player 2 win!# Quantity card Player 1: %d Quantity card Player 2 %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        # print('PLAY-2 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')

if len(player1) > 0:
    print("PLAYER 1 WON!!!!!")
else:
    print("PLAYER 2 WON!!!!!")