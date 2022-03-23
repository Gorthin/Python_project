import datetime
import math

# Klasa wyposażona we właściwości (properties), oraz oferująca jedną zmienną klasową

class Pomiar():
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
p1=Pomiar("Tester1",  220.1)
print(f"Obiekt 'p1' to [{p1}]")
print("Licznik obiektów:", Pomiar.Licznik)

p2=Pomiar("Tester2", 200)
print(f"Obiekt 'p2' to [{p2}]")
print("Licznik obiektów:", Pomiar.Licznik)

p3=Pomiar("Tester1", -221)
print(f"Obiekt 'p3' to [{p3}]")
print("Licznik obiektów:", Pomiar.Licznik)

#print(p1._autor)     # AttributeError: 'Pomiar' object has no attribute '_autor' (*)
print(f"Obiekt 'p3' utworzył {p3.autor}, data: {p3._dataczas}")
print("Modyfikujemy p3 - wartość zmieniona na -230:")
#p1.Autor="222" # AttributeError: can't set attribute (zablokowaliśmy możliwość modyfikacji) (**)
p3.odczyt=-230
print(f"Obiekt 'p3' to teraz [{p3}]")

p3.komunikat()