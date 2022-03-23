import numpy as np
from matplotlib import pyplot as plt

osX=np.arange(-5, 6)       # Tablica 1-wymiarowa, seria liczb od -5 do +5
osY=[x*x+5 for x in osX]   # List comprehension działa też w NumPy (*)

print("x=", osX)  # [-5 -4 -3 -2 -1  0  1  2  3  4]
print("y=", osY)  # [30, 21, 14, 9, 6, 5, 6, 9, 14, 21]
plt.xlabel("X")
plt.ylabel("Y=X*X+5")
plt.title("Wykres utworzony przy użyciu tabel NumPy")
plt.plot(osX, osY,
         marker='.',        # Styl markera (tu: symbol gwiazdki)
         linestyle='--',    # Styl linii (tu: kreskowana)
         color='k',         # Kod koloru (tu: czarny)
         ms=10,             # Rozmiar markera
         linewidth = '1')   # Grubość linii
plt.show()

