a, b = 0, 1
for i in range(0,31):
    print('Step',i,"value",a)
    a, b = b, a + b
print("=============")

# we obtain n first words of the Fibonacci sequence using the generator
def genFib(n):
    a, b = 0, 1
    for i in range(n + 1):
        yield a
        a, b = b, a + b

print(list(genFib(5)))

print("===============")
# we obtain n first words of the Fibonacci sequence using the iterator

class itFib:
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

lista = []

for x in itFib(5):
    lista.append(x)

print(lista)
print("===============")

def fibonacci_loop(x):
    previous_previous_number = 0
    previous_number = 0
    search_number = 1
    for i in range(1, x):
        previous_previous_number = previous_number
        previous_number = search_number
        search_number = previous_previous_number + previous_number

    return search_number


def fibonacci_recurrence(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci_recurrence(x - 1) + fibonacci_recurrence(x - 2)

print("")
print("Fibonacci for loop: ")
print(fibonacci_loop(10))
print("")
print("Fibonacci for recurrence: ")
print(fibonacci_recurrence(10))