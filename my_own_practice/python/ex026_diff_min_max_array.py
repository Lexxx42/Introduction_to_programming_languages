# Задача 3: Задайте массив вещественных чисел. Найдите разницу между максимальным и минимальным элементов массива.


from array import array
import random


def validation(length):
    if length < 0:
        return -1
    elif length == 0:
        return 0
    else:
        return 1


def generate_array(length):
    arr = array('i', [])
    for i in range(length):
        arr.append(random.randint(-9, 10))
    return arr


def print_array(arr):
    for i in range(0, len(arr)):
        print(arr[i], ' ', end='')
    print()


def find_max(array):
    max = array[0]
    for i in range(0, len(array)):
        if array[i] > max:
            max = array[i]
    return max


def find_min(array):
    min = array[0]
    for i in range(0, len(array)):
        if array[i] < min:
            min = array[i]
    return min


def diff_max_min(array):
    dif = find_max(array)-find_min(array)
    return dif


def result():
    if validation(length) == -1:
        print("Length can't be negative!")
    elif validation(length) == 0:
        print("length is 0!")
    else:
        array = generate_array(length)
        print_array(array)
        print("MAX - MIN =", diff_max_min(array))


print("this program generates array, searches for MIN and MAX elements and returns MAX-MIN")
print("please enter array's length:")
length = int(input())
result()
