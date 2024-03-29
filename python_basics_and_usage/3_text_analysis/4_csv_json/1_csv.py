# Существуют разные форматы текстовых данных.

# Мы поговорим о CSV (comma separated values).

# В общем случае csv файл выглядит просто, у нас есть значения разделенные запятой.
# example.csv
# Первая строка - это шапка нашей таблицы.

# Данный формат идеально подходит, для того чтобы хранить табличные данные.
# Потому что он не хранит ничего лишнего.

# В языке python есть встроенная библиотека csv.

import csv

# with open("example.csv") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# Первый резонный вопрос, который можно задать: а зачем нам для этого отдельная библиотека?
# Можем считать наш файл построчно, разбить каждую строку оп запятой и получить
# те же самые листы, которые мы получили от библиотеки.

# Ответ.
# Мы не всегда это можем сделать, потому что существую еще дополнительные правила.

# Например, мы можем захотеть использовать запятую не только в качестве разделителя в нашей таблице.
# Например, мы заходи отделить целую часть от дробной у числа.

# Поменяем запятую у дробной части (90.2 на 90,2).
# Появится 1 лишнее значение в нашем ряде, чего мы не хотели.

# Однако, используя csv формат, вы можете изолировать любое значение в не зависимости от того,
# какие символы в нем используются.

# Для этого используются двойные кавычки.

# Если описывать таблицу построчно, т.е. мы говорим, что в строке через запятую у нас будут следовать
# элементы данной строки.
# А что если мы хотим, чтобы элементом строки был символ переноса строки?

# Таким образом в библиотеки csv учтены все эти мелочи, которые легко забыть.
# Но что самое замечательное в данной библиотеке, так это то, что мы сами
# можем явно указать знак разделителя или допустим какой символ использовать вместо кавычки.

with open("example.csv") as f:
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        print(row)

# Данный модуль позволяет данные не только считывать, но и позволяет записывать.

students = [
    ["Greg", "Dean", 70, 80, 90, "Good job, Greg"],
    ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
]

with open("writer.csv", "a") as f:
    writer = csv.writer(f, lineterminator='\n')
    # for student in students:
    #     writer.writerow(student)
    writer.writerows(students)

# Также мы можем уточнять некоторое поведение, которое нам требуется при записи.
# Например, сказать writer-у поместить в кавычки все значения, которые мы записываем.

with open("writer.csv", "a") as f:
    writer = csv.writer(f, lineterminator='\n', quoting=csv.QUOTE_ALL)
    writer.writerows(students)

# CSV - это очень простой текстовый формат для табличных данных.
# Однако даже внутри такого формата зарегламентированны маленькие правила,
# про которые можно легко забыть.
# Чтобы такого не допустить лучше использовать библиотеку.
