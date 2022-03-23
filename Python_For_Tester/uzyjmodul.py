# Dwie wersje importowania modułów z pakietu:



from mytoolkit import matematyczne as mat     # Importujemy moduł i nadajemy mu alias nazwy ('mat' zamiast 'matematyczne')
from mytoolkit import pomocnicze as pom       # Importujemy moduł i nadajemy mu alias nazwy ('pom' zamiast 'pomocnicze')

# Użycie metod/funkcji/klas z mytoolkit/matematyczne (alias: 'mat')
print(mat.odejmij(2, 5))
print(mat.dodaj(2, 5))

# Użycie metod/funkcji/klas z mytoolkit/pomocnicze (alias: 'pom')
pom.drukuj("Dzień dobry. A na wypadek gdybyśmy się już potem nie widzieli – także dobry wieczór i dobranoc!")




