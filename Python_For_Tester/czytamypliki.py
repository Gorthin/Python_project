# Kilka popularnych metod odczytywania zawartości plików tekstowych
nazwapliku="inputs.txt"
""" Plik o podnej wyżej nazwie zawiera 3 wiersze (pierwszy ma 9 znaków plus znak nowej linii):
Linijka_1
A to jest drugi wiersz
Trzeci wiersz pliku 
"""

print("*** Odczyt pojedynczych znaków ***")

try:
    plik = open(nazwapliku, "r", encoding="utf-8")  # Wpisz złą nazwę pliku, np. inputs.txz, aby sprawdzić wyjątku!
except FileNotFoundError:
    print("Hm, gdzie ten plik??")
    exit()

print("Otwarto plik: ",plik.name)
print("Tryb otwarcia: ",plik.mode)

print("Pozycja kursora:", plik.tell())

print("4 znaki:[", plik.read(4),"]")
print("Pozycja kursora po przeczytaniu 4 znaków:", plik.tell())
print("5 kolejnych znaków znaki:[", plik.read(5),"]")
print("Ostatni znak to będzie znak nowej linii:[", plik.read(1),"]")
plik.close()            # Pamiętaj o zamykaniu pliku!

print("*** Odczyt pojedynczych wierszy ***")
# plik = open(nazwapliku, "r", encoding="ascii") # To się nie uda, jeśli w pliku będa polskie znaki...

plik = open(nazwapliku, "r") # Domyślnie: encoding="utf-8"

print("Linia 1.(3 znaki):", plik.readline(3))  # Czytamy tylko pierwsze 3 znaki z bieżącego wiersza
print("Linia 2.(pozostałe znaki):", plik.readline(), end="")
print("Linia 2.:", plik.readline(), end="")


print("pozycja.:", plik.tell())

#open()


print("Linia 3.:", plik.readline())
print("Linia 4.(tu nic nie ma, bo nie ma takiej linii):", plik.readline()) # Wiersz 4. nie istnieje i ta instrukcja nic nie zwróci
plik.close()

print("*** Konwersja zawartości pliku do listy zawierającej odczytane wiersze ***")
plik = open(nazwapliku, "r")
wiersze = plik.readlines()
print("Lista zawierająca wiersze odczytane z pliku:", wiersze)
print("Odczytamy wiersze zapisane w liście:")
for biezacyWiersz  in wiersze: # Sprawdźmy wynik konwersji pliku na listę
    print(biezacyWiersz, end="")
plik.close()

print("\n*** Iteracyjne odczytywanie wierszy ***")

i =0
plik = open(nazwapliku, "r")
for biezacyWiersz in plik:
    i=i+1
    print("Linia nr: ", i, ":", biezacyWiersz, end="")
plik.close()