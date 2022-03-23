#print("Wartość: ", nieznanaZmienna)                          # Python zgłosi błąd

""" tej kod jest już prawidłowy:

nieznanaZmienna=None                      # Ot, jakaś wstępna deklaracja, za którą nic się nie kryje
print("Wartość: ", nieznanaZmienna)       # Python wyświetli: "Wartość:  None"

"""

mojKod=0                            # Liczba całkowita (typ int)
mojParametr=3.14                    # Liczba zmiennopozycyjna (typ float)
wielkaLiczba=4.34561e13             # Notacja 'e': 4.34561 razy 10 do potęgi 13
mojNapis="Napis"                    # Zmienna tekstowa (typ obiektowy str)
mojaLista={"ala", "ma", "kota"}     # Zbiór elementów (kolekcja, typ obiektowy set)

print( mojKod, " --- ", type(mojKod), "\n",      # kod \n wymusza kontynuację w nowej linii
       mojParametr, " --- ", type(mojParametr), "\n",
       mojNapis, " --- ", type(mojNapis), "\n",
       mojaLista, " --- ", type(mojaLista) )
print("Wielka liczba=", wielkaLiczba)

print("Długość napisu:", len(mojNapis))

