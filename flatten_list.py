lst = [1, 8, 9, [5, 6, 7, ['10', '11', [88, 99, 100]]], 13, 14, 'q', 'w', ['e', 'r', 't', ['y1', 'y2']], 'y']

def flatten(lst):
    for i in lst:
        if isinstance(i, list):
            for j in flatten(i):
                yield j
        else:
            yield i

print(list(flatten(lst)))