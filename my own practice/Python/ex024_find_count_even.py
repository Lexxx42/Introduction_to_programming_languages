# Задача 1: Задайте массив заполненный случайными положительными трёхзначными числами. Напишите программу, которая покажет количество чётных чисел в массиве.

from array import array
import random


def validation(length):
    if length < 0:
        return -1
    elif length == 0:
        return 0
    return 1


def generate_array(length):
    arr = array('i', [])
    for i in range(0, length):
        arr.append(random.randint(0, 10))
    return arr


def search_for_even(arr):
    count = 0
    for i in range(0, len(arr)):
        if arr[i] % 2 == 0:
            count = count+1
    return count

def print_array(arr):
    for i in range(0, len(arr)):
        print(arr[i],' ',end='')



print("This program generates array of 3-digit numbers and seaches for returns quantity of even numbers in array")
print("Please enter array length: ")
length = int(input())
if validation(length) == 1:
    arr = generate_array(length)
    print_array(arr)
    print()
    print("quantity of even numbers in array is", search_for_even(arr))

elif validation(length) == -1:
    print("length can't be negative")
else:
    print("length of array is 0")
