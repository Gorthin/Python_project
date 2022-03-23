import sys
print (f"Nazwa pliku: {sys.argv[0]}")
print ("Liczba parametrów", len(sys.argv)-1)

lista_parametrow=sys.argv[1:]              # Kopiujemy argumenty do osobnej tablicy

print("Lista parametrów:", lista_parametrow)

for x in range(len(lista_parametrow)):
    print(f"Parametr nr {x+1}: {lista_parametrow[x]}")

print("Ścieżka interpretera Pythona:", sys.executable)
