def select(f, data):
    return [f(x) for x in data]


def where(f, data):
    return [x for x in data if f(x)]


data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data)
res = where(lambda x: not x % 2, res)
res = select(lambda x: (x, x ** 2), res)
print(res)
