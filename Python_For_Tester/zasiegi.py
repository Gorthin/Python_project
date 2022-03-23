v = int()  # Pusta deklarcja zmiennej typu int
wynik = 6
print ("wynik=", wynik)

def pi_razy_drzwi(pi, drzwi):
    global x
    x=5
    wynik = pi*drzwi
    print("wynik=", wynik)


pi_razy_drzwi(3,4)

# print("x=", x)    # Zwróci błąd, x jest zmienną lokalną!

# Ilustracja użycia zmiennej globalnej w ciele funkcji:

def funkcyjka():
    global v # Odnosimy się do zmiennej globalnej v
    v=5
    print("Wywołanie lokalne, v=", x)

funkcyjka() # Wywołanie funkcji zmodyfikuje obiekt globalny przypisany do zmiennej v

v=v+1       # Kolejna modyfikacja zmiennej v, już poza ciałem funkcji
print("Wywołanie globalne, v=", v)

