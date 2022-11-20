# 5. Напишите программу,
# которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1
#
# out
# 5.099


def input_coordinates():
    print("Please enter coordinates for 1st point")
    x1 = int(input('Please enter coordinate X > '))
    y1 = int(input('Please enter coordinate Y > '))
    print("Please enter coordinates for 2nd point")
    x2 = int(input('Please enter coordinate X > '))
    y2 = int(input('Please enter coordinate Y > '))
    return [x1, y1, x2, y2]


def calculate_distance(list_results):
    distance = round(((list_results[2] - list_results[0]) ** 2 + (list_results[3] - list_results[1]) ** 2) ** 0.5, 5)
    print(f'Distance between points is {distance}')


print('This program takes as input the coordinates of two points and finds the distance between them in 2D space.')
user_input = input_coordinates()
calculate_distance(user_input)
