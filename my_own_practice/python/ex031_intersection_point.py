# Задача 2: Напишите программу, которая найдёт точку пересечения двух прямых,
# заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; значения b1, k1, b2 и k2 задаются пользователем.
# b1 = 2, k1 = 5, b2 = 4, k2 = 9 -> (-0,5; -0,5)

def input_user():
    print("Please enter k1 value:")
    k1 = int(input())
    print("Please enter b1 value:")
    b1 = int(input())
    print("Please enter k2 value:")
    k2 = int(input())
    print("Please enter b2 value:")
    b2 = int(input())
    return k1, b1, k2, b2


def determine_points(input):
    x_coordinate = (input[1] - input[3]) / (input[2] - input[0])
    y_coordinate = (input[2] * input[1] - input[0] * input[3]) / (input[2] - input[0])
    return (x_coordinate, y_coordinate)


def intersection_point(input):
    print(input)
    if input[0] == input[2] and input[1] == input[3]:
        print("Lines match!")
    elif input[0] == input[2]:
        print("Parallel lines!")
    else:
        print(determine_points(input))


print("This program finds the point of intersection of two", end='')
print(" lines given by the equations y = k1 * x + b1, y = k2 * x + b2; b1, k1, b2 and k2. Values are user defined.")
intersection_point(input_user())
