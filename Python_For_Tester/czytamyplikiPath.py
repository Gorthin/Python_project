import pathlib
katalogBiezacy=pathlib.Path.cwd()  # Obiekt wskazujący na katalog bieżący
nazwapliku="inputs.txt"
plik=katalogBiezacy / nazwapliku

""" Plik o podnej wyżej nazwie zawiera 3 wiersze (pierwszy ma 9 znaków plus znak nowej linii):
Linijka_1
A to jest drugi wiersz
Trzeci wiersz pliku 
"""

print("Odczytujemy plik tekstowy, używając metody 'open' z klasy 'Path'")
print("-Czytamy cały plik za jednym zamachem:")

with plik.open(mode="r", encoding="utf=8") as f:
    tekst=f.read() #  Czytamy cały plik od razu
print(tekst)

print("- Czytamy pojedyncze linie:")

with plik.open() as f:  # Pomijam parametry domyślne mode="r", encoding="utf=8"
    for wiersz in f.readlines(): # Czytamy pojedyncze wiersze
        print(f"  Odczytany wiersz: {wiersz}", end ="")
print()