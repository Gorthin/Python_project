import time
def silnia(n):  # Silnia - wersja rekurencyjna
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)
def silnia_it(n, res=1): # Funkcja silnia - wersja iteracyjna
    while n!=0:
        res=n*res
        n=n-1
    return res
n=20
czasstart = time.time()
wynik=silnia(n)
czasend = time.time()
print(f"Silnia z {n} rekurencyjnie: {wynik}, czas: {czasend-czasstart:e}")
czasstart = time.time()
wynik=silnia_it(n)
czasend = time.time()
print(f"Silnia z {n} iteracyjnie: {wynik}, czas: {czasend-czasstart:e}")
