import sys

if len(sys.argv) !=4:
    print("""Wymagane użycie 3 parametrów:
    <plik wejściowy.csv> <plik wyjściowy.csv> <N>,
    gdzie N jest liczbą w zakresie 1-10""")
    print("Do widzenia!")
    exit()  # Zakończ dzialanie skryptu i wróć do systemu operacyjnego!
# W tym miejscu wiemy, że skrypt ma już poprawną liczbę parametrów (3),
# sprawdźmy teraz ich wartości. # W tym celu wykorzystamy pożyteczną metodę
# 'find' zawartą w klasie <str>. find(s) zwraca indeks pierwszego wystąpienia napisu
# 's' w badanym ciągu znaków lub wartość -1 w przeciwnym przypadku

par1=sys.argv[1].find(".csv")!=-1 #   Czy nazwa zawiera ".csv"? (<plik wejściowy.csv>)
par2=sys.argv[2].find(".csv")!=-1 #   Czy nazwa zawiera ".csv"? (<plik wyjściowy.csv>)

val=sys.argv[3]
# Nie pamiętasz, co robi funkcja 'int'? Zajrzyj do rozdziału 2.
par3= val.isdigit() and 1 <= int(val) <=10  #   Czy trzeci parametr to liczba? (N, gdzie 1<=N<=1)?

if not (par1 and par2 and par3):
    print ("Jeden z podanych parametrów jest błędny")
    print("Do widzenia!")
    exit()

print("Oto lista parametrów:", sys.argv[1:])
