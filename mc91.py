'''
https://en.wikipedia.org/wiki/McCarthy_91_function
'''


def mc91(n: int) -> int:
    """McCarthy 91 function."""
    if n > 100:
        return n - 10
    else:
        return mc91(mc91(n + 11))
      
x = mc91(91)
print(x)
