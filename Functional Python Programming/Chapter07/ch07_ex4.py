#!/usr/bin/env python3
"""Python. Programowanie funkcyjne

Rozdział 7, zbiór przykładów 4
"""
#pylint: disable=wrong-import-position,reimported

# Jeszcze bardziej ogólne przetwarzanie rankingu.

# from collections import namedtuple
# Rank_Data = namedtuple("Rank_Data", ("rank_seq", "raw"))

from typing import NamedTuple, Tuple, Any
class Rank_Data(NamedTuple):
    """
    Dwie podobne odmiany :
    - Rank_Data((rank,), data) -- ranking singleton
    - Rank_Data((rank, rank), data)
    
    >>> data = {'key1': 1, 'key2': 2}
    >>> r = Rank_Data((2, 7), data)
    >>> r.rank_seq[0]
    2
    >>> r.raw
    {'key1': 1, 'key2': 2}
    """
    rank_seq: Tuple[float]
    raw: Any

from typing import (
    Callable, Sequence, Iterator, Union, Iterable, TypeVar, cast,
    Union
)
K_ = TypeVar("K_") # Jakiś porównywalny typ kluczowy używany do rankingu.
Source = Union[Rank_Data, Any]  # Generyczny względem źródła
def rank_data(
        seq_or_iter: Union[Sequence[Source], Iterator[Source]],
        key: Callable[[Rank_Data], K_] = lambda obj: cast(K_, obj)
    ) -> Iterable[Rank_Data]:
    """Ranking nieprzetworzonych danych poprzez stworzenie obiektów Rank_Data z obiektu iterowalnego.
    Lub ponowne utworzenie rankingu istniejących danych przez stworzenie nowych obiektów Rank_Data na podstawie
    rych obiektów Rank_Data.

    >>> scalars = [0.8, 1.2, 1.2, 2.3, 18]
    >>> list(rank_data(scalars))  # doctest: +NORMALIZE_WHITESPACE
    [Rank_Data(rank_seq=(1.0,), raw=0.8), Rank_Data(rank_seq=(2.5,), raw=1.2),
     Rank_Data(rank_seq=(2.5,), raw=1.2), Rank_Data(rank_seq=(4.0,), raw=2.3),
     Rank_Data(rank_seq=(5.0,), raw=18)]

    >>> pairs = ((2, 0.8), (3, 1.2), (5, 1.2), (7, 2.3), (11, 18))
    >>> rank_x = tuple(rank_data(pairs, key=lambda x:x[0] ))
    >>> rank_x  # doctest: +NORMALIZE_WHITESPACE
    (Rank_Data(rank_seq=(1.0,), raw=(2, 0.8)),
     Rank_Data(rank_seq=(2.0,), raw=(3, 1.2)),
     Rank_Data(rank_seq=(3.0,), raw=(5, 1.2)),
     Rank_Data(rank_seq=(4.0,), raw=(7, 2.3)),
     Rank_Data(rank_seq=(5.0,), raw=(11, 18)))
    >>> rank_xy = (rank_data(rank_x, key=lambda x:x[1] ))
    >>> tuple(rank_xy)  # doctest: +NORMALIZE_WHITESPACE
    (Rank_Data(rank_seq=(1.0, 1.0), raw=(2, 0.8)),
     Rank_Data(rank_seq=(2.0, 2.5), raw=(3, 1.2)),
     Rank_Data(rank_seq=(3.0, 2.5), raw=(5, 1.2)),
     Rank_Data(rank_seq=(4.0, 4.0), raw=(7, 2.3)),
     Rank_Data(rank_seq=(5.0, 5.0), raw=(11, 18)))
    """
    if isinstance(seq_or_iter, Iterator):
        # To nie sekwencja? Materializacja obiektu sekwencji
        yield from rank_data(list(seq_or_iter), key)
        return
    data: Sequence[Rank_Data]
    if isinstance(seq_or_iter[0], Rank_Data):
        # Preferujemy kolekcję danych Rank_Data.
        data = seq_or_iter
    else:
        # Collection of non-Rank_Data? Convert to Rank_Data and process.
        empty_ranks: Tuple[float] = cast(Tuple[float], ())
        data = list(
            Rank_Data(empty_ranks, raw_data)
            for raw_data in cast(Sequence[Source], seq_or_iter)
        )

    for r, rd in rerank(data, key):
        new_ranks = cast(Tuple[float], rd.rank_seq + cast(Tuple[float], (r,)))
        yield Rank_Data(new_ranks, rd.raw)

from typing import Callable, Tuple, Iterator, Iterable, TypeVar, cast
def rerank(
        rank_data_iter: Iterable[Rank_Data],
        key: Callable[[Rank_Data], K_]
    ) -> Iterator[Tuple[float, Rank_Data]]:
    """Ponowne stworzenie rankingu poprzez dodanie kolejności rang do obiektu Rank_Data.
    """
    sorted_iter = iter(
        sorted(
            rank_data_iter, key=lambda obj: key(obj.raw)
        )
    )
    # Zastosowanie funkcji ranker to nagłówka head, *tail = sorted(rank_data_iter)
    head = next(sorted_iter)
    yield from ranker(sorted_iter, 0, [head], key)

from typing import Iterator, Tuple
def yield_sequence(
        rank: float,
        same_rank_iter: Iterator[Rank_Data]
    ) -> Iterator[Tuple[float, Rank_Data]]:
    """Emisja sekwencji takich samych wartości rang."""
    head = next(same_rank_iter)
    yield rank, head
    yield from yield_sequence(rank, same_rank_iter)

from typing import List
def ranker(
        sorted_iter: Iterator[Rank_Data],
        base: float,
        same_rank_seq: List[Rank_Data],
        key: Callable[[Rank_Data], K_]
    ) -> Iterator[Tuple[float, Rank_Data]]:
    """Wartości rang z sorted_iter przy użyciu wartości rangi podstawowej.
    Jeśli klucz następnej wartości pasuje do same_trank_seq, to go akumulujemy.
    Jeśli klucz następnej wartości jest inny, kumulujemy te same wartości rang
    i zaczynamy gromadzić nową sekwencję.

    >>> scalars= [0.8, 1.2, 1.2, 2.3, 18]
    >>> list(rank_data(scalars))  # doctest: +NORMALIZE_WHITESPACE
    [Rank_Data(rank_seq=(1.0,), raw=0.8), Rank_Data(rank_seq=(2.5,), raw=1.2),
     Rank_Data(rank_seq=(2.5,), raw=1.2), Rank_Data(rank_seq=(4.0,), raw=2.3),
     Rank_Data(rank_seq=(5.0,), raw=18)]
    """
    try:
        value = next(sorted_iter)
    except StopIteration:
        # Ostatnia partuia
        dups = len(same_rank_seq)
        yield from yield_sequence(
            (base+1+base+dups)/2, iter(same_rank_seq))
        return
    if key(value.raw) == key(same_rank_seq[0].raw):
        # Dopasowanie, akumulacja partii
        yield from ranker(
            sorted_iter, base, same_rank_seq+[value], key)
    else:
        # Brak dopasowania, emitujemy poprzednią partię i zaczynamy kolejną
        dups = len(same_rank_seq)
        yield from yield_sequence(
            (base+1+base+dups)/2, iter(same_rank_seq))
        yield from ranker(
            sorted_iter, base+dups, [value], key)

__test__ = {
    'example': '''
>>> scalars= [0.8, 1.2, 1.2, 2.3, 18]
>>> list(rank_data(scalars))
[Rank_Data(rank_seq=(1.0,), raw=0.8), Rank_Data(rank_seq=(2.5,), raw=1.2), Rank_Data(rank_seq=(2.5,), raw=1.2), Rank_Data(rank_seq=(4.0,), raw=2.3), Rank_Data(rank_seq=(5.0,), raw=18)]
'''
}

def test():
    import doctest
    doctest.testmod(verbose=True)

if __name__ == "__main__":
    test()
