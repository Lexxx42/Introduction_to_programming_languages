# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27


def calc_sum_digits(input_list):
    sum_after_dot = 0
    while input_list[1] > 9:
        sum_after_dot += input_list[1] % 10
        input_list[1] = input_list[1] // 10
    sum_after_dot += input_list[1]
    return abs(input_list[0]) + sum_after_dot


input_number = [int(i) for i in input().split('.')]
result = calc_sum_digits(input_number)
print(result)
