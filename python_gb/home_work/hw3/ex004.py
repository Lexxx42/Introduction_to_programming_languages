# 4.* Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

import random


def input_values_in_list(length):
    output_list = []
    for i in range(length):
        output_list.append(round(random.uniform(0, 10), 2))
    print(f'Input list is: {output_list}')
    return output_list


def diff_max_min_fraction(list_input):
    fractional_list = []
    for i in range(len(list_input)):
        fractional_list.append(round(list_input[i] % 1, 2))
    min_in_list = min(fractional_list)
    max_in_list = max(fractional_list)
    print(f'Min: {min_in_list}, Max: {max_in_list}, Difference: {round(max_in_list - min_in_list, 2)}')


def main():
    print('This program finds the difference between the maximum and minimum'
          ' values of the fractional part of the elements.')
    length_of_list = int(input('Please enter the number: '))
    diff_max_min_fraction(input_values_in_list(length_of_list))


if __name__ == '__main__':
    main()
