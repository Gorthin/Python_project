#!/usr/bin/env python3
"""Python. Programowanie funkcyjne

Rozdział 15, zbiór przykładów 5.

Zobacz https://tools.ietf.org/html/rfc4648
"""
# pylint: disable=wrong-import-position

import random
rng = random.SystemRandom()

class TestRandom:
    def __init__(self):
        self.calls = 0
    def randrange(self, low, high):
        self.calls += 1
        return (self.calls % (high-low)) + low

import base64
def make_key_1(rng=rng, size=1):
    """Tworzy klucz znakowy 24 * size zawierający wielkie i małe litery, cyfry oraz znaki - i _ .

    >>> test_rng = TestRandom()
    >>> make_key_1(test_rng)
    'AQIDBAUGBwgJCgsMDQ4PEBES'
    >>> test_rng.calls
    18
    """
    key_bytes = bytes(rng.randrange(0, 256) for i in range(18*size))
    key_string = base64.urlsafe_b64encode(key_bytes).decode('us-ascii')
    return key_string

import hashlib
def make_key_2(rng=rng, size=2):
    """Tworzy klucz o stałym rozmiarze zawierający wielkie i małe litery, cyfry oraz znaki - i _ .
    sha384 tworzy 48 bajtów zakodowanych jako 64 znaki.
    Losowość zwiększa parametr size, a nie długość .

    >>> test_rng = TestRandom()
    >>> make_key_2(test_rng)
    'Luk-0U4W3bGXW0OF_UE9WYMS3ERY92eJsJnmy8khCkBVCglz0MlzuPlM1wgm1KrM'
    >>> test_rng.calls
    512
    """
    raw_bytes = bytes(rng.randrange(0, 256) for i in range(256*size))
    key_bytes = hashlib.sha384(raw_bytes).digest()
    key_string = base64.urlsafe_b64encode(key_bytes).decode('us-ascii')
    return key_string

def make_key_3(rng=rng, size=1):
    """Tworzy znakowy klucz 32 * size zawierający wielkie i małe litery, cyfry oraz znaki - i _ .

    >>> test_rng = TestRandom()
    >>> make_key_3(test_rng)
    'AEBAGBAFAYDQQCIKBMGA2DQPCAIREEYU'
    >>> test_rng.calls
    20
    """
    key_bytes = bytes(rng.randrange(0, 256) for i in range(20*size))
    key_string = base64.b32encode(key_bytes).decode('us-ascii')
    return key_string

import uuid
make_key_4 = lambda: uuid.uuid4()

import secrets
def make_key_5(size=1):
    """
    Tworzy klucz znakowy 24*size
    """
    return secrets.token_urlsafe(18*size)

def demo():
    print(make_key_1())
    print(make_key_2())
    print(make_key_3())
    print(make_key_4())
    print(make_key_5())

def test():
    import doctest
    doctest.testmod(verbose=1)

if __name__ == "__main__":
    test()
    demo()
