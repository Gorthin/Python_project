import pathlib
import re
katalogBiezacy=pathlib.Path.cwd()  # Obiekt wskazujący na katalog bieżący
nazwapliku="Inne/autoupdate2.log"
plik=katalogBiezacy / nazwapliku

wzorzec1="0x[a-fA-F0-9]"
wzorzec2="pid: 43[78][0-9][0-9]"

wyrazenieReg1 = re.compile(wzorzec1)    # Zwraca skompilowany obiekt Regex
wyrazenieReg2 = re.compile(wzorzec2)

with plik.open() as f:  # Pomijam parametry domyślne mode="r", encoding="utf=8"
    print("*Wzorzec 1.: ", wzorzec1)
    for wiersz in f.readlines(): # Czytamy pojedyncze wiersze
        if wyrazenieReg1.search(wiersz) is not None:
            print(f" Odczytany wiersz: {wiersz}", end="")
            print(f" Zgodny z regex '{wzorzec1}'")
    f.seek(0)   # Powrót na początek pliku
    print("*Wzorzec 2.: ", wzorzec2)
    for wiersz in f.readlines():
        if wyrazenieReg2.search(wiersz) is not None:
            print(f" Odczytany wiersz: {wiersz}", end="")
            print(f" Zgodny z regex '{wzorzec2}'")

