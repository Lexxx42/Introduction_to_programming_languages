# 1. Задайте строку из набора чисел. Напишите программу,
#    которая покажет большее и меньшее число.
#    В качестве символа-разделителя используйте пробел.


def cleaner(string: str):
    list_1 = string.split()
    for i, item in enumerate(list_1):
        list_1[i] = item.strip('!')
        if not list_1[i].replace('-', '').isdigit():
            print('Incorrect data')
            return []
    return list_1


def diff(list_for_diff: list):
    if list_for_diff:
        min_value = min(list_for_diff, key=int)
        max_value = max(list_for_diff, key=int)
        return min_value, max_value
    return 0, 0


user_input = input()
input_list = cleaner(user_input)
min_val, max_val = diff(input_list)
print(f'Min value = {min_val}, max malue = {max_val}')
