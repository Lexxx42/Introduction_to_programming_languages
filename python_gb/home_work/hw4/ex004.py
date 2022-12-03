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


def generate_polynome(degree: int):
    degree_temp = degree
    start = 1
    for _ in range(3):
        polynome_list = []
        degree = degree_temp
        k = randint(0, 100)
        length_of_polynome = randint(0, degree)
        first_poly = 1
        while degree >= 0 and length_of_polynome >= 0:
            if degree == 1:
                polynome_list.append(str(k) + '*' + 'x' + '+' + str(randint(0, 100)))
                length_of_polynome -= 1
            elif degree == 0:
                polynome_list.append(str(randint(0, 100)))
                length_of_polynome -= 1
            else:
                polynome_list.append(
                    str(k) + '*' + 'x' + '^' + generate_power(degree, first_poly, length_of_polynome) + '+' + str(
                        randint(0, 100)))
                first_poly = 0
                length_of_polynome -= 1
            degree -= 1
        file_write(polynome_list, start)
        start = 0
        print(polynome_list)


def generate_power(degree: int, first_poly: int, length_of_polynome: int):
    if first_poly == 1:
        power = str(degree)
    else:
        power = str(randint(length_of_polynome, degree))
    return power


def choose_symbol():
    symbol_rand = randint(0, 1)
    if symbol_rand == 1:
        symbol = ' - '
    else:
        symbol = ' + '
    return symbol


def file_write(export_list: list, start: int):
    export_string = ''
    for i, item in enumerate(export_list):
        if i == len(export_list) - 1:
            export_string = export_string + item
        else:
            export_string = export_string + item + choose_symbol()
    if start == 1:
        with open('ex004.txt', 'w', encoding='utf-8') as data:
            data.write(export_string + '\n')
    else:
        with open('ex004.txt', 'a', encoding='utf-8') as data:
            data.write(export_string + '\n')


def main():
    print(
        "This program randomly generates a list of coefficients "
        "(values from 0 to 100) of a polynomial and writes a polynomial of degree k to a file")
    user_input()


if __name__ == '__main__':
    main()
