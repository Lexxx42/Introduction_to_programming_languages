# def sum1(x, y):
#     return x + y


# f = sum1  # создание псевдонима функции
sum1 = lambda x, y: x + y


def mult(x, y):
    return x * y


def calc(op, a, b):
    print(op(a, b))
    return op(a, b)


calc(sum1, 12, 1)  # 13
# calc(f, 12, 1)  # 13
print()
calc(lambda x, y: x + y, 12, 1)  # 13
