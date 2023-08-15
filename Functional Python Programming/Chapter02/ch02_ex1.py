#!/usr/bin/env python3
"""Python. Programowanie funkcyjne

Rozdział 2, zbiór przykładów 1
"""
# pylint: disable=missing-docstring,wrong-import-position

from typing import Iterator
def numbers() -> Iterator[int]:
    for i in range(1024):
        # print(f"= {i}")
        yield i

def sum_to(n: int) -> int:
    sum: int = 0
    for i in numbers():
        if i == n:
            break
        sum += i
    return sum


def namedtuples():
    """porównanie wydajności nazwana krotka vs. klasa"""
    import timeit
    class_time = timeit.timeit(
        """x= X(1,2,3)""",
        """
class X:
    def __init__( self, a, b, c ):
        self.a= a
        self.b= b
        self.c= c
        """)
    print(f"klasa {class_time}")

    tuple_time = timeit.timeit("""x= (1,2,3)""")
    print(f"krotka {tuple_time}")

    collections_nt_time = timeit.timeit(
        """x= X(1,2,3)""",
        """
from collections import namedtuple
X = namedtuple( "X", ("a", "b", "c") )
        """)
    print(f"nazwana krotka {collections_nt_time}")

    typing_nt_time = timeit.timeit(
        """x= X(1,2,3)""",
        """
from typing import NamedTuple
class X(NamedTuple):
    a: str
    b: str
    c: str
        """)
    print(f"NamedTuple {typing_nt_time}")

import math
def isprimei(n: int) -> bool:
    """Czy n jest pierwsze?

    >>> isprimei(2)
    True
    >>> tuple( isprimei(x) for x in range(3,11) )
    (True, False, True, False, True, False, False, False)
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, 1+int(math.sqrt(n)), 2):
        if n % i == 0:
            return False
    return True

def isprimer(n: int) -> bool:
    """Czy n jest pierwsze?

    >>> isprimer(2)
    True
    >>> tuple( isprimer(x) for x in range(3,11) )
    (True, False, True, False, True, False, False, False)
    """
    def isprime(k: int, coprime: int) -> bool:
        """Czy k jest względnie pierwsze do wartości coprime?"""
        if k < coprime*coprime:
            return True
        if k % coprime == 0:
            return False
        return isprime(k, coprime+2)

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return isprime(n, 3)

def isprimeg(n: int) -> bool:
    """Czy n jest pierwsze?

    >>> isprimeg(2)
    True
    >>> tuple( isprimeg(x) for x in range(3,11) )
    (True, False, True, False, True, False, False, False)

    Stosunkowo wolny dla dużych liczb pierwszych, na przykład, M_61=2**61-1.

    >>> isprimeg(62710593)
    False
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return not any(n%p == 0 for p in range(3, int(math.sqrt(n))+1, 2))

def recursion():
    """Porównanie wydajności rekurencji.
    """
    import timeit
    print("isprimei",
          timeit.timeit(
              """isprimei(131071)""",
              """
import math
def isprimei( n ):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3,1+int(math.sqrt(n)),2):
        if n % i == 0:
            return False
    return True
              """, number=100000))

    print("isprimer",
          timeit.timeit(
              """isprimer(131071)""",
              """
def isprimer( n ):
    def isprime( n, coprime ):
        if n < coprime*coprime: return True
        if n % coprime == 0: return False
        return isprime( n, coprime+2 )

    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    return isprime( n, 3 )
              """, number=100000))

    print("isprimeg",
          timeit.timeit(
              """isprimeg(131071)""",
              """
import math
def isprimeg(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    return not any(n%p==0 for p in range(3,int(math.sqrt(n))+2))
              """, number=100000))

def limit_of_performance():
    """Widzimy, że testowanie dużej liczby pierwszej jest
    dość powolne. Testowanie dużych liczb niepierwszych jest dość szybkie.
    """
    import time

    t = time.perf_counter()
    for i in range(30, 89):
        m = 2**i-1
        print(i, m, end="")
        if isprimeg(m):
            print("prime", end="")
        else:
            print("composite", end="")
        print(time.perf_counter() - t)


__test__ = {
    'higher_order':
    """Funkcje wyższego rzędu.

>>> year_cheese = [(2000, 29.87), (2001, 30.12), (2002, 30.6),
... (2003, 30.66), (2004, 31.33), (2005, 32.62), (2006, 32.73),
... (2007, 33.5), (2008, 32.84), (2009, 33.02), (2010, 32.92)
... ]

>>> max( year_cheese )
(2010, 32.92)
>>> max( year_cheese, key= lambda yc: yc[1] )
(2007, 33.5)

Opakuj-przetwarzaj-rozpakuj
>>> max(map(lambda yc: (yc[1], yc), year_cheese))[1]
(2007, 33.5)

>>> wrapped = map(lambda yc: (yc[1], yc), year_cheese)
>>> processed = max(wrapped)
>>> processed[1]
(2007, 33.5)

>>> snd= lambda x: x[1]
>>> snd(max(map(lambda yc: (yc[1],yc), year_cheese)))
(2007, 33.5)

    """,
    'sum_non_strict':
    """Nieściśle wartościowane generatory.

>>> sum_to(5)
10
    """,
    'inne testy':
    """
>>> def example(a, b, **kw):
...     return a*b
...
>>> type(example)
<class 'function'>
>>> example.__code__.co_varnames
('a', 'b', 'kw')
>>> example.__code__.co_argcount
2
>>> isprimei(131071)
True
>>> isprimer(131071)
True
>>> isprimeg(131071)
True
    """
    }

def test():
    import doctest
    doctest.testmod(verbose=2)

if __name__ == "__main__":
    test()
    namedtuples()
    #recursion()
    #limit_of_performance()
