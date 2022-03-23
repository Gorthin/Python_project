# Zapis CSV zawierającego wiersz nagłówkowy
import csv
import pathlib
pomiary=[
    {"Miernik":"Sonel",    "Data":"2021-05-20", "Odczyt": 130.42},
    {"Miernik":"CEM",      "Data":"2021-05-20", "Odczyt": 129.13},
    {"Miernik":"Fluke",    "Data":"2021-05-21", "Odczyt": 130},
    {"Miernik":"Fluke",    "Data":"2021-05-21", "Odczyt": 119.99},
    {"Miernik":"Voltcraft","Data":"2021-05-21", "Odczyt": 131.01}]

nazwapliku="seriaH-output.csv"
plik=pathlib.Path(nazwapliku).open(mode="w", encoding="utf-8", newline="")  # Tryb zapisu 'w' - ang. write
CSVwriter=csv.DictWriter(plik, fieldnames=["Miernik","Data", "Odczyt"]) # Zwróć uwagę na etykiety nagłówka
CSVwriter.writeheader()         # Zapis wiersza nagłówka
CSVwriter.writerows(pomiary)    # Zapis pozostałych wierszy
plik.close()

print(f"Sprawdzam zawartość pliku '{nazwapliku}':")
plik=pathlib.Path(nazwapliku).open()
print(plik.read())
plik.close()