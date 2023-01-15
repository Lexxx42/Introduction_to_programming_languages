import operator as op

x = [
    ("Guido", 1),
    ("Heskel", 12),
    ("John", 34)
]


def sorting(name):
    return name[1]


# name_lengths = [sorting(name) for name in x]
# print(name_lengths)

x.sort(key=lambda x: x[1], reverse=True)
print(x)

print()
x.sort(key=op.itemgetter(-1), reverse=True)
print(x)
