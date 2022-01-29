#!/usr/bin/python3
import math


# A naive test of primacy
def is_prime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


# find all prime numbers up to n
def generator_prime(n):
    for i in range(2, n + 1):
        if is_prime(i):
            yield i


print(list(generator_prime(100)))

# solving with iterator
class iterator_prime:
    def __init__(self, n):
        self.i = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        while 1:
            self.i += 1
            if self.i > self.n:
                raise StopIteration
            if is_prime(self.i):
                return self.i


print(list(iterator_prime(100)))