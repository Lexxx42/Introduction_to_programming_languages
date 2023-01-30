# Напишите программу, которая задаёт массив из some элементов и выводит их на экран.

from array import array
import random


def generate_length():
    length = random.randint(8, 12)
    return length


def generate_array(length):
    arr = array('i', [])
    for i in range(length):
        arr.append(random.randint(-99, 100))
    return arr


def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], ' ', end='')


print("This programm generates array and show it to the user")
print()
length = generate_length()
print("Generated array: ", end='')
print_array(generate_array(length))
