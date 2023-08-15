# Obliczenia χ² 
# ==============

# ..  contents:: 

# Tabela χ² w statystyce zawiera 
# wartości funkcji skumulowanej dystrybucji χ², 
# CDF. 
#
# ..  math::
#
#     F(x;k) = \dfrac{\gamma \left( \frac{k}{2}, \frac{x}{2}\right)}{\Gamma\left(\frac{k}{2}\right)}
#
# Zobacz http://en.wikipedia.org/wiki/Space-time_tradeoff.
#
# Na podstawie sumy kwadratów, :math: `\ chi ^ 2` i stopni swobody,:math:` f`.
# Możemy obliczyć: math: `p = 1-F (\ chi ^ 2; k)` które jest prawdopodobieństwem 
#że wartość :math:`\ chi ^ 2` jest losowe.
# Wartość :math: `p \ leq 0.05` oznacza, że dane nie będą przypadkowe. Wartość 
# :math: `p> 0.05` oznacza, że hipoteza zerowa jest prawdopodobnie prawdziwa:
# dane są losowe. Im wyższa wartość :math: `p`, tym bardziej prawdopodobne, że 
# hipoteza zerowa jest prawdziwa. 
#
# Ten dokument przedstawia obliczenia CDF, :math: `F (x; k)`.
# Pokazuje kilka podejść do obliczeń dwóch wymaganych wartości, 
# :math: `\ gamma (s, z)` i :math: `\ Gamma (t)`.  Ostateczny wybór dotyczący użytecznej,  
# kompletnej funkcji gamma jest dokonywany na podstawie dokładności dla danego przypadku użycia.
#
# Zobacz http://en.wikipedia.org/wiki/Incomplete_gamma_function#Regularized_Gamma_functions_and_Poisson_random_variables 
#
# Zobacz http://en.wikipedia.org/wiki/Stirling%27s_approximation
#
# Zobacz http://dlmf.nist.gov/5 and http://dlmf.nist.gov/8
#
# Zobacz http://netlib.org/ szczególnie moduł 542

# Importy
# -------

# Moduły wymagane przez ten moduł.

import operator
from functools import reduce, lru_cache
from fractions import Fraction
import math
from typing import Iterator, Tuple, Callable, Iterable, TypeVar

# Silnia
# -----------

# Silnia jest używana w wielu miejscach do obliczeń 
# niekompletnych i kompletnych wartości funkcji gamma. 

# Użyliśmy następującej definicji silni: 
#
# ..  
#
# ..  math::
#
#     n! = \prod_{i=1}^{n} i

@lru_cache(128)
def fact(k: int) -> int:
    """Prosta silnia.

    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(3)
    6
    >>> fact(4)
    24
    """
    if k < 2:
        return 1
    return reduce(operator.mul, range(2,k+1))

# Implementacja używa `` reduce (operator.mul, ...  ) `` do obliczenia 
# iloczynu sekwencji liczb całkowitych. 
# Zastosowaliśmy `` @ lru_cache`` ponieważ funkcja jest często używana, 
# a mała domena możliwych wartości prowadzi do pewnych korzyści 
# z wykorzystania pamięci podręcznej. 

# Możemy również użyć `` math.factorial () ``.  Aby skorzystać z 
# pamięci podręcznej, musielibyśmy zrobić coś takiego. 
#
# ..  parsed-literal::
#
#     fact = lru_cache(128)(math.factorial)
#
# Stworzyłoby to podobnie buforowaną funkcję silni. 

# Niekompletna Gamma 
# -----------------

# Niekompletna (dolna) funkcja gamma jest wyliczana następująco: 
#
# ..  math::
#
#     \gamma(s,z) = \sum_{k=0}^{\infty} \dfrac {(-1)^k} {k!} \; \dfrac {z^{s+k}} {s+k}
#

def gamma(s: float, z: float) -> float:
    """Niekompletna funkcja gamma.

    >>> import math
    >>> round(gamma(1, 2),7)
    0.8646647
    >>> round(1-math.exp(-2),7)
    0.8646647
    >>> round(gamma(1, 3),7)
    0.9502129
    >>> round(1-math.exp(-3),7)
    0.9502129
    >>> round(gamma(0.5, 2),7)
    1.6918067
    >>> round(math.sqrt(math.pi)*math.erf(math.sqrt(2)),7)
    1.6918067
    """
    
    def terms(s: float, z: float) -> Iterator[float]:
        for k in range(1000):
            term = ((-1)**k/fact(k))*(z**(s+k)/(s+k))
            yield term
    
    T_ = TypeVar("T_")        
    def take_until(function: Callable[[T_], bool], source: Iterable[T_]) -> Iterator[T_]:
        for v in source:
            if function(v): return
            yield v
    ε = 1E-8
    return sum(take_until(lambda t: abs(t) < ε, terms(s, z)))

# Koncepcja polega na obliczeniu nieskończonej sekwencji 
# wartości dla :math: `\ dfrac {(-1) ^ k} {k!}  \; \dfrac {z^{s+k}} {s+k}`.
# Wyliczamy te wartości, gdy są większe niż :math: `\ epsilon`. 
#
# Napisaliśmy własną funkcję filtra ``take_until (end_condition, function)``.
# To zatrzymuje nieskończoną generację wyrażeń, gdy jest spełniony warunek końcowy.
#
# Alternatywą jest pojedyncza rekurencja ogonowa, którą możemy zoptymalizować 
# tworząc prostą pętlę ** for **, która emituje wyrażenia tak długo, aż wartości będą zbyt małe 
# na to by były istotne. 

#
# ..  parsed-literal::
#
#         sigma = 0
#         for k in range(1000):
#             term = ((-1)**k/fact(k))*(z**(s+k)/(s+k))
#             if abs(term) < ε: break
#             sigma += term
#         return sigma
#
# Możemy dalej optymalizować tę funkcję, używając stanowych 
# wewnętrznych zmiennych w pętli ** for **.  Moglibyśmy nieznacznie 
# poprawić wydajność za pomocą dwóch zmian. 
#
# Wyrażenie `` (-1) ** k`` odwraca znak w każdym z wyrazów. 
# Możemy użyć na przykład  ``1 if k% 2 == 0 else -1``, 
# który byłby nieco mniej kosztowny do ewaluacji. 
#
# Podobnie, tak naprawdę nie musimy obliczać  :math:`k!` dla
# rosnących wartości *k*. Zamiast tego moglibyśmy zastosować stanowe obliczenia 
# iloczynu, w których wynik mnożylibyśmy przez następną wartość 

# of *k*.

# Funkcja Gamma 1 
# -----------------

# Różne wartości kompletnej funkcji gamma są nieznaczne 
# błędne w różnych miejscach.  Wykonaliśmy trzy implementacje 
# w celu znalezienia najlepszej funkcji. 
#
# W Pythonie 3.2 jest funkcja `` math.gamma () ``. 
# Możemy ją porównać z naszymi wymaganiami.
#

# Kompletna funkcja gamma ma następującą definicję: 
#
# ..  math::
#
#     \Gamma(t) = \dfrac{1}{t} \prod_{k=1}^{\infty} \dfrac{\left(1+\frac{1}{k}\right)^t}{1+\frac{t}{k}}
#

def Gamma1(t: float) -> float:
    """Gamma Function.

    Gamma(n) == fact(n-1)

    >>> import math
    >>> round(Gamma1(2),0)
    1.0
    >>> round(Gamma1(3),0)
    2.0
    >>> round(Gamma1(4),0)
    6.0
    >>> round(Gamma1(5),0)
    24.0
    >>> round(Gamma1(.5), 7) # Not quite right
    1.7726754
    >>> round(math.sqrt(math.pi), 7)
    1.7724539
    """

    def num_den(t: float) -> Iterator[Tuple[float, float]]:
        for k in range(1, 1000):
            yield (1+1/k)**t, (1+t/k)

    T_ = TypeVar("T_")
    def take_until_star(
            function: Callable[[T_, T_], bool],
            source: Iterable[Tuple[T_, ...]]
        ) -> Iterable[Tuple[T_, ...]]:
        for v in source:
            if function(*v): return
            yield v

    prod = lambda x: reduce(operator.mul, x)
    fst = lambda x: x[0]
    snd = lambda x: x[1]
    ε = 1E-8

    terms = tuple(take_until_star(lambda n, d: abs(n/d-1) < ε, num_den(t)))

    return prod(map(fst, terms))/(t*prod(map(snd, terms)))

# Obejmuje to dwa iloczyny:  iloczyn licznika i mianownika 
:
# Funkcja `` num_den () `` emituje sekwencję par, `` (n, d) ``. 
#
# Możemy uznać ją za sekwencję następujących par: 
#
# ..  math::
#
#     \left\langle \left(1+\frac{1}{k}\right)^t, 1+\frac{t}{k} \right\rangle
#     \textbf{ for} 1 \leq k < \infty
#
# Napisaliśmy własną funkcję filtra ``take_until (end_condition, function)``.
# To zatrzymuje nieskończoną generację krotek, gdy jest spełniony warunek końcowy.
# dla krotek.  Nie możemy użyć prostej funkcji `` take_util () `` zdefiniowanej powyżej, ponieważ 
# sprawia, że praca z krotkami jest trochę niezgrabna.
# Ta wersja działa bardziej elegancko z krotkami wielowartościowymi.
#
# Jeśli :math:`\frac{\left(1+\frac{1}{k}\right)^t}{1+\frac{t}{k}}`
# jest bliskie 1, możemy zatrzymać pobieranie wartości
# z nieskończonego iteratora.  Zapiszemy tę sekwencję w zmaterializowanym obiekcie, 
# `` terms``, ponieważ musimy wykonać na sekwencji dwie redukcje. 
#
# Następnie podzielimy dwie wartości w sekwencji `` terms`` 
# korzystając z funkcji ``fst()`` i ``snd()``.
# Dzięki temu możemy obliczyć oddzielnie iloczyny w liczniku i mianowniku.
# Odraczamy obliczenbie ostatecznego dzielenia do samego końca 
# w celu zachowania jak najwięcej bitów dokładności.
#
# Oto alternatywna konstrukcja pętli.
#
# ..  parsed-literal::
#
#     p_num = p_den = 1
#     for n in range(1,1000):
#         num, den = (1+1/n)\*\*t, (1+t/n)
#         if abs(num/den-1) < ε: break
#         p_num \*= num
#         p_den \*= den
#     return p_num/(t*p_den)
#
# Zwróćmy uwagę, że wartość of :math:`\Gamma\left(\frac{1}{2}\right)` jest bardzo
# bliska zdefiniowanej wartości :math:`\sqrt{\pi}`.
# Wartości całkowite wymagają jednak zaokrąglania do zera miejsc, 
# aby wyświetlić oczekiwane wartości.

# Oto druga wersja używająca obiektów `` Fraction`` zamiast floats.
# Chodzi o to, aby obliczyć wartość ** exact **, w celu sprawdzenia,
# czy - być może - niewielkie rozbieżności między faktycznym a oczekiwanym wynikiem
# są rezultatem problemów z liczbami zmiennoprzecinkowymi. 

# Działa to tylko dla wartości `` int`` i `` Fraction``.  Nie działa
# dla dowolnych wartości ``float``. To nie jest duże ograniczenie 
# dla tej aplikacji.


def Gamma1f(t: float) -> float:
    """Gamma Function.

    Gamma(n) == fact(n-1)

    >>> import math
    >>> round(Gamma1f(2),0)
    Fraction(1, 1)
    >>> round(Gamma1f(3),0)
    Fraction(2, 1)
    >>> round(Gamma1f(4),0)
    Fraction(6, 1)
    >>> round(Gamma1f(5),0)
    Fraction(24, 1)
    >>> round(Gamma1f(Fraction(1,2)), 7) # Not quite right
    1.7726754
    >>> round(math.sqrt(math.pi), 7)
    1.7724539
    """

    def num_den(t: Fraction) -> Iterator[Tuple[Fraction, float]]:
        for k in range(1, 1000):
            yield (1+Fraction(1, k))**t, (1+t/k)

    T_ = TypeVar("T_")
    def take_until_star(
            function: Callable[[T_, T_], bool],
            source: Iterable[Tuple[T_, ...]]
        ) -> Iterable[Tuple[T_, ...]]:
        for v in source:
            if function(*v): return
            yield v

    prod = lambda x: reduce(operator.mul, x)
    fst = lambda x: x[0]
    snd = lambda x: x[1]
    ε = 1E-8

    t_f = Fraction(t)
    terms = tuple(take_until_star(lambda n, d: abs(n/d-1) < ε, num_den(t_f)))

    return prod(map(fst, terms))/(t_f*prod(map(snd, terms)))

# Zastąpiliśmy operację dzielenia w funkcji `` num_den () `` 
# obiektem ``Fraction()``. Zastąpiliśmy także wartość argumentu ``t``,
# obiektem ``Fraction``, ``t_f``.
#
# Dwa inne dzielenia pozostały na miejscu, ponieważ argumenty były
# egezmplarzami obiektów ``Fraction``:
#
# -  w funkcji ``num_den()``, zostaliwliśmy dzielenie, ponieważ argument,
#    ``t`` hest obiektem ``Fraction``.
#
# -  Końcowe dzielenie (pomiędzy dwoma obiektami ``Fraction`` objects) pozostało.
#
# Co ciekawe, daje to zasadniczo takie same wyniki jak poprzednie 
# wersja. To także nie jest zbyt dokładne dla wartości bliskich :math:``\frac{1}{2}``.

# Funkcja Gamma 2
# ------------------

# Nie jest jasne, czy możemy zrobić coś lepszego niż `gamma1 ()` `, ale warto to sprawdzić 
# w innych alternatywach.  Aproksymacja Nemesa ma 
# przewagę zwięzłości. 
#
# ..  math::
#
#     \Gamma(z) \sim \sqrt{ \frac{2\pi}{z} } \left( \frac{1}{e} \left(z+\frac{1}{12z-\frac{1}{10z}} \right) \right)^z
#

def Gamma2(z: float) -> float:
    """Gamma Function. Gergő Nemes version.

    Gamma(n) == fact(n-1)

    >>> import math
    >>> round(Gamma2(2),1)
    1.0
    >>> round(Gamma2(3),1)
    2.0
    >>> round(Gamma2(4),1)
    6.0
    >>> round(Gamma2(5),1)
    24.0
    >>> round(Gamma2(.5), 7) # Not quite right
    1.7630962
    >>> round(math.sqrt(math.pi), 7)
    1.7724539
    """
    t_1 = math.sqrt(2*math.pi/z)
    t_2 = (z+(1/(12*z-(1/(10*z)))))/math.e
    return t_1*t_2**z

# Podzieliliśmy wyrażenie na dwie części, aby je skrócić 
#
# ..  math::
#
#     t_1 &= \sqrt{ \frac{2\pi}{z} } \\
#     t_2 &= \frac{\left(z+\frac{1}{12z-\frac{1}{10z}} \right)}{e} \\
#     \Gamma(z) &= {t_1} \times {t_2}^z
#

# Jest to prosta, zamknięta ocena funkcji
# Jest niedokładna dla :math:`\Gamma \left( \dfrac{1}{2} \right)`.
# Dla wartości całkowitych jest jednak bardzo dobra.

# Funkcja Gamma 3
# -------------------

# Oto wersja Sterlinga. Sumuje sekwencję wartości.
#
# ..  math::
#
#     \Gamma(z) \sim e^{-z}z^z \sqrt{ \frac{2\pi}{z} } \left( \sum_{k=0}^\infty \dfrac{g_k} {z^k} \right)
#
# Oto początek sekwencji wartości :math:`g_k`.
#
# ..    math::
#
#       g_0	&=1,	\\
#       g_1	&=1/12,	\\
#       g_2	&=1/288,	\\
#       g_3	&=−139/51840,	\\
#       g_4	&=−571/24\,88320,	\\
#       g_5	&=1\,63879/2090\,18880,	\\
#       g_6	&=52\,46819/7\,52467\,96800.
#
# Istnieje zdefiniowana reguła do obliczania tych niejasnych wartości. 
# Jednakże zauważamy, że ostatni z nich znajduje się w pobliżu `` 10E-5``, to wystarczy 
# aby dać nam użytecznie trafną odpowiedź. 

# To nie jest ciąg zbieżny:  użycie większej liczby używanych wyrazów może faktycznie * zmniejszyć * 
# dokładność zbliżania.  Dla wartości, z którymi pracujemy, 
# wydaje się, że nie potrzebujemy wszystkich sześciu wyrazów pokazanych powyżej. 


def Gamma3(z: float) -> float:
    """Funkcja Gamma. Wersja Sterlinga.

    http://dlmf.nist.gov/5.11#E3

    Gamma(n) == fact(n-1)

    >>> import math
    >>> round(Gamma3(2),1)
    1.0
    >>> round(Gamma3(3),1)
    2.0
    >>> round(Gamma3(4),1)
    6.0
    >>> round(Gamma3(5),1)
    24.0
    >>> round(Gamma3(.5), 7)
    1.7737381
    >>> round(math.sqrt(math.pi), 7)
    1.7724539
    """
    t_1 = math.exp(-z)*z**z
    t_2 = math.sqrt(2*math.pi/z)
    g = [1, 1/12, 1/288, -139/51840, -571/2488320, 163879/209018880, 5246819/75246796800]
    t_3 = sum(g[k]/(z**k) for k in range(2))
    return t_1*t_2*t_3

# Rozbiliśmy to na trzy części, aby zmniejszyć rozmiar całości 
# wyrażenia .
#
# ..  math::
#
#     t_1 &= e^{-z}z^z \\
#     t_2 &= \sqrt{ \frac{2\pi}{z} } \\
#     t_3 &= \sum_{k=0}^\infty \dfrac{g_k} {z^k} \\
#     \Gamma(z) &= t_1 \times t_2 \times t_3
#
# Jest to akceptowalne dla :math:`\Gamma \left( \dfrac{1}{2} \right)`.
# Zwróćmy uwagę, że użyliśmy tylko dwóch pierwszych wyrazów. Porownajmy wyniki z
# funkcją ``Gamma2()`` powyżej. Liczba wymaganych wyrazów
# zmienia się w zależności od zakresu wartości of :math:`z`.

# Gamma Hybrydowa
# -------------

# Większość przybliżeń nie jest bardzo dokładnych
# dla wartości :math:`\Gamma\left(\frac{k}{2}\right)`.
# W zamian możemy użyć tego dokładnego zamkniętego wyrażenia:
#
# ..  math::
#
#     \Gamma\left(\frac{1}{2}+n\right) = \frac{(2n)!}{4^n n!}\sqrt{\pi}
#
# Zapewnia ono precyzyjne wartości dla specjalnych przypadków, z których korzystamy.  

# Oto hybrydowa funkcja ``Gamma()``. W przypadku niektórych wartości używamy tej samej  
# wartości :math:`\Gamma\left(\frac{1}{2}+n\right)`. Dla innych wartości
# użyjemy powyższego przybliżenia ``Gamma2()``.

def Gamma_Half(k: float) -> float:
    """Gamma(k) z przypadkiem specjalnym dla k = n+1/2; k-1/2=n.

    >>> import math
    >>> round(Gamma_Half(2),1)
    1.0
    >>> round(Gamma_Half(3),1)
    2.0
    >>> round(Gamma_Half(4),1)
    6.0
    >>> round(Gamma_Half(5),1)
    24.0

    >>> round(Gamma_Half(.5), 7)
    1.7724539
    >>> round(math.sqrt(math.pi), 7)
    1.7724539
    >>> round(Gamma_Half(1.5), 7)
    0.8862269
    >>> round(math.sqrt(math.pi)/2, 7)
    0.8862269
    """
    ε = 1E-6
    if abs(k-int(k)-.5) < ε:
        n = int(k-.5)
        return fact(2*n)/(4**n*fact(n))*math.sqrt(math.pi)
    else:
        return float(Gamma2(k))

# Dla wartości :math: `n + \ dfrac {1} {2} \ pm \ epsilon`, użyjemy specjalnego 
# wyrażenia zamykającego. Jeśli wartość nie jest zbliżona do :math: `n + \ dfrac {1} {2}`,
# użyjemy bardziej ogólnego przybliżenia. 
# Wersja math.gamma () 
#
# --------- ------------------ 
# Oto przypadek testowy dla funkcji `` math.gamma () ``.


test_math_gamma = """
>>> import math
>>> round(math.gamma(2),2)
1.0
>>> round(math.gamma(3),2)
2.0
>>> round(math.gamma(4),2)
6.0
>>> round(math.gamma(5),2)
24.0

>>> round(math.gamma(.5), 7)
1.7724539
>>> round(math.sqrt(math.pi), 7)
1.7724539
>>> round(math.gamma(1.5), 7)
0.8862269
>>> round(math.sqrt(math.pi)/2, 7)
0.8862269
"""

# To też wygląda dobrze. Dla danych przypadków testowych działa tak samo 
# jak pokazana powyżej nasza hybryda 


# Skumulowana funkcja dystrybucji
# ==================================

# Rzeczywiste obliczenie CDF ze wzoru :math:`\chi^2` value, ``x`` oraz
# stopni swobody ``k``.

def cdf(x: float, k: int) -> float:
    """χ² skumulowana funkcja dystrybucji.

    :param x: wartość χ² -- ogólnie sum (obs[i]-exp[i])**2/exp[i]
        dla równoległych sekwencji obserwowanych i oczekiwanych wartości.
    :param k: stopnie swobody >= 1; ogólnie len(data)-1

    Z http://en.wikipedia.org/wiki/Chi-squared_distribution

    >>> round(cdf(0.004, 1), 2)
    0.95
    >>> round(cdf(10.83, 1), 3)
    0.001
    >>> round(cdf(3.94, 10), 2)
    0.95
    >>> round(cdf(29.59, 10), 3)
    0.001
    >>> expected=[0.95, 0.90, 0.80, 0.70, 0.50, 0.30, 0.20, 0.10, 0.05, 0.01, 0.001]
    >>> chi2= [0.004, 0.02, 0.06, 0.15, 0.46, 1.07, 1.64, 2.71, 3.84, 6.64, 10.83]
    >>> act= [round(x,3) for x in map(cdf, chi2, [1]*len(chi2))]
    >>> act
    [0.95, 0.888, 0.806, 0.699, 0.498, 0.301, 0.2, 0.1, 0.05, 0.01, 0.001]

    Z http://www.itl.nist.gov/div898/handbook/prc/section4/prc45.htm

    >>> round(cdf(19.18, 6), 5)
    0.00387
    >>> round(cdf(12.5916, 6), 2)
    0.05

    Z http://www.itl.nist.gov/div898/handbook/prc/section4/prc46.htm
    >>> round(cdf(12.131, 4), 5)
    0.01639
    >>> round(cdf(9.488, 4), 2)
    0.05

    """
    return 1-gamma(k/2, x/2)/Gamma_Half(k/2)

# Obliczenie 1 minus współczynnik częściowej funkcji
# gamma do kompletnej funkcji gamma.

# Przypadki testów jednostkowych
# ===============

# Będziemy używać komentarzy doctest w każdej z funkcji zdefiniowanych powyżej.
# Dodatkowo użyjemy ciągów z testowymi przypadkami testowymi.

__test__ = {
    "test_math_gamma": test_math_gamma,
}

def test(*args, **kw):
    import doctest
    doctest.testmod(*args, **kw)

if __name__ == "__main__":
    test()
