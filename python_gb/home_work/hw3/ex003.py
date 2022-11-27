# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
#
# in
# 11
# out
# 1011
#

def convert_to_binary(number):
    output_list = []
    while (number // 2) > 1:
        output_list.append(number % 2)
        number = number // 2
    return output_list[::-1]


print('This program converts decimal number to binary.')
int_number_input = int(input('Please enter the number: '))
converted_number = convert_to_binary(int_number_input)
print(converted_number)
