# Задайте массив из 12 элементов, заполненный случайными числами из промежутка [-9, 9].
# Найдите сумму отрицательных и положительных элементов массива.
# Например, в массиве [3,9,-8,1,0,-7,2,-1,8,-3,-1,6]
# сумма положительных чисел равна 29, сумма отрицательных равна -20.

from array import array
import random


def validation(len):
    if len < 0:
        return -1
    elif len == 0:
        return 0
    else:
        return 1


def generate_array(len):
    arr = array('i', [])
    for i in range(0, len):
        arr.append(random.randint(-9, 10))
    return arr


def find_sum(arr):
    sum_positive = 0
    sum_negative = 0
    for i in range(0, len(arr)):
        if arr[i] > 0:
            sum_positive += arr[i]
        else:
            sum_negative += arr[i]
    return (sum_positive, sum_negative)


def print_array(arr):
    for i in range(0, len(arr)):
        print(arr[i], ' ', end='')
    print()


def result(len):
    if validation(len) == -1:
        print("Length can't be negative!")
    elif validation(len) == 0:
        print("Length is null")
    else:
        arr = generate_array(len)
        print_array(arr)
        sum_found = find_sum(arr)
        print()
        print("sum of positive elements =",
              sum_found[0], "sum of negative elements =", sum_found[1])
        print()


print("This program finds sum of positive elements of array and sum negative ones")
print("please enter length of generated array:")
length = int(input())
result(length)
