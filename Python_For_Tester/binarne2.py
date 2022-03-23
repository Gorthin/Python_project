import pickle

with open("binarne1.bin", "rb") as plik_in:
    pracownicy_z_dysku = None                   # Nowa, pusta zmienna
    pracownicy_z_dysku = pickle.load(plik_in)   # Ładujemy zawartość nowej zmiennej danymi odczytanymi z dysku
    print("Słownik odczytany z dysku:")
    print(pracownicy_z_dysku)                   # Użycie with/as pozwala unikać jawnego zamykania pliku

print("Dodajemy nowy wpis do słownika odczytanego z dysku:") # W tym miejscu operujemy na obiekcie znajdującym się w pamięci komputera
osoba=input("Podaj dane nowej osoby (Imię Nazwisko): ")
telefon=int(input("Podaj nr telefonu: "))
pracownicy_z_dysku[osoba]=telefon               # Rozszerzamy słownik o nowy wpis
print("Słownik odczytany z pamięci komputera:")  # Sprawdzamy zawartość słownika
print(pracownicy_z_dysku)

print("Zapis zmodyfikowanego słownika na dysk")
plik_out=open("binarne1.bin", "wb")             # Otwieramy klasycznie, bez with/as
pickle.dump(pracownicy_z_dysku, plik_out)
plik_out.close()                                # Wymagane jawne zamknięcie pliku
print("Uruchom program ponownie, aby sprawdzić wynik!")