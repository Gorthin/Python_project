#!/usr/bin/python3

import random

def fast_sorting(list):
    lower = []
    equal = []
    greater = []

    if len(list) > 1:
        pivot = list[0]
        for x in list:
            if x > pivot:
                greater.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                lower.append(x)
        return fast_sorting(lower) + equal + fast_sorting(greater)
    else:
        return list


def fast_sorting2(list):
    if len(list) > 1:
        return (
            fast_sorting([x for x in list[1:] if x < list[0]])
            + [x for x in list if x == list[0]]
            + fast_sorting([x for x in list[1:] if x > list[0]])
        )
    else:
        return list


list = []
for i in range(15):
    list.append(random.randint(0, 100))

print(list)
print(fast_sorting(list))
print(fast_sorting2(list))