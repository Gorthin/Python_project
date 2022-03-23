import pandas as pd # Alias nazwy pandas

""" Warianty odczytu CSV
# W systemie Windows użyj następującego formatu ścieżki: r"misiePanda\<nazwa pliku>.csv" 

# Wersja domyślna, poprawny układ z wierszem nagłówkowym:
pomiary = pd.read_csv("misiePanda/dane1.csv")

# Brak wiersza nagłówkowego:
pomiary = pd.read_csv("misiePanda/dane2.csv", header=None, names=["nazwa1","nazwa2","nazwa3", "nazwa4"])

# Jest wiersz nagłówkowy, ale definiujmy nasz własny nagłówek nadpisując domyślny:
pomiary = pd.read_csv("misiePanda/dane1.csv", header=0, names=["nazwa1","nazwa2","nazwa3", "nazwa4"])

"""

""" Warianty odczytu pliku Excela
# W systemie Windows użyj następującego formatu ścieżki: r"misiePanda\<nazwa pliku>.xlsx" 

# Wersja domyślna, tabela w pierwszej zakładce
pomiary = pd.read_excel("misiePanda/dane1.xlsx")

# Brak wiersza nagłówkowego i tabela zawarta jest w innej, niż pierwsza zakładce (tutaj: 'ArkuszExtra')

pomiary = pd.read_excel("misiePanda/dane2.xlsx", sheet_name='ArkuszExtra', header=None, \
                        names=["nazwa1","nazwa2","nazwa3", "nazwa4"])

# Jest obecny wiersz nagłówkowy, tabela zawarta w 'ArkuszExtra2' i przesunięta w dół o 1 wiersz:

pomiary = pd.read_excel("misiePanda/dane2.xlsx", sheet_name='ArkuszExtra2', header=1)


"""

pomiary = pd.read_excel("misiePanda/dane2.xlsx", sheet_name='ArkuszExtra2', header=1)

print("Tak Pandas zinterpretowało dane:\n",  pomiary.info())
print("Cała tabela:\n", pomiary)

print("Kształt tabeli:", pomiary.shape) # W naszym przykładzie zwróci (19,4)
print("Liczba wierszy:", pomiary.shape[0]) # W naszym przykładzie zwróci 19


print("Czytamy 3 wiersze z przodu:\n", pomiary.head(3))
print("Czytamy cały plik oprócz 6 ostatnich wierszy:\n", pomiary.head(-6))
print("Czytamy 2 wiersze od tyłu:\n",  pomiary.tail(2))



