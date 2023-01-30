# Задача 2
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 3D пространстве.
# A (3,6,8); B (2,1,-7), -> 15.84
# A (7,-5, 0); B (1,-1,9) -> 11.53

from array import array
from cmath import sqrt


print("This program takes as input the coordinates of two points and finds the distance between them in 3D space")
print()
print("Please, enter coordinates for 2 dots in 3D dimension")
print()


def input_coordinates():
    number_of_coordinates = 3
    x_y_z_coords = []
    for i in range(number_of_coordinates):
        if i == 0:
            print("please enter X coordinate")
            x_y_z_coords.append(int(input()))
        if i == 1:
            print("please enter Y coordinate")
            x_y_z_coords.append(int(input()))
        if i == 2:
            print("please enter Z coordinate")
            x_y_z_coords.append(int(input()))
    return x_y_z_coords


def distance(coords_fp, coors_sp):
    result = ((coords_fp[0]-coors_sp[0])**2 + (coords_fp[1] -
              coors_sp[1])**2 + (coords_fp[2]-coors_sp[2])**2)**0.5
    return result


print("Enter coordinates for 1st point")
first_point = input_coordinates()
print()
print("Enter coordinates for 2nd point")
second_point = input_coordinates()
print()

print("first point:", first_point[0], first_point[1], first_point[2])
print()
print("second point:", second_point[0], second_point[1], second_point[2])
print()
print("Distanst between points is", '%.3f' %
      distance(first_point, second_point))
