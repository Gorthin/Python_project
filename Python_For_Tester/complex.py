# Realizacja klasy Complex() w której zabezpieczono pola wewnętrzne __re, __im
# realizując dostęp do nich przez właściwości Re, Im. Ponadto zrealizowano
class Complex():
       def __init__(self, pRe=0, pIm=0): # Konstruktor
              self._re = pRe  # Tworzymy atrybut _re - część rzeczywista
              self._im = pIm  # Tworzymy atrybut _im – część urojona

       def __str__(self): # Zwracamy obiektu jako napis nadający się do wydruku w funkcji print
              return str(self._re) + "+" + str(self._im) + "*i"

       def __add__(self, x2):  # Realizacja operatora + (suma dwóch liczb zespolonych)
              return Complex(self._re + x2._re, self._im + x2._im)

       @property
       def re(self):
              return self._re
       @property
       def im(self):
              return self._im

# --------- Kilka przykładów użycia: ------------------------------------------------------------
x = Complex(5,8)                # Tworzymy nowy obiekt x = 5 + 8*i
y = Complex(1,2)                # Tworzymy nowy obiekt y = 1 + 2*i
print(f"Obiekt 'x' to [{x}]")
print(f"Obiekt 'y' to [{y}]")
z=x+y
print(f"Obiekt z=x+y to [{z}]") # Sprawdźmy wynik dodawania x+y

""" Operacja niewspierana:
x.Re=2  --> Python zgłosi błąd "AttributeError: can't set attribute"

print(x.__re) --> Python zgłosi błąd  "AttributeError: 'Complex' object has no attribute '__re'"
"""