import matplotlib.pyplot as plt
import numpy as np
# Plik danedowykresu.csv zawiera te same dane, jakie użyto w wykres2.py

osX, osY, osY2 = np.loadtxt('danedowykresu.csv',
                                          delimiter=',', unpack=True)
seria1,=plt.plot(osX, osY,  marker='*', linestyle='--', color='k',
                 ms=10, linewidth = '1', label='Seria 1.') # Seria 1.
seria2,=plt.plot(osX, osY2, marker='o', linestyle='-',  color='k',
                 ms=10, linewidth = '1', label='Seria 2.') # Seria 1.
plt.title("Pomiary napięcia\n(dane pobrane z pliku CSV)")
plt.legend(handles=[seria1, seria2])
plt.xlabel("[t]")
plt.ylabel("[V]")
plt.legend()
plt.show()