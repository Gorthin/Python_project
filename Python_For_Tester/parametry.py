import sys
print (f"Nazwa pliku: {sys.argv[0]}")
print ("Liczba paramaterów", sys.argv.__len__()-1)
lista_parametrow=sys.argv[1:]
print("Lista parametrów:", lista_parametrow)
s=input("Naciśnij klawisz ")
