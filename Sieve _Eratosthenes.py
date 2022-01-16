#!/usr/bin/python3

'''To find all the prime numbers less than or equal to a given integer n by Eratosthenes' method:

1 Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
2 Initially, let p equal 2, the smallest prime number.
3 Enumerate the multiples of p by counting in increments of p from 2p to n, and mark them in the list (these will be 2p, 3p, 4p, ...; the p itself should not be marked).
4 Find the smallest number in the list greater than p that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
5 When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.'''

def sieve(n):
    temp = [1 for x in range(n+1)]
    for i in range(2,n+1):
        for j in range(i+1, n+1):
            if j % i == 0:
                temp[j] = 0

    primes = []
    for i in range(2,len(temp)):
        if temp[i] == 1:
            primes.append(i)

    return primes

print(sieve(100))