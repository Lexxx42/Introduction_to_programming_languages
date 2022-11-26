# def f(x):
#     if x==1:
#         return 'Целое'
#     elif x==2.3:
#         return 23
#     else:
#         return
#
# print(f(1))

def new_string(symbol, count=3):  # 3 - значение по умолчанию
    return symbol * count


print(new_string('!', 5))
print(new_string('!'))
print(new_string(4))


def concatinatio(*params):  # любое число агрументов
    res: str = ''
    for item in params:
        res += item
    return res


print(concatinatio('a', 'b', 'c', 'd', 'e', '1'))  # abcde1
# print(concatinatio(1, 2, 3))  # TypeError: can only concatenate str (not "int") to str



