import pickle # Ten moduł umożliwia tzw. serializację obiektów Pythona i ich zapis do pliku dyskowego

# Zapisujemy słownik - strukturę danych Pythona - na dysk
pracownicy = {
    "Jan Kowalski":668168555,
    "Anna Zwinna":605123001,
    "Marek Ekspercki":721003050}
print("Lista Pythona:", pracownicy) # Sprawdzamy zawartość

plik_out=open("binarne1.bin", "wb")    # W tym pliku zapiszemy obiekt Pythona

pickle.dump(pracownicy, plik_out)
plik_out.close()
del pracownicy                          # Usuwamy obiekt z pomięci komputera

input("Zapisano do pliku, naciśnij Enter, aby sprawdzić wynik operacji:")

plik_in=open("binarne1.bin", "rb")                  # Sprawdzamy wynik
pracownicy_z_dysku = None                           # Pusta (na razie) zmienna
pracownicy_z_dysku = pickle.load(plik_in)           # Ładujemy zawartość nowej zmiennej danymi odczytanymi z dysku
print("Słownik odczytany z dysku:")
print(pracownicy_z_dysku)
plik_in.close()