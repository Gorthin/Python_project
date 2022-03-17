#!/usr/bin/python3

'''Napisac funkcje, ktora przyjmuje jeden argument 'Specials' i zwraca wszystkie wiersze
z danych wejsciowych dla zadanego 'Specials'
'''

TABLE = [('S_Lenght', 'S_Width', 'P_Lenght', 'P_Width', 'Special'),
        (5, 2, 6, 1, 'carrier'),
        (4, 3, 8, 5, 'saltos'),
        (3, 7, 4, 6, 'randar'),
        (1, 8, 3, 1, 'plotes'),
        (9, 4, 2, 3, 'edente'),
        (6, 2, 8, 9, 'aserty')]

# print(TABLE[1][4])
def display_row(special):
    special = TABLE[1:]
    for i in special:
        print(i[4])

display_row(TABLE)
