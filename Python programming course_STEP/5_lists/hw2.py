# Напишите программу, на вход которой подаётся список чисел одной строкой.
# Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
# Для элементов списка, являющихся крайними, одним из соседей считается элемент,
# находящий на противоположном конце этого списка.
# Например, если на вход подаётся список "1 3 5 6 10",
# то на выход ожидается список "13 6 9 15 7" (без кавычек).

# Если на вход пришло только одно число, надо вывести его же.

# Вывод должен содержать одну строку с числами нового списка, разделёнными пробелом.

# Sample Input 1:

# 1 3 5 6 10
# Sample Output 1:

# 13 6 9 15 7
# Sample Input 2:

# 10
# Sample Output 2:

# 10

def sum_neighbor(in_list):
    out_list = []
    if len(in_list) == 1:
        out_list.append(in_list[0])
        return out_list
    else:
        for i in range(len(in_list)):
            if i < len(in_list)-1:
                out_list.append(in_list[i+1]+in_list[i-1])
            else:
                out_list.append(in_list[i-1]+in_list[0])
        return out_list


input_list = list(int(i) for i in input().split())
a=sum_neighbor(input_list)
str_a = map(str, a)
print(*str_a, sep=' ')

