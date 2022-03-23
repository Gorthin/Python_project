opcja = str()     # Deklaracja zmiennej, która zostanie zainicjowana później

while opcja != "q":
    print("""
     *** Dostępne opcje ***
       q - Wyjście
       1 - Uruchomienie testów
       2 - Analiza logów
       3 - Przerwa na kawę""")
    opcja = input("Wybierz opcję: ")
    print()
    if opcja == 'q':
        print("Do widzenia")
    elif opcja == "1":
        print("Wybrano: '1 - Uruchomienie testów ")
    elif opcja == "2":
        print("Wybrano: '2 - Analiza logów ")
    elif opcja == "3":
        print("Wybrano: '3 - Przerwa na kawę ")
    else:   # Błędna opcja
        print(f"Niepoprawna opcja {opcja}, spróbuj ponownie!")

# Opóźnienie wyjścia z programu

input("\n\nNaciśnij klawisz Enter")
