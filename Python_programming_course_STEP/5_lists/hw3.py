# Напишите программу, которая принимает на вход список чисел в одной строке
# и выводит на экран в одну строку значения,
# которые встречаются в нём более одного раза.

# Для решения задачи может пригодиться метод sort списка.

# Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.

# Sample Input 1:
# 4 8 0 3 4 2 0 3
# Sample Output 1:
# 0 3 4
# Sample Input 2:
# 10
# Sample Output 2:
# Sample Input 3:
# 1 1 2 2 3 3
# Sample Output 3:
# 1 2 3
# Sample Input 4:
# 1 1 1 1 1 2 2 2
# Sample Output 4:
# 1 2


def count_similar(in_list):
    out_list = []
    temp = None
    for i in range(len(in_list)):
        if i == len(in_list)-1:
            break
        if in_list[i] == in_list[i+1] and in_list[i] != temp:
            out_list.append(in_list[i])
            temp = in_list[i]
    return out_list


input_list = list(int(i) for i in input().split())
input_list.sort()
out_str = map(str, count_similar(input_list))
print(*out_str, sep=' ')
