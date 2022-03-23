# Kopia pliku complex.py bez elementów funkcji main ("goła" definicja)
class Complex():
       def __init__(self, pRe=0, pIm=0): # Konstruktor
              self.__re = pRe  # Tworzymy atrybut __re - część rzeczywista
              self.__im = pIm  # Tworzymy atrybut __im – część urojona

       def __str__(self): # Zwracamy obiektu jako napis nadający się do wydruku w funkcji print
              return str(self.__re) + "+" + str(self.__im) + "*i"

       def __add__(self, x2):  # Realizacja operatora + (suma dwóch liczb zespolonych)
              return Complex(self.__re + x2.__re, self.__im + x2.__im)

       @property
       def Re(self):
              return self.__re
       @property
       def Im(self):
              return self.__im