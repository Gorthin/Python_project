# Zapis pliku CSV o jednolitej zawartości
import csv
import pathlib
nazwapliku="seria-output.csv"
pomiary=[ [15.2,2.1,3.2,3.3,5.5,6.60,1.01],
          [5.2,1.30,2.330,8.30,-4.50,-6.23,1.01],
          [3.22,20,50,50,70,80,1.20]]

plik=pathlib.Path(nazwapliku).open(mode="w", newline="") # Tryb zapisu 'w' - ang. write
CSVwriter=csv.writer(plik)
print("Zapisujemy wiersze do pliku CSV na podstawie listy:")
print(pomiary)
for wiersz in pomiary:
    CSVwriter.writerow(wiersz)
plik.close()
print("Sprawdzam zawartość pliku CSV:")
plik=pathlib.Path(nazwapliku).open()
print(plik.read())
plik.close()