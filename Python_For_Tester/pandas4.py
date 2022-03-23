import pandas as pd
pomiary = pd.read_csv("misiePanda/dane1.csv")
pomiary.dropna(inplace=True) # Kasujemy wierszy zawierających puste komórki (NaN)
# Modyfikacja typu danych w kolumnie:
pomiary["Max"]=pomiary["Max"].astype('uint8')
print("Zaimportowana tabela:\n", pomiary)
print("Dodaję kolumnę 'Pomiar OK?' i wypełniam ją wartością 'True', gdy 'Odczyt średni' wynosi 219")
pomiary["Pomiar OK?"] = (pomiary["Odczyt średni"]==219)
print(pomiary)
# Przeliczenie wartości w kolumnie:
print("Przeliczenie wartości w kolumnie 'Tryb pomiaru'")
def funkcyjka(x):
    if x=='A':      return "Pełny"
    elif x=='B':    return "Uproszczony"
    else:           return "Pozostałe"
pomiary["Tryb pomiaru"] = pomiary["Tryb pomiaru"].apply(funkcyjka)
print(pomiary)

print("Statystyki dla kolumny 'Max':")
print("   Średnia::", pomiary["Max"].mean())
print("   Mediana:",  pomiary["Max"].median())
print("   Min:",  pomiary["Max"].min())
print("   Max:",  pomiary["Max"].max())
print("   Wartość najczęściej występująca:",  pomiary["Max"].mode()[0])


print("Liczba satysfakcjonujących pomiarów")
print (pomiary.loc[pomiary["Pomiar OK?"] == True])


# Zliczanie wierszy posiadających określoną wartość:
print("Zliczanie wierszy posiadających określoną wartość w kolumnie: 'Tryb pomiaru'")
print (pomiary.groupby("Tryb pomiaru").count())

print ("Liczba pomiarów z Max=225:",pomiary.loc[pomiary["Max"] == 225])

print("Suma wartości 'Odczyt średni' dla tych pomiarów, w których Max=225:", end=" ")
print (pomiary.loc[pomiary["Max"] == 225]["Odczyt średni"].sum())

print("Wartość średnia wartości 'Odczyt średni' dla pomiarów, w których Max=225: ", end=" ")
print (pomiary.loc[pomiary["Max"] == 225]["Odczyt średni"].mean())

print("Sortowanie po wartości zawartej w kolumnie 'Urządzenie':'")
print(pomiary.sort_values(by="Urządzenie"))



import matplotlib.pyplot as plt

pomiary.plot()
plt.show()
