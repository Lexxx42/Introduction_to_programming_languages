# Напишите программу, которая считывает со стандартного ввода целые числа,
# по одному числу в строке,
# и после первого введенного нуля выводит сумму полученных на вход чисел.

number = int(input())
sum_number = 0
while (number != 0):
    sum_number += number
    number = int(input())
print(sum_number)
