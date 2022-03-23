# Odczyt pliku CSV o jednolitej zawartości
import csv
import pathlib
nazwapliku="seria.csv"
""" Plik zawiera serie liczb:
10,20,30,30,50,60,100
50,10,30,30,50,60,100
30,20,50,50,70,80,120
"""
plik=pathlib.Path(nazwapliku).open(newline='')
CSVreader=csv.reader(plik, delimiter=',')

print("Prezentacja w formie tekstowej:")
for wiersz in CSVreader:
    print(wiersz)

plik.seek(0)    # Wracamy na początek pliku, aby ponownie odczytać plik
pomiary_int=[]  # Pusta lista
wiersz_int =[]  # Pusta lista (robocza)


for wiersz in CSVreader:
    for odczyt in wiersz:
        wiersz_int=[ int(odczyt) for odczyt in wiersz]  # Konwersje napisów na liczby (tutaj: int)
    pomiary_int.append(wiersz_int)
print("Prezentacja w formie listy załadowanej seriami liczb:")
print(pomiary_int)
plik.close()