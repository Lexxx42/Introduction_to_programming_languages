# Жители страны Малевии часто экспериментируют с планировкой комнат. 
# Комнаты бывают треугольные, прямоугольные и круглые. 
# Чтобы быстро вычислять жилплощадь, требуется написать программу, 
# на вход которой подаётся тип фигуры комнаты и соответствующие параметры, 
# которая бы выводила площадь получившейся комнаты.

# Для числа π в стране Малевии используют значение 3.14.

# Формат ввода, который используют Малевийцы:

# треугольник
# a
# b
# c
# где a, b и c — длины сторон треугольника

# прямоугольник
# a
# b
# где a и b — длины сторон прямоугольника

# круг
# r
# где r — радиус окружности

def input_values(figure):
    if figure == 'треугольник':
        a = float(input())
        b = float(input())
        c = float(input())
        return a, b, c
    elif figure == 'прямоугольник':
        a = float(input())
        b = float(input())
        return a, b
    elif figure == 'круг':
        return float(input())


def calculate(figure):
    if figure == 'треугольник':
        figure_values = input_values(figure)
        p = (figure_values[0]+figure_values[1]+figure_values[2])/2
        return (p*(p-figure_values[0])*(p-figure_values[1])
                * (p-figure_values[2]))**0.5
    elif figure == 'прямоугольник':
        figure_values = input_values(figure)
        return figure_values[0]*figure_values[1]
    elif figure == 'круг':
        figure_values = input_values(figure)
        pi = 3.14
        return pi*figure_values**2


figure_type = input()
print(calculate(figure_type))