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


user_input_list = []
adding_to_list(user_input_list)
print(user_input_list)  # list with values [[1, 2, 3], [1, 2, 3]]

n = len(user_input_list)
sub_list = [[0]*len(user_input_list[0])]*n
print(sub_list)  # [[0, 0, 0], [0, 0, 0]]

numbers_list = [] 
for c in user_input_list:
    for k in c:
        numbers_list.append(k)
print(numbers_list)  # [1, 2, 3, 1, 2, 3]

# for i in range(len(sub_list)):
#     for j in range(len(sub_list[0])):
#         #sub_list[i][j] = 
#         if j==len(sub_list[0]):

# print(sub_list)

print(user_input_list[-1][-1]) # 6
