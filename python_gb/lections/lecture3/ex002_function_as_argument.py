def f(x):
    return x ** 2


g = f  # переменная хранит в себе функцию


def calc1(x):
    return x + 10


def calc2(x):
    return x * 10


def math(op, x):
    print(op(x))


math(calc2, 10)
