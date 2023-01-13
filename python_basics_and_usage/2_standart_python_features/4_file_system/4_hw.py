# Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.
#
# Пример входного файла:
# ab
# c
# dde
# ff
#
# Пример выходного файла:
# ff
# dde
# c
# ab

with open("dataset_24465_4.txt") as start, open("output.txt", "w") as output:
    a = [i.strip() for i in start.readlines()][::-1]
    for item in a:
        output.write(item + '\n')


# lines = open("input.txt").readlines()
# with open("output.txt", "w") as out:
#     out.writelines(reversed(lines))
