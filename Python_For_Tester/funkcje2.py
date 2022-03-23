# Przykład funkcji(procedury) ze zmienną liczbą parametrów

def parametry(*params):
    print ("Liczba parametrów: ", len(params))
    for x in range(0, len(params) ):             # Funkcja len() zwróci liczbę przekazanych parametrów
        print(f"Parametr {x}  to {params[x]} ")     # Wypisz każdy parametr
# Testujemy wywołanie funkcji parametry:

parametry(2, "New York", 6, 6.5)


print ("Przykład funkcji(procedury) ze zmienną liczbą parametrów - wersja 'słownikowa'")
# Przykład funkcji(procedury) ze zmienną liczbą parametrów - wersja "słownikowa"

def scenariusz_testowy(**params):
   t1=params["timing1"]
   t2=params["timing2"]
   s=params["napis"]
   print(f" timing1={t1}, timing2={t2}, napis={s}")

# Testujemy wywołanie funkcji scenariusz_testowy:
scenariusz_testowy(timing1=50, timing2=100, napis="ala")
scenariusz_testowy(timing5=50, timing2=100, napis="ala") # Błąd, patrz 'timing5'

