# Pewna część wspólna
import sys
print(f"Cześć, tu skrypt {sys.argv[0]}!")
timing1 = sys.argv[1] # Odczytujemy parametr 1.
timing2 = sys.argv[2] # Odczytujemy parametr 2.
print("timing1=", timing1)
print("timing2=", timing2)

# Wywołaj kod z innych skryptów:
import roboczy1
import roboczy2
import roboczy3
