import operator as op
from functools import partial

x = [
    ("Guido", 1),
    ("Heskel", 12),
    ("John", 34)
]


def sorting(name):
    return name[1]


x.sort(key=lambda x: x[1], reverse=True)
print(x)

print()
x.sort(key=op.itemgetter(-1), reverse=True)
print(x)

print()
sort_by_last = partial(list.sort, key=op.itemgetter(-1), reverse=True)
sort_by_last(x)
print(x)
