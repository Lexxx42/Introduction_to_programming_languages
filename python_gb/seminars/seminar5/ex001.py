# 1. Создайте список из N натуральных чисел(0 до N),
#    упорядоченных по возрастанию. Среди чисел не хватает
#    одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
#    Найдите это число.

from random import choice

n = abs(int(input()))


def create_list(max: int):
    i_list = list(range(max + 1))
    i_list.remove(choice(i_list))
    return i_list


def rew(my_list: list):
    print(my_list)
    for i in range(1, len(my_list)):
        if my_list[i] - 1 != my_list[i - 1]:
            return my_list[i] - 1
    return -1


print(rew(create_list(n)))
