# Moduł datetime - kilka przykładowych metod
import datetime
print("Odczyt daty i czasu w formacie napisu")
s=str(datetime.datetime.now())
print (f" Czas i data bieżące    - format pełny    {s}")
print (f" Czas i data bieżące - wersja skrócona {s[0:16]}")
print("Odczyt daty - dekompozycja składowych")
dzis=str( datetime.date.today() )
print(" Wydruk w formie tekstowej:", dzis)
dzis_rozszerz= datetime.datetime.strptime(dzis, "%Y-%m-%d")

print(f" Dzień: {dzis_rozszerz.day}, miesiąc: {dzis_rozszerz.month}, rok: {dzis_rozszerz.year}")

print("Odczyt daty i czasu - dekompozycja składowych")
teraz = datetime.datetime.now()
print(f" Data -> Dzień: {teraz.day}, miesiąc: {teraz.month}, rok: {teraz.year}")
print(f" Czas -> Godzina: {teraz.hour}, minuta: {teraz.minute}, sekunda: {teraz.second}")
print("Formatowanie daty i czasu:")
t = datetime.datetime.now()
print(t.strftime(" %Y-%m-%d %H:%M:%S"))
print(t.strftime(" %d/%m/%Y Nr tygodnia: %U"))
print(t.strftime(" %Y\\%m\\%d"))
print(t.strftime(" %I:%M:%S %p"))
print(t.strftime(" %A -  %b %d, %Y"))
