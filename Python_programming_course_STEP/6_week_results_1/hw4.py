# Напишите программу, на вход которой подаётся прямоугольная матрица
# в виде последовательности строк.
# После последней строки матрицы идёт строка,
# содержащая только строку "end" (без кавычек, см. Sample Input).

# Программа должна вывести матрицу того же размера,
# у которой каждый элемент в позиции i, j равен сумме элементов
# первой матрицы на позициях (i-1, j), (i+1, j), (i, j-1), (i, j+1).
# У крайних символов соседний элемент находится с противоположной стороны матрицы.

# В случае одной строки/столбца элемент сам себе является
# соседом по соответствующему направлению.

# Sample Input 1:

# 9 5 3
# 0 7 -1
# -5 2 9
# end
# Sample Output 1:

# 3 21 22
# 10 6 19
# 20 16 -1
# Sample Input 2:

# 1
# end
# Sample Output 2:

# 4


def adding_to_list(list_for_input):
    user_input = input()
    if user_input == 'end':
        return list_for_input
    else:
        sub_list = list(int(i) for i in user_input.split())
        list_for_input.append(sub_list[:])
    adding_to_list(list_for_input)


def plot(sub_list):
    for i in range(len(a)):
        sub_sub_list = []
        for j in range(len(a[0])):
            if j == len(a[0]) - 1:
                if i == len(a) - 1:
                    sub_sub_list.append(a[i - 1][j] + a[0][j] + a[i][j - 1] + a[i][0])
                else:
                    sub_sub_list.append(a[i - 1][j] + a[i + 1][j] + a[i][j - 1] + a[i][0])
            else:
                if i == len(a) - 1:
                    sub_sub_list.append(a[i - 1][j] + a[0][j] + a[i][j - 1] + a[i][j + 1])
                else:
                    sub_sub_list.append(a[i - 1][j] + a[i + 1][j] + a[i][j - 1] + a[i][j + 1])
        sub_list.append(sub_sub_list)
    return sub_list


def print_output(list_for_output):
    for n in range(len(list_for_output)):
        for m in range(len(list_for_output[0])):
            print(list_for_output[n][m], end=' ')
        if len(list_for_output) > 1:
            print()


a = []
adding_to_list(a)
sub_list = []
output_list = plot(sub_list)
print_output(output_list)
