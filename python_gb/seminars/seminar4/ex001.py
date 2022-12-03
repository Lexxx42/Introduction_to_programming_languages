# Из дз перемешивание листа

from random import randrange

num = int(input())
nums_list = list(range(num))
res_list = []

print(nums_list)

for i in range(num):
    n_1, n_2 = randrange(num), randrange(num)
    nums_list[n_1], nums_list[n_2] = nums_list[n_2], nums_list[n_1]

print(nums_list)
