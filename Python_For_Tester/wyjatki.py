while True:
    try:
        x = int(input("Proszę wprowadzić liczbę: "))
        break
    except ValueError:
        # Możliwe jest także podanie listy wyjątków w nawiasie, np.: except (ValueError, TypeError)
        print ("Ups, to raczej nie jest liczba... Próbuj dalej.")
print (f"Brawo, na to czekałem! Wprowadzono liczbę: {x}")

while True:
    try:
        x = int(input("Proszę wprowadzić liczbę: "))
        break
    except ValueError as e:
        print ("Ups, to raczej nie jest liczba... Próbuj dalej.")
        print (e)
print (f"Brawo, na to czekałem! Wprowadzono liczbę: {x}")