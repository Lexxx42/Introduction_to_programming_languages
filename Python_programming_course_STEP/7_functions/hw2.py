# Напишите функцию modify_list(l), которая принимает на вход список целых чисел,
# удаляет из него все нечётные значения, а чётные нацело делит на два.
# Функция не должна ничего возвращать, требуется только изменение переданного списка, например:
#
# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]
#
# lst = [10, 1, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]
# Функция не должна осуществлять ввод/вывод информации.

def modify_list(l):
    for j in range(len(l)-1, 1, -1):
        if l[j] % 2 != 0:
            l.remove(l[j])
    for i, item in enumerate(l):
        if item % 2 == 0:
            temp = item
            l.remove(item)
            l.insert(i, temp // 2)


# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]

lst = [10, 5, 8, 3]
modify_list(lst)
print(lst)  # [5, 4]
