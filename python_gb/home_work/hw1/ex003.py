# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
# *Пример:*
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def input_values():
    x = int(input('Please enter X coordinate value > '))
    y = int(input('Please enter Y coordinate value > '))
    quarter_of_the_plane(x, y)


def quarter_of_the_plane(x, y):
    if x == 0 and y == 0:
        print('Please enter valid values, X ≠ 0 и Y ≠ 0')
        input_values()
    elif x == 0 and y != 0:
        print('Point on the X axis')
    elif y == 0 and x != 0:
        print('Point on the Y axis')
    elif x > 0 and y > 0:
        print(f'x={x}; y={y} -> 1')
    elif x < 0 and y > 0:
        print(f'x={x}; y={y} -> 2')
    elif x < 0 and y < 0:
        print(f'x={x}; y={y} -> 3')
    elif x > 0 and y < 0:
        print(f'x={x}; y={y} -> 4')


print("This program takes as input the coordinates of a point (X and Y)"
      "and gives the number of a quarter of the plane in which this point is located"
      "(or on which axis it is located).")
input_values()
