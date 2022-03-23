import numpy as np
from matplotlib import pyplot as plt

t1 = np.arange(-5, 6)   #  Od -5 do +5, co 1
t2=[x*x-5 for x in t1]  # Obliczamy funkcję x^2-5 z wartości pobranych z t1
t3=[3*x-2 for x in t1]  # Obliczamy funkcję 3x-2 z wartości pobranych z t1

print("t1:", t1)        # [-5 -4 -3 -2 -1  0  1  2  3  4  5]
print("t2:", t2)        # [20,   11, 4, -1, -4, -5, -4, -1, 4, 11, 20]
print("t3:", t3)        # [-17, -14, -11, -8, -5, -2, 1, 4, 7, 10, 13]

t3 = np.vstack((t1, t2, t3))    # Składamy wszystko do jednej tablicy
print("t3 po zastosowaniu vstack(t1, t2, t3): ",t3)
t3=t3.transpose()
print("t3 transpozycji:", t3)

plt.xlabel("X")
plt.ylabel("Wykresy")
plt.title("Wykres utworzony przy użyciu tabel NumPy")
plt.plot(t3[:,0:1], t3[:,1:3],  # Pierwsza kolumna: oś X, druga i trzecia kolumna - wartości osi Y
         marker='.',            # Styl markera (tu: symbol gwiazdki)
         ms=10,                 # Rozmiar markera
         linewidth = '1')       # Grubość linii
plt.show()
