# Ten fragment kodu odpowiada za uruchomienie komendy systemowej odczytującej zawartość bieżącego katalogu
# Ponieważ jest to wersja przeznaczona dla macOS/Linux, to użyto komendy 'ls'

import subprocess
prog = subprocess.Popen("ls", stdout=subprocess.PIPE, shell=True)
(wynik, err) = prog.communicate()
print(f"'Surowy' wynik komendy \'ls\':\n {wynik} ")

# Otrzymany wynik jest zapisany jako ciąg bajtów tzn. zawiera prefiks b'
# oraz surową listę danych będących mieszanką nazw wykrytych w katalogu plików
# oraz znaków specjalnych np. '\n'

tmp=str(wynik)
tmp=tmp.lstrip('b\'') # Usuwamy prefiks 'b'
print("Wynik pozbawiony prefiksu:\n", tmp)


print("\nTak wygląda lista plików wykrytych w folderze :")
lista_plikow_all=tmp.split('\\n')
print(lista_plikow_all)

# Tworzymy drugą listę zawierającą wyłącznie plikami Pythona (.py)

lista_plikow_py=[]    # Pusta lista

for s in lista_plikow_all:            # Przeszukujemy listę wszystkich plików
    if s.find(".py") != -1:           # Znaleziono nazwę pliku z rozszerzeniem .py
        lista_plikow_py.append(s)     # Kopiujemy ją do listy lista_plikow_py

print("\nDrukujemy listę plików Pythona (*.py):")
# Drukujemy tylko plik Pythona
print(lista_plikow_py)

lista_plikow_py.sort(reverse=True)      # Sortowanie w kierunku wartości malejących:

print("\nDrukujemy listę plików Pythona (*.py) posortowaną zstępująco:")
print(lista_plikow_py)

