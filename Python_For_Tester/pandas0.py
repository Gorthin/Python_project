import pandas as pd # Alias nazwy pandas
t1 = [4, 2, 8]   # Indeks domyślny jak w tablicach, tj. 0, 1, 2...
seria1 = pd.Series(t1)
print("seria1=")
print(seria1)
print("seria[1]=", seria1[1]) # Wypisze: 2 (wartość)

# Poniższa instrukcja wypisze: [2 8] (wartości na pozycjach indeksu 1. i 2.):

print("seria1[1, 2]=", seria1[[1, 2]].values)
wycinek=[True, False, True] # Poniższa instrukcja wypisze: [4 8] (wartości na pozycjach True):
print("seria1[True, False, True]=", seria1[wycinek].values)

t2 = [5, 'a', "Hello"]
indeksik=['a','b','c']
seria2 = pd.Series(t2, index=indeksik)
print("seria2=")
print(seria2)
print("seria2['a':'b']=",seria2['a':'b'].values) # Wycinek

limity = {"Miernik1":100.20, "Miernik2":120, "Miernik3":150.5, "Miernik4": 115, "Miernik5": 125}
seria3 = pd.Series(limity) # Seria utworzona na podstawie słownika Pythona
print("seria3=")
print(seria3)


wszedzietosamo = pd.Series(5, index=[x for x in range(10)]) # Seria dzisięciu liczb 5
print("wszedzietosamo=", wszedzietosamo.values)

