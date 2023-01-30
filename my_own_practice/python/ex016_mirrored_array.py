
from array import array
import random


def array_fill():
    arr = array('i', [])
    for i in range(0, random.randint(5, 10)):
        arr.append(random.randint(0, 9))
    return arr


def array_print(arr):
    for i in range(0, len(arr)):
        print(arr[i], ' ', end='')


def mirror_array(arr):
    for i in range(0, len(arr)//2):
        temp = arr[i]
        arr[i] = arr[len(arr)-(i+1)]
        arr[len(arr)-(i+1)] = temp
    return arr


arr = array_fill()
print("Array filled: ", end='')
array_print(arr)
print()
print("Array mirrored: ", end='')
array_print(mirror_array(arr))
