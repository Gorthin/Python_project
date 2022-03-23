import datetime
dni=[ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dzis=str( datetime.date.today() )
print(dzis)
dzis_rozszerz= datetime.datetime.strptime(dzis, "%Y-%m-%d")
dzien   =int(dzis_rozszerz.day)        # Dzień
miesiac =int(dzis_rozszerz.month)      # Miesiąc
rok     =int(dzis_rozszerz.year)       # Rok

if (rok % 4 == 0) and (rok % 100 != 0) or (rok % 400 == 0): # Czy rok przestępny?
    dni[1]=29   # Luty będzie miał 29 dni

print(f"Dzień: {dzien}, miesiąc: {miesiac}, rok: {rok}")
print("Liczba dni w miesiącu wynosi", dni[miesiac-1])
