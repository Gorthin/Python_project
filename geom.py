#!/usr/bin/python3

def GiveGeomSeqElement(a1=2, factor=2, index=2):
    # returns n-th term of geometric sequence starting with element a1 and having
    value = a1 * pow(factor, index - 1)
    return value


def GiveFactorForGeomSeq(term, nextterm):
    # returns factor for geometrical sequence having two following terms of the sequence
    return nextterm / term


def GiveSumOfNElementsGeomSeq(a1=2, factor=2, n=2):
    # returns sum of n first elements of geometrical sequence with first term a1 and factor
    sumN = a1 * (1 - pow(factor, n)) / (1 - factor)
    return sumN
