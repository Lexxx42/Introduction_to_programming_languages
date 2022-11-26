# 2. Создать список, длины n, значения формируются по формуле 3k + 1,
#    где k принимает значения от 1 до n включительно.

list_1 = []

length = int(input())

for k in range(1, length + 1):
    list_1.append(3 * k + 1)
print(list_1)
