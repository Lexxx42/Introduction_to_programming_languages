# Задайте одномерный массив, заполненный случайными числами. Найдите сумму элементов, стоящих на нечётных позициях.


from array import array
import random


def validation(len):
    if len < 0:
        return -1
    elif len == 0:
        return 0
    return 1


def generate_array(length):
    arr = array('i', [])
    for i in range(0, length):
        arr.append(random.randint(-9, 10))
    return arr


def print_array(arr):
    for i in range(0, len(arr)):
        print(arr[i], ' ', end='')
    print()


def odd_sum_array(arr):
    sum = 0
    i = 1
    while i < len(arr):
        sum = sum + arr[i]
        i += 2
    return sum


print("This profran generates an array and returns sum of odd elements of that array")
print("please enter array length:")
length = int(input())
if validation(length) == -1:
    print("length can't have negative value!")
if validation(length) == 0:
    print("length iis 0!")
if validation(length) == 1:
    arr = generate_array(length)
    print_array(arr)
    print("sum of add elements in array =", odd_sum_array(arr))

else:
    print("CAN'T BE!")
