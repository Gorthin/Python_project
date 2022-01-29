#!/usr/bin/python3

# An iterator is an object that browses through the elements of a collection
# Lists, collections, dictionaries, tuples are iterable

list = [1, 3, 4]

iterator_list = iter(list)
print(iterator_list)
print(next(iterator_list))
print(next(iterator_list))
print(next(iterator_list))
# print(next(iterator_list))

# iter - initializes iterations
# next - returns the value of the element and moves on to the next
# Returns an exception when it reaches the end


class my_iterator:
    def __init__(self, max=10):
        self.x = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        x = self.x

        if x > self.max:
            raise StopIteration

        self.x += 5
        return x


for i in my_iterator(40):
    print(i)


class reverse:
    def __init__(self, data="Caption"):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration

        self.index -= 1
        return self.data[self.index]


for i in reverse():
    print(i, end="")

print("")

for i in reverse("capitol"):
    print(i, end="")

print("")

for i in reverse((3, 2, "z", 10, 'c')):
    print(i, end="")

print("")

for i in reverse([1,2,3,4,5]):
    print(i, end="")