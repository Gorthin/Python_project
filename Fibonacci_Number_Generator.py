#!/usr/bin/python3

# We obtain the first n words of the Fibonacci sequence using the generator
def generator_fib(n):
    a, b = 0, 1
    for i in range(n + 1):
        yield a
        a, b = b, a + b


print(list(generator_fib(10)))

# We obtain the n first words of the Fibonacci sequence using the iterator


class iterator_fib:
    def __init__(self, n):
        self.a = 0
        self.b = 1
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > self.n:
            raise StopIteration
        self.i += 1
        x = self.a
        self.a, self.b = self.b, self.a + self.b
        return x


list = []

for x in iterator_fib(10):
    list.append(x)

print(list)