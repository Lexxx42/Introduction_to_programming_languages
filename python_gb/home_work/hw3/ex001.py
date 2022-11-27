# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
#
# out
# [10, 2, 3, 8, 9]
# 22
#
# in
# 4
#
# out
# [4, 2, 4, 9]
# 8

def input_data_in_list(length):
    output_list = []
    for i in range(length):
        output_list.append(int(input(f"Enter list's {i + 1} value: ")))
    print(output_list)
    return output_list


def sum_of_elements_in_list(list_for_sum):
    sum_elements = 0
    for i in range(0, len(list_for_sum), 2):
        sum_elements += list_for_sum[i]
    return sum_elements


print('This program finds the sum of the elements of a list in an odd position.')
list_length = int(input('Enter the length of the list: '))
print(f'Sum of the elements in list = {sum_of_elements_in_list(input_data_in_list(list_length))}')
