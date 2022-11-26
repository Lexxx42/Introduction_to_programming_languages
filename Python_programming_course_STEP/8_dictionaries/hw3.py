# Напишите программу, которая считывает строку с числом n, которое задаёт количество чисел, которые нужно считать.
# Далее считывает n строк с числами xi, по одному числу в каждой строке.
# Итого будет n+1 строк.
# При считывании числа xi программа должна на отдельной строке вывести значение f(xi)
# Функция f(x) уже реализована и доступна для вызова.
#
# Функция вычисляется достаточно долго и зависит только от переданного аргумента x.
# Для того, чтобы уложиться в ограничение по времени, нужно избежать повторного вычисления значений.
#
# Sample Input:
#
# 5
# 5
# 12
# 9
# 20
# 12
# Sample Output:
#
# 11
# 41
# 47
# 61
# 41

n = int(input())
d = []
for i in range(n):
    d.append(int(input()))
print('input', d)


def strp_2(list_input):
    for i in range(len(list_input) - 1, 0, -1):
        if list_input[i] == list_input[i - 1]:
            list_input.remove(list_input[i])
        return list_input


def strp_1(list_1):
    if len(list_1) == 2:
        strp_2(list_1)
    for i in range(len(list_1) - 1, 1, -1):
        if i == 0:
            return list_1
        else:
            if list_1[i] == list_1[i - 1]:
                list_1.remove(list_1[i])
                if len(list_1) == 2:
                    strp_2(list_1)
        return list_1
    return list_1


d = strp_1(d)
print('output', d)
