#! /usr/bin/env python

''' Find the next permutation in lexicographic order after a given permutation

    This algorithm, due to Narayana Pandita, is from
    https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order

    1. Find the largest index j such that a[j] < a[j + 1]. If no such index exists, 
    the permutation is the last permutation.
    2. Find the largest index k greater than j such that a[j] < a[k].
    3. Swap the value of a[j] with that of a[k].
    4. Reverse the sequence from a[j + 1] up to and including the final element a[n].

    Implemented in Python by PM 2Ring 2015.07.28
'''

import sys

def next_perm(a):
    ''' Advance permutation a to the next one in lexicographic order '''
    n = len(a) - 1
    #1. Find the largest index j such that a[j] < a[j + 1]
    for j in range(n-1, -1, -1):
        if a[j] < a[j + 1]:
            break
    else:
        #This must be the last permutation
        print(f'This is a descending sequence: {a[::-1]}')
        return False


    #2. Find the largest index k greater than j such that a[j] < a[k]
    v = a[j]
    for k in range(n, j, -1):
        if v < a[k]:
            break

    #3. Swap the value of a[j] with that of a[k].
    a[j], a[k] = a[k], a[j]

    #4. Reverse the tail of the sequence
    a[j+1:] = a[j+1:][::-1]

    return True


def test(n):
    ''' Print all permutations of an ordered numeric string (1-based) '''
    i = 0
    while True:
        print(f'{i}: {n}')
        i += 1
        if not next_perm(n):
            break


def main():
    s = sys.argv[1] if len(sys.argv) > 1 else '123'
    a = list(s)
    next_perm(a)
    print('%s -> %s' % (s, ''.join(a)))


if __name__ == '__main__':
    test([3,2,1])
    #main()