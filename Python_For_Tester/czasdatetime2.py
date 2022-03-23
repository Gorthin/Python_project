import datetime

teraz = datetime.datetime.now()

print(f" Data -> Dzień: {teraz.day}, miesiąc: {teraz.month}, rok: {teraz.year}")
print(f" Czas -> Godzina: {teraz.hour}, minuta: {teraz.minute}, sekunda: {teraz.second}")
print("Modyfikacja składowych (miesiąc ustawiamy na 10, czyli październik")
teraz=teraz.replace(month=10)   # Maszyna czasu w akcji!
print("Obiekt po modyfikacji")
print(f" Data -> Dzień: {teraz.day}, miesiąc: {teraz.month}, rok: {teraz.year}")

print("Operacje arytmetyczne na obiektach 'datetime':")
d1=datetime.datetime(2021,5,1,0,0,0)            # Określony moment w czasie (1 maja 2021 r.)
print(" Data 1:                 ", str(d1))
d3=datetime.datetime(2021, 5, 3, 0, 0, 0)       # Określony moment w czasie (3 maja 2021 r.)

print(" Data 2:                 ", str(d3))
przesuniecie=datetime.timedelta(days=2, hours=1, minutes=5, seconds=30)
print(" Przesunięcie:               ", str(przesuniecie))
print(" Data 2 + 'Przesunięcie':", str(d3+przesuniecie))
print("Pierwszy maja wypada przed świętem 3 maja:", d1 < d3)

teraz = datetime.datetime.now() # Wracamy do prawdziwej daty...

print(teraz.strftime("%d.%m.%Y Nr tygodnia: %U (teraz)"))
delta=datetime.timedelta(days=25)
print( (teraz+delta).strftime("%d.%m.%Y Nr tygodnia: %U (teraz+25 dni)"))
