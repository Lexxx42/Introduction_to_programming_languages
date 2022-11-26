# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
import random


def mix(list_1):
    for i in range(len(list_1)):
        random_index = random.randrange(len(list_1))
        temp_1 = random_index
        random_index = random.randrange(len(list_1))
        temp_2 = random_index
        temp_1_value = list_1[temp_1]
        temp_2_value = list_1[temp_2]
        list_1.pop(temp_1)
        list_1.insert(temp_1, temp_2_value)
        list_1.pop(temp_2)
        list_1.insert(temp_2, temp_1_value)
    return list_1


input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(input_list)
list_output = mix(input_list)
print(list_output)
