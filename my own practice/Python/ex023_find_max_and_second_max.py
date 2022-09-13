# Напишите программу, которая задаёт массив из 8 элементов случайными числами и выводит их на экран.
# Также ищет второй максимум (число меньше максимального элемента, но больше всех остальных)

from array import array
import random
MIN = -10
MAX = 10

def generate_array(length):
    arr = array('i', [])
    for i in range(0, length):
        arr.append(random.randint(MIN, MAX))
    return arr


def print_array(arr):
    for i in range(0, len(arr)):
        print(arr[i], ' ', end='')


def search_for_maxes(arr):
    max1 = MIN-1
    max2 = MIN-1
    for i in range(0, len(arr)):
        if arr[i]>max1:
            max2 = max1
            max1=arr[i]
        if arr[i]>max2 and arr[i]!=max1:
            max2 = arr[i]
    answer = array('i',[max1, max2])
    return answer



print("this program searches for max and second max in the array")
print("enter array's length: ")
length = int(input())
arr = generate_array(length)
print_array(arr)
answer = search_for_maxes(arr)
print(answer)