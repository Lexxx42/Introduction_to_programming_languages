# Вам дана частичная выборка из датасета зафиксированных преступлений,
# совершенных в городе Чикаго с 2001 года по настоящее время.

# Одним из атрибутов преступления является его тип – Primary Type.

# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.

# Файл с данными:
# Crimes.csv

import csv

crimes = {}
with open("Crimes.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        if row[5] in crimes:
            crimes[row[5]] += 1
        else:
            crimes[row[5]] = 1
print(crimes)
sorted_tuples = sorted(crimes.items(), key=lambda item: item[1], reverse=True)
sorted_dict = {k: v for k, v in sorted_tuples}
print(sorted_dict)
