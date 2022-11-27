# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
#
# out
# [2, 5, 8, 10]
# [20, 40]
#
# in
# 5
#
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from ex001 import input_data_in_list


def mult_pairs_in_list(input_list):
    output_list = []
    for i, item in enumerate(input_list):
        if i < len(input_list) // 2:
            output_list.append(input_list[i] * input_list[-(i + 1)])
        else:
            if len(input_list) % 2 != 0:
                output_list.append(input_list[i])
                return output_list
            return output_list


def main():
    print('This program finds the product of pairs of numbers in a list. '
          'A pair is the first and last element, the second and penultimate, and so on.')
    list_length = int(input('Enter the length of the list: '))
    s = input_data_in_list(list_length)
    print(mult_pairs_in_list(s))


if __name__ == '__main__':
    main()
