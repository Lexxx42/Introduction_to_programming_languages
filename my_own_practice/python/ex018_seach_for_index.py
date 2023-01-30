# search for number's index in array

from array import array
from dataclasses import asdict
import random


print("please enter number for search from 0 to 9")
number = int(input())


def generate_array():
    arr = array('i', [])
    for i in range(0, random.randint(7, 10)):
        arr.append(random.randint(0, 9))
    return arr


def search_for_number(arr, number):
    for i in range(0, len(arr)):
        if arr[i] == number:
            return i
    return -1


def validation(number):
    if number < 0 or number > 9:
        return False
    else:
        return True


if validation(number) == True:
    arr = generate_array()
    print(arr)
    index = search_for_number(arr, number)
    if (index == -1):
        print("number isn't found")
    else:
        print("number", number, "is found on index =", index)
else:
    print("number is invalid!")
