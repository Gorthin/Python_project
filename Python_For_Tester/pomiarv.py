import datetime
import math

# Ilustracja dziedziczenia klas

class Pomiar():  # Kod klasy jest kopią tego jaki został zawarty w pliku pomiar.py
       LimitNapiecia=250    # Zmienna klasowa (limit pomiarowy)
                            # Zmienna klasowa jest dostępny nawet, gdy nie utworzymy obiektów!
       Licznik=0            # Zmienna klasowa (liczbę utworzonych obiektów)

       def __init__(self, pAutor, pOdczyt):      # Konstruktor
              self._dataczas = str (datetime.datetime.now() )[0:19]  # Wynik będzie podobny do: 2021-04-20 13:51:27
              self._autor=pAutor
              if math.fabs(pOdczyt) <= Pomiar.LimitNapiecia:
                     self._odczyt = pOdczyt
              else:
                     raise Exception("Odczyt nie może przekroczyć wartości " + \
                                     str(Pomiar.LimitNapiecia) + "V")
              Pomiar.Licznik+=1    # Inkrementacja

       def __str__(self): # Obiekt jako napis
              return "Odczyt=" + str(self._odczyt) +\
                     " Dane kontrolne:|"+self._autor +"|"+self._dataczas
       # Realizacja koncepcji "właściwości":
       # Właściwości przeznaczone tylko do odczytu:
       @property
       def dataczas(self):
              return self._dataczas
       @property
       def autor(self):
              return self._autor
       # Jedna właściwość będzie przeznaczona do odczytu lub modyfikacji:
       @property
       def odczyt(self):
              return self._odczyt
       @odczyt.setter
       def odczyt(self, korekta):
              if math.fabs(korekta) <= Pomiar.LimitNapiecia:
                     self._odczyt = korekta
              else:
                     raise Exception("Odczyt nie może przekroczyć wartości " + \
                                     str(Pomiar.LimitNapiecia) + "V")
       def komunikat(self):
              print("Cześć, jestem obiektem klasy Pomiar!")
# --------- Kilka przykładów użycia: ------------------------------------------------------------
class PomiarV(Pomiar):
       DolnyLimit=100       # Wartości domyślne, do nadpisania
       GornyLimit=200
       def __init__(self, pAutor, pOdczyt, pNrSeryjny):  # Konstruktor
              super().__init__(pAutor, pOdczyt)          # Wywołujemy konstruktor klasy bazowej
              if pOdczyt >= PomiarV.DolnyLimit and pOdczyt <= PomiarV.GornyLimit:
                     self._odczyt = pOdczyt
              else:
                     raise Exception("Błąd zakresu")
              self._nrseryjny=pNrSeryjny                # Tworzymy nowe pole potrzebne w klasie PomiarV

       @property
       def odczyt(self):
              return self._odczyt

       @odczyt.setter
       def odczyt(self, korekta):
              if korekta >= PomiarV.DolnyLimit and korekta <= PomiarV.GornyLimit:
                     self._odczyt = korekta
              else:
                     raise Exception("Błąd zakresu")

       def __str__(self): # Obiekt jako napis
              s = super().__str__()                     # Wykorzystamy częściowo z kodu klasy bazowej!
              return s+" Nr seryjny="+self._nrseryjny   # Doklejamy informacje specyficzne dla klasy PomiarV
       def komunikat(self):
              print("Cześć, jestem obiektem klasy PomiarV!")
# --------- Kilka przykładów użycia: ------------------------------------------------------------

p1=Pomiar("Tester1",  220.1)
print(f"Obiekt klasy bazowej Pomiar 'p1' to [{p1}]")
print("Licznik obiektów:", Pomiar.Licznik)
print("Przechodzimy do domeny obiektów klasy OdczytV:")
print(f"Pierwotny limit dolny: {PomiarV.DolnyLimit} i limit górny: {PomiarV.GornyLimit}")
PomiarV.DolnyLimit=0 # Nadpisujemy oryginalne wartości zmiennych klasowych (*)
PomiarV.GornyLimit=30
print(f"Nowy limit dolny: {PomiarV.DolnyLimit} i limit górny: {PomiarV.GornyLimit}")

p2=PomiarV("Tester1",  5, "F123123B")
print(f"Obiekt klasy pochodnej PomiarV 'p2' to [{p2}]")
print("Licznik obiektów:", Pomiar.Licznik)

p3=PomiarV("Tester1",  30, "Z123123B")
print(f"Obiekt klasy pochodnej PomiarV 'p3' to [{p3}]")
print("Licznik obiektów:", Pomiar.Licznik) # Zgadnij jaka tu pojawi się wartość? (**)
p3.odczyt= 22.3 # Sprawdzamy działanie ‘settera’
print(f"Obiekt 'p3' po modyfikacji to [{p3}]")
print("Odczytujemy właściwość obiektu, używając metody klasy bazowej")
print("Czytam pole 'autor' obiektu p3: ", p3.autor)
p3.komunikat()
