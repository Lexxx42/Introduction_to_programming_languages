def sum(x):
    return x + 10


def mult(x):
    return x ** 2


sum(mult(2))


def sum1(x):
    return x + 22


def mult2(x):
    return x ** 3


sum1(mult2(2))


def sum3(x):
    return x + 242


def mult4(x):
    return x ** 5


sum3(mult2(2))


def f(x):
    return x ** 2


g = f

print(type(f))
print(f(1))
print(g(1))
