# Przykład procedury (technicznie: funkcji niezwracającej żadnej wartości przy pomocy instrukcji 'return'.
# Dwa parametry posiadają wartości domyślne

komunikat = "[Odmówił podania]"
def pacjent(numer, imie=komunikat, nazwisko=komunikat):
  print(f"Pacjent: nr={numer} imię: {imie} nazwisko: {nazwisko}")
#Testujemy wywołanie funkcji pacjent:
pacjent(4)
pacjent(5, "Jan", "Kowalski")

# Przykład funkcji rekurencyjnej z jednym parametrem
def silnia(n):
    if n == 0:
        return 1     # (**)
    else:
        return n * silnia(n - 1)

# Testujemy funkcję silnia
print("silnia(5)=", silnia(5))

# Przykład funkcji iteracyjnej z jednym parametrem głównym i drugim domyślnym

def silnia_it(n, res=1):
    while n!=0:
        res=n*res
        n=n-1
    return res

print("silnia iteracynie  (5)=", silnia_it(5)) # testujemy funkcję