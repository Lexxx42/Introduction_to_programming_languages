# Различные функции
# Без возвращаемого значения: либо не содержат return, либо с ним но без значения после него
# Без параметров: def name_func():
# Произвольное число параметров: print() - можем передать сколько угодно параметров
# Параметры со значениями по умолчанию:


# Произвольное число параметров

def min_2(*a):  # Специальный способ указать, что принимается произвольное число аргументов
    m = a[0]
    for x in a:
        if m > x:
            m = x
    return m


print(min_2(2, 4, 6))

# Значения параметров по умолчанию


def my_range(start, stop, step=1):
    res = []
    if step > 0:
        x = start
        while x < stop:
            res += [x]
            x += step
    elif step < 0:
        x = start
        while x > stop:
            res += [x]
            x += step
    return res


print(my_range(2, 15, 3))

# Явное указание аргументов

print(my_range(stop=21, start=3))
