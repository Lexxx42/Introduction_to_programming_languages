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
    output_str = ''
    while (number // 2) >= 1:
        output_str += ''.join(str(number % 2))
        number = number // 2
    if number == 1:
        output_str += ''.join(str(number % 2))
    return output_str[::-1]


def main():
    print('This program converts decimal number to binary.')
    int_number_input = int(input('Please enter the number: '))
    if int_number_input < 0:
        print("Program don't work with negative numbers")
        exit()
    converted_number = convert_to_binary(int_number_input)
    print(converted_number)


if __name__ == '__main__':
    main()
