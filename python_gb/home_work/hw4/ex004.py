# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint


def user_input():
    input_number = int(input('Please enter a natural degree k: '))
    if input_number > 0:
        generate_polynome(input_number)
    else:
        print('Value must be natural')
        user_input()


def generate_polynome(degree):
    polynome_list = []
    k = randint(0, 100)
    length_of_polynome = randint(0, degree)
    while degree >= 0 and length_of_polynome >= 0:
        power = str(degree)
        if degree == 1:
            polynome_list.append(str(k) + '*' + 'x' + '+' + str(randint(0, 100)))
            length_of_polynome -= 1
        elif degree == 0:
            polynome_list.append(str(randint(0, 100)))
            length_of_polynome -= 1
        else:
            polynome_list.append(str(k) + '*' + 'x' + '^' + power + '+' + str(randint(0, 100)))
            length_of_polynome -= 1
        degree -= 1
    file_write(polynome_list)
    print(polynome_list)


def choose_symbol():
    symbol_rand = randint(0, 1)
    if symbol_rand == 1:
        symbol = ' - '
    else:
        symbol = ' + '
    return symbol


def file_write(export_list):
    export_string = ''
    for i, item in enumerate(export_list):
        if i == len(export_list) - 1:
            export_string = export_string + item
        else:
            export_string = export_string + item + choose_symbol()

    with open('ex004.txt', 'w') as data:
        data.writelines(export_string)


def main():
    print(
        "This program randomly generates a list of coefficients "
        "(values from 0 to 100) of a polynomial and writes a polynomial of degree k to a file")
    user_input()


if __name__ == '__main__':
    main()
