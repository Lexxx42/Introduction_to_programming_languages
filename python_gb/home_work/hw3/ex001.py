# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_list_elements(input_list):
    sum_elements = 0
    for i in range(0, len(input_list), 2):
        sum_elements += input_list[i]
    return sum_elements


print('This program finds the sum of the elements of a list in an odd position.')
list_1 = [2, 3, 5, 9, 3]
print(f'List for sum of the elements calculation is {list_1}')
print(f'Sum of the elements of the list = {sum_list_elements(list_1)}')
