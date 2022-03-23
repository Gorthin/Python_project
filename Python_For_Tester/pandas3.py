import pandas as pd
# W systemie Windows użyj następującego formatu ścieżki: r"misiePanda\<nazwa pliku>.csv"
# ‘inplace=True’ oznacza modyfikację oryginalnego obiektu, a nie tworzenie kopii

# Wersja podstawowa tego skrytu:
pomiary = pd.read_csv("misiePanda/dane1.csv")
pomiary.dropna(inplace=True) # Kasujemy wierszy zawierających puste komórki (NaN)

# Wersje alternatywne tego skrytu - przypadki są omówione w książce
# Użyj takie wersji jaka jest przydatna w danej sytucji

# 1) Poprawiamy typ danych w trakcie importu:
#mojetypy={'Tryb pomiaru': np.object, 'Odczyt średni': np.float64, 'Max': np.uint8, 'Urządzenie': np.object}
# Uwaga" w Pandas 'object' to tak naprawdę napis, nazwa jest  myląca
#pomiary = pd.read_csv("misiePanda/dane1.csv", dtype=mojetypy, nrows=10)
# Uwaga, obecność pustego wiersza wygeneruje błąd "ValueError: Integer column has NA values in column 2"
# Aby uniknąć takiej sytuacji, lepiej jest zmodyfikowac typu danych już w pamięci komputera, po załadowaniu
# serii i po jej wyczyszczeniu 

# 2) Poprawienie błędnej wartości (przykład)
#pomiary.loc[1, "Urządzenie"] ="Miernik-X" # Drugi wiersz zostanie poprawiony

# 3) Wykasowanie wierszy zawierających puste komórki, (NaN):
#pomiary.dropna(inplace=True)

# 4) Wykasowanie duplikatów:
#pomiary.drop_duplicates(inplace=True)

# 5) Wstawienie do pustych komórek pewnej arbitralnej wartości
#pomiary.fillna(250, inplace=True)

# 6) Wstawienie do pustych komórek wybranej kolumny pewnej arbitralnej wartości:
#pomiary["Max"].fillna(999, inplace=True)

# 7) Wstawienie do pustych komórek wybranej kolumny wartości średniej wyliczonej z pozostałych, niezerowych wartości:
#srednia=pomiary["Max"].mean()
#print("Wartość średnia w kolumnie Max=", srednia)
#pomiary["Max"].fillna(srednia, inplace = True)

# 8) Wstawienie do pustych komórek wybranej wartości mediany wyliczonej z pozostałych, niezerowych wartości:
#mediana=pomiary["Max"].median()
#print("Mediana w kolumnie Max=", mediana)
#pomiary["Max"].fillna(mediana, inplace = True)

# 9) Wstawienie do pustych komórek wartości najbardziej popularnej w danej kolumnie:
#pop=pomiary["Max"].mode()[0]
#print("Najbardziej popularna wartość występująca w kolumnie Max=", pop)
#pomiary["Max"].fillna(pop, inplace = True)

# 10) Przykładowe wykasowanie wybranych wierszy, np. takich dla których odczyt średni wyniósł poniżej 225V
#for x in pomiary.index:
#  if pomiary.loc[x, "Odczyt średni"] < 225:
#    pomiary.drop(x, inplace=True)

print("Zaimportowane typy danych:\n", pomiary.dtypes)
print("Zaimportowana tabela:\n", pomiary)
print("Zaimportowane typy danych:\n", pomiary.dtypes)

# Modyfikacj typu danych w kolumnie:
pomiary["Max"]=pomiary["Max"].astype('uint8')
print("Zaimportowana tabela:\n", pomiary)
print("Zaimportowane typy danych:\n", pomiary.dtypes)

print("Usuwam kolumnę 'Max':")
pomiary.drop(columns=["Max"], inplace=True)
print("Dodaję kolumnę 'Pomiar OK?' i wypełniam ją wartością 'False':")
pomiary["Pomiar OK?"]=False   # Dodanie nowej kolumny o nazwie "Pomiar OK?"

# Oznaczany wartością True w kolumnie „Pomiar OK?” wiersze "Odczyt średni" wynosi 219:
# Sposób 1.: NIEOPTYMALNY
#for x in pomiary.index:
#  if pomiary.loc[x, "Odczyt średni"] == 219:
#      pomiary.loc[x, "Pomiar OK?"] = True
# Sposób 2. - dodanie kolumny i wypełnienie jej wartością wynikająca z odczytu wartości z innej kolumny:
pomiary["Pomiar OK?"] = (pomiary["Odczyt średni"]==219)

print(pomiary)
print(pomiary.dtypes)

# Przeliczenie wartości w kolumnie:
print("Przeliczenie wartości w kolumnie 'Tryb pomiaru'")
def funkcyjka(x):
    if x=='A':      return "Pełny"
    elif x=='B':    return "Uproszczony"
    else:           return "Pozostałe"
pomiary["Tryb pomiaru"] = pomiary["Tryb pomiaru"].apply(funkcyjka)
print(pomiary)






