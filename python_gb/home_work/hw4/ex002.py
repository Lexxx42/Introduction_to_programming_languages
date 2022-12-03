# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


print('This program lists the prime factors of N.')
input_number = int(input('Please enter a naturel number N: '))

list_out = [x for x in range(2, input_number) if not input_number % x and not x %]
print(list_out)
