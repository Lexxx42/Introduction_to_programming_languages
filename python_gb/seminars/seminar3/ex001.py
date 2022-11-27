# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.
from random import sample


# def find_in_list(value, len):
#     list_1 = sample(range(1, len * 2), k=len)
#     print(list_1)
#     return print(value in list_1)

def find_in_list(value, len):
    list_1 = sample(range(1, len * 2), k=len)
    print(list_1)
    return 'Yes' if value in list_1 else 'No'


length = int(input('length of the list: '))
number = int(input('enter the number: '))
print(find_in_list(number, length))
