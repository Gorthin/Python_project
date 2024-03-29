#!/usr/bin/env python3
"""Python. Programowanie funkcyjne

Rozdział 10, Spłaszczenie przykładowych danych NIST.

"""
import csv
import io
import random

raw_data = """\
Grupa 1	6.9	5.4	5.8	4.6	4.0
Grupa 2	8.3	6.8	7.8	9.2	6.5
Grupa 3	8.0	10.5	8.1	6.9	9.3
Grupa 4	5.8	3.8	6.1	5.6	6.2
"""

def row_iter_tab( source ):
    rdr= csv.reader( source, delimiter="\t" )
    return rdr
def pieces(grouped):
    for row in grouped:
        yield from ((row[0][-1], float(v)) for v in row[1:])
        #for t in ((row[0][-1], float(v)) for v in row[1:]):
        #    yield t

if __name__ == "__main__":
    grouped= tuple( row_iter_tab(io.StringIO(raw_data)))
    data= list(pieces(grouped))
    random.shuffle(data)
    print( data )

