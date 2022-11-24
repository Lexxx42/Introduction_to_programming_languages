# Объявления функции
def min2(a, b):
    if a <= b:
        return a
    else:
        return b


# Функция должна быть объявлена ранее первого вызова
print(min2(5, 1))
print(min2(min2(57, 6), 34))
