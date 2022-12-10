# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
#
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
#
# in
# 10
#
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import randint

n = int(input(''))
generated_list = [randint(0, 100) for _ in range(n)]
answer_list = [generated_list[i] for i in range(1, len(generated_list)) if
               generated_list[i] > generated_list[i - 1]]
print(generated_list)
print(answer_list)
