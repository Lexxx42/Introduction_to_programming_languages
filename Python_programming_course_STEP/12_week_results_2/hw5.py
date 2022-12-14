# Дан файл с таблицей в формате TSV с информацией о росте школьников разных классов.

# Напишите программу, которая прочитает этот файл и подсчитает для каждого класса средний рост учащегося.

# Файл состоит из набора строк, каждая из которых представляет собой три поля:
# Класс Фамилия Рост

# Класс обозначается только числом. Буквенные модификаторы не используются.
# Номер класса может быть от 1 до 11 включительно.
# В фамилии нет пробелов, а в качестве роста используется натуральное число,
# но при подсчёте среднего требуется вычислить значение в виде вещественного числа.

# Выводить информацию о среднем росте следует в порядке возрастания номера класса
# (для классов с первого по одиннадцатый). Если про какой-то класс нет информации, необходимо вывести напротив него прочерк.

# В качестве ответа прикрепите файл с полученными данными о среднем росте.

# Sample Input:

# 6	Вяххи	159
# 11	Федотов	172
# 7	Бондарев	158
# 6	Чайкина	153
# Sample Output:

# 1 -
# 2 -
# 3 -
# 4 -
# 5 -
# 6 156.0
# 7 158.0
# 8 -
# 9 -
# 10 -
# 11 172.0


def write(class_number, avr_height):
    arg = ''
    with open('output.txt') as data:
        if data.readline():
            arg = 'a'
        else:
            arg = 'w'

    with open('output.txt', arg) as ouf:
            ouf.write(str(class_number)+' '+avr_height+'\n')


with open('dataset_3380_5.txt') as data:
    classes = {}
    for i, item in enumerate(data):
        line_list = item.strip().split()
        line_list[0] = int(line_list[0])
        line_list[2] = int(line_list[2])
        classes[(line_list[1], i)] = line_list[0], line_list[2]


for i in range(1, 12):
    count_students = 0
    sum_height = 0
    for key, value in classes.items():
        if value[0] == i:
            sum_height += value[1]
            count_students += 1
    if count_students == 0:
        print(f'{i} -')
        write(i, '-')
    else:
        print(f'{i} {sum_height/count_students}')
        write(i, str(float(sum_height/count_students)))
