#!/usr/bin/env python3
"""Python. Programowanie funkcyjne

Rozdział 9, zbiór przykładów 1

Zmienna ``MYPYPATH`` powinna zawierać ścieżkę do katalogu ``stubs``.
"""
# pylint: disable=wrong-import-position,wrong-import-order,unused-wildcard-import,reimported
import time
from PIL import Image

from itertools import product
from typing import TypeVar, Iterable, Iterator, Callable, Tuple
JT_ = TypeVar("JT_")
def join(
        t1: Iterable[JT_],
        t2: Iterable[JT_],
        where: Callable[[Tuple[JT_, JT_]], bool]
    ) -> Iterable[Tuple[JT_, JT_]]:
    return filter(where, product(t1, t2))

# from collections import namedtuple
# Color = namedtuple("Color", ("rgb", "name"))
from typing import NamedTuple
class Color(NamedTuple):
    rgb: Tuple[int, int, int]
    name: str

from itertools import dropwhile, islice
import csv
from typing import Sequence, cast
def get_colors(filename: str = "crayola.gpl") -> Sequence[Color]:
    with open(filename) as source:
        rdr = csv.reader(source, delimiter='\t')
        rows = dropwhile(lambda row: row[0] != '#', rdr)
        color_rows = islice(rows, 1, None)
        colors = list(
            Color(
                cast(Tuple[int, int, int], tuple(map(int, color.split()))),
                name
            )
            for color, name in color_rows)
    return colors

from typing import Iterator, Tuple
Point = Tuple[int, int]
RGB = Tuple[int, int, int]
Pixel = Tuple[Point, RGB]
def pixel_iter(img: Image) -> Iterator[Pixel]:
    w, h = img.size
    return (
        (c, img.getpixel(c))
        for c in product(range(w), range(h))
    )

import math
def euclidean(pixel: RGB, color: Color) -> float:
    return math.sqrt(
        sum(map(
            lambda x, y: (x-y)**2,
            pixel,
            color.rgb))
        )

def manhattan(pixel: RGB, color: Color) -> float:
    return sum(map(
        lambda x, y: abs(x-y),
        pixel,
        color.rgb))

def max_d(pixel: RGB, color: Color) -> float:
    return max(map(
        lambda x, y: abs(x-y),
        pixel,
        color.rgb))

# from itertools import islice
from typing import TypeVar, Iterable, List
T_ = TypeVar("T_")
def take(n: int, iterable: Iterable[T_]) -> List[T_]:
    """Zwraca pierwsze n pozycji obiektu iterowalnego jako listę"""
    return list(islice(iterable, n))

from itertools import groupby #, product
def matching_1(
        pixels: Iterable[Pixel],
        colors: Iterable[Color]
    ) -> Iterator[Tuple[Point, RGB, Color, float]]:

    xy = lambda xyp_c: xyp_c[0][0]
    p = lambda xyp_c: xyp_c[0][1]
    c = lambda xyp_c: xyp_c[1]

    distances = (
        (xy(item), p(item), c(item), euclidean(p(item), c(item)))
        for item in product(pixels, colors))
    for _, choices in groupby(distances, key=lambda xy_p_c_d: xy_p_c_d[0]):
        yield min(choices, key=lambda xypcd: xypcd[3])

test_matching_1 = """
>>> img= Image.open("IMG_2705.jpg")
>>> print(img) # doctest: +ELLIPSIS
<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3648x2736 at ...

>>> colors= get_colors()
>>> color_subset= list(islice(colors,0,None,len(colors)//6))
>>> print( color_subset )
[Color(rgb=(239, 222, 205), name='Migdałowy'), Color(rgb=(255, 255, 153), name='Kanarkowy'), Color(rgb=(28, 172, 120), name='Zielony'), Color(rgb=(48, 186, 143), name='Górska łąka'), Color(rgb=(255, 73, 108), name='Radykalna czerwień'), Color(rgb=(253, 94, 83), name='Zachodzące słońce'), Color(rgb=(255, 174, 66), name='Żółtopomarańczowy')]

>>> pixel_subset= tuple(take(10,pixel_iter(img)))

>>> print( list(matching_1(pixel_subset, color_subset)))
[((0, 0), (92, 139, 195), Color(rgb=(48, 186, 143), name='Górska łąka'), 82.75868534480233), ((0, 1), (92, 139, 195), Color(rgb=(48, 186, 143), name='Górska łąka'), 82.75868534480233), ((0, 2), (92, 139, 195), Color(rgb=(48, 186, 143), name='Górska łąka'), 82.75868534480233), ((0, 3), (91, 138, 194), Color(rgb=(48, 186, 143), name='Górska łąka'), 82.18272324521742), ((0, 4), (91, 138, 194), Color(rgb=(48, 186, 143), name='Górska łąka'), 82.18272324521742), ((0, 5), (91, 138, 194), Color(rgb=(48, 186, 143), name='Górska łąka'), 82.18272324521742), ((0, 6), (91, 138, 194), Color(rgb=(48, 186, 143), name='Górska łąka'), 82.18272324521742), ((0, 7), (91, 138, 194), Color(rgb=(48, 186, 143), name='Górska łąka'), 82.18272324521742), ((0, 8), (92, 139, 195), Color(rgb=(48, 186, 143), name='Górska łąka'), 82.75868534480233), ((0, 9), (93, 140, 196), Color(rgb=(48, 186, 143), name='Górska łąka'), 83.36666000266533)]

"""

test_matching_1_full = """
Zajmuje bardzo dużo czasu -- nie rób tego :

>>> colors= get_colors()
>>> img= Image.open("IMG_2705.jpg")
>>> revised= list( matching_1(pixel_iter(img), colors))
"""

def matching_2(
        pixels: Iterable[Pixel],
        colors: Iterable[Color]
    ) -> Iterator[Tuple[Point, RGB, Color, float]]:

    for xy, pixel in pixels:
        choices = map(
            lambda color: (
                xy, pixel, color, euclidean(pixel, color)
                ),
            colors)
        yield min(choices, key=lambda xypcd: xypcd[3])

test_matching_2 = """
>>> img= Image.open("IMG_2705.jpg")
>>> print(img) # doctest: +ELLIPSIS
<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3648x2736 at ...

>>> colors= get_colors()
>>> color_subset= list(islice(colors,0,None,len(colors)//6))
>>> print( color_subset )
[Color(rgb=(239, 222, 205), name='Migdałowy'), Color(rgb=(255, 255, 153), name='Kanarkowy'), Color(rgb=(28, 172, 120), name='Zielony'), Color(rgb=(48, 186, 143), name='Górska łąka'), Color(rgb=(255, 73, 108), name='Radykalna czerwień'), Color(rgb=(253, 94, 83), name='Zachodzące słońce'), Color(rgb=(255, 174, 66), name='Żółtopomarańczowy')]

>>> pixel_subset= tuple(take(10,pixel_iter(img)))

>>> print( list(matching_2(pixel_subset, color_subset)))
[((0, 0), (92, 139, 195), Color(rgb=(48, 186, 143), name='Górska łąka'), 82.75868534480233), ((0, 1), (92, 139, 195), Color(rgb=(48, 186, 143), name='Górska łąka'), 82.75868534480233), ((0, 2), (92, 139, 195), Color(rgb=(48, 186, 143), name='Górska łąka'), 82.75868534480233), ((0, 3), (91, 138, 194), Color(rgb=(48, 186, 143), name='Górska łąka'), 82.18272324521742), ((0, 4), (91, 138, 194), Color(rgb=(48, 186, 143), name='Górska łąka'), 82.18272324521742), ((0, 5), (91, 138, 194), Color(rgb=(48, 186, 143), name='Górska łąka'), 82.18272324521742), ((0, 6), (91, 138, 194), Color(rgb=(48, 186, 143), name='Górska łąka'), 82.18272324521742), ((0, 7), (91, 138, 194), Color(rgb=(48, 186, 143), name='Górska łąka'), 82.18272324521742), ((0, 8), (92, 139, 195), Color(rgb=(48, 186, 143), name='Górska łąka'), 82.75868534480233), ((0, 9), (93, 140, 196), Color(rgb=(48, 186, 143), name='Górska łąka'), 83.36666000266533)]

"""

test_matching_2_full = """
Zajmuje bardzo dużo czasu -- nie rób tego :

>>> colors= get_colors()
>>> img= Image.open("IMG_2705.jpg")
>>> revised= list( matching_2(pixel_iter(img), colors))
"""

def performance():
    import timeit

    perf = timeit.timeit(
        """
euclidean( (92, 139, 195), Color(rgb=(239, 222, 205), name='Migdałowy') )
        """,
        setup="""
from typing import NamedTuple, Tuple
class Color(NamedTuple):
    rgb: Tuple[int, ...]
    name: str
import math
def euclidean( pixel, color ):
   return math.sqrt( sum( map( lambda x,y: (x-y)**2, pixel, color.rgb ) ) )
        """
    )
    print("Euklidesowy", perf)

    perf = timeit.timeit(
        """
manhattan( (92, 139, 195), Color(rgb=(239, 222, 205), name='Migdałowy') )
        """,
        setup="""
from typing import NamedTuple, Tuple
class Color(NamedTuple):
    rgb: Tuple[int, ...]
    name: str
def manhattan( pixel, color ):
    return sum( map( lambda x,y: abs(x-y), pixel, color.rgb ) )
        """
    )
    print("Manhattan", perf)

    perf = timeit.timeit(
        """
min(choices, key=lambda xypcd: xypcd[3] )
        """,
        setup="""
from typing import NamedTuple, Tuple
class Color(NamedTuple):
    rgb: Tuple[int, ...]
    name: str
choices= (((0, 0), (92, 139, 195), Color(rgb=(239, 222, 205), name='Migdałowy'), 169.10943202553784), ((0, 0), (92, 139, 195), Color(rgb=(255, 255, 153), name='Kanarkowy'), 204.42357985320578), ((0, 0), (92, 139, 195), Color(rgb=(28, 172, 120), name='Zielony'), 103.97114984456024), ((0, 0), (92, 139, 195), Color(rgb=(48, 186, 143), name='Górska łąka'), 82.75868534480233), ((0, 0), (92, 139, 195), Color(rgb=(255, 73, 108), name='Radykalna czerwień'), 196.19887869200477), ((0, 0), (92, 139, 195), Color(rgb=(253, 94, 83), name='Zachodzące słońce'), 201.2212712413874), ((0, 0), (92, 139, 195), Color(rgb=(255, 174, 66), name='Żółtopomarańczowy'), 210.7961100210343))
        """
    )
    print("min(choices,...)", perf)

def gather_data():
    img = Image.open("IMG_2705.jpg")

    from collections import defaultdict, Counter
    palette = defaultdict(list)
    for xy, rgb in pixel_iter(img):
        palette[rgb].append(xy)

    w, h = img.size
    print("total pixels", w*h)
    print("total colors", len(palette))

    masks = [0b11100000, 0b11110000, 0b11111000, 0b11111100]
    subsets = dict((mask, Counter()) for mask in masks)
    for c in palette:
        for m in masks:
            masked_color = tuple(map(lambda x: x&m, c))
            subsets[m][masked_color] += 1
    for m in masks:
        print(bin(m), len(subsets[m]))

from typing import Dict
def make_color_map(colors: Sequence[Color]) -> Dict[RGB, Color]:
    bit3 = range(0, 256, 0b100000)

    best_iter = (
        min((euclidean(rgb, c), rgb, c) for c in colors)
        for rgb in product(bit3, bit3, bit3)
    )
    color_map = dict((b[1], b[2]) for b in best_iter)
    return color_map

test_make_color_map = """
>>> colors = get_colors()
>>> m = make_color_map(colors)
>>> len(m)
512
>>> m[(0,0,0)]
Color(rgb=(0, 0, 0), name='Czarny')
>>> m[(224,224,224)]
Color(rgb=(219, 215, 210), name='Dębowy')

"""

def clone_picture(color_map: Dict[RGB, Color], filename: str = "IMG_2705.jpg"):
    mask = 0b11100000
    img = Image.open(filename)
    clone = img.copy()
    for xy, rgb in pixel_iter(img):
        r, g, b = rgb
        repl = color_map[(mask&r, mask&g, mask&b)]
        clone.putpixel(xy, repl.rgb)
    clone.show()

def demo():
    start = time.perf_counter()
    color_map = make_color_map(get_colors())
    clone_picture(color_map)
    print(time.perf_counter()-start, "seconds")

__test__ = {
    "test_matching_1": test_matching_1,
    # skip: "test_matching_1_full": test_matching_1_full,
    "test_matching_2": test_matching_2,
    # skip: "test_matching_2_full": test_matching_2_full,
    "test_make_color_map": test_make_color_map,
}

def test():
    import doctest
    doctest.testmod(verbose=1)

if __name__ == "__main__":
    test()
    #gather_data()
    performance()
    #demo()
