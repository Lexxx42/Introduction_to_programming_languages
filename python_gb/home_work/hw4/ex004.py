# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


def main():
    print(
        "This program randomly generates a list of coefficients "
        "(values from 0 to 100) of a polynomial and writes a polynomial of degree k to a file")
    user_input()


if __name__ == '__main__':
    main()
