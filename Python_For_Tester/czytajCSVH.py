# Odczyt pliku CSV zawierającego wiersz nagłówkowy
import csv
import pathlib
nazwapliku="seriaH.csv"
""" Plik zawiera zrzut z bazy danych z systemu F/K:
Imię,Nazwisko,Wiek,Płaca,Mnożnik premii
Jan,Maria,40,4000,1.12
Anna,Zwinna,49,7500,1.60
Olek,Praktykant,40,3500,0
Magda,Onyks,35,6500,1.65
"""
plik=pathlib.Path(nazwapliku).open(mode="r", encoding="utf-8", newline='')
CSVreader=csv.DictReader(plik, delimiter=',')

print("Etykiety kolumn wiersza nagłówkowego:", CSVreader.fieldnames)
print("Wartości w słowniku można adresować, używając etykiet z wiersza nagłówkowego:")
print(f"{CSVreader.fieldnames[0]:10}{CSVreader.fieldnames[1]:11}\
{CSVreader.fieldnames[2]:5}{CSVreader.fieldnames[3]:6}\
{CSVreader.fieldnames[4]}")
for w in CSVreader:
    print(f"{w['Imię']:10}{w['Nazwisko']:11}{w['Wiek']:5}\
{float(w['Płaca']):8.2f}{float(w['Mnożnik premii']):8.2f}")
plik.seek(0)

print("Zawartość odczytanego pliku CSV odczytana jako lista słowników Pythona:")
for w in CSVreader:
    print(w)
plik.close()

