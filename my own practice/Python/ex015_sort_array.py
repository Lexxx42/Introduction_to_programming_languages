from array import array
import random

print("This program sorts array from min to max and vice versa")
print()


def random_array():
    arr = array('i', [])
    for i in range(0, random.randint(5, 10)):
        arr.append(random.randint(0, 9))
    return arr


def print_array(arr):
    for i in range(0, len(arr)):
        print(arr[i], ' ', end='')
    print()

def sort_array_from_max_to_min(arr):
    for i in range(0, len(arr)-1):
        max_position = i
        for j in range(i+1, len(arr)):
            if arr[j] > arr[max_position]:
                max_position = j
        temp = arr[i]
        arr[i] = arr[max_position]
        arr[max_position] = temp
    return arr

def sort_array_from_min_to_max(arr):
    for i in range(0, len(arr)-1):
        min_position = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_position]:
                min_position = j
        temp = arr[i]
        arr[i] = arr[min_position]
        arr[min_position] = temp
    return arr

generated_array = random_array()
print("Generated array:",' ', end='')
print_array(generated_array)
print()
print("Sorted from max to min:",' ',end='')
print_array(sort_array_from_max_to_min(generated_array))
print()
print("Sorted from min to max:",' ',end='')
print_array(sort_array_from_min_to_max(generated_array))
