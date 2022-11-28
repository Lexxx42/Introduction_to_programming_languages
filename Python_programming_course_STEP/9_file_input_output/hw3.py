# Имеется файл с данными по успеваемости абитуриентов.
# Он представляет из себя набор строк, где в каждой строке записана следующая информация:
# Фамилия;Оценка_по_математике;Оценка_по_физике;Оценка_по_русскому_языку
# Поля внутри строки разделены точкой с запятой, оценки — целые числа.
# Напишите программу, которая считывает исходный файл с подобной структурой
# и для каждого абитуриента записывает его среднюю оценку по трём предметам на отдельной строке,
# соответствующей этому абитуриенту, в файл с ответом.
#
# Также вычислите средние баллы по математике,
# физике и русскому языку по всем абитуриентам и добавьте полученные значения,
# разделённые пробелом, последней строкой в файл с ответом.
#
# В качестве ответа на задание прикрепите полученный файл со
# средними оценками по каждому ученику и одной строкой со средними оценками по трём предметам.
#
# Примечание. Для разбиения строки на части по символу ';' можно использовать метод split следующим образом:
#
# print('First;Second-1 Second-2;Third'.split(';'))
# # ['First', 'Second-1 Second-2', 'Third']
# Sample Input:
#
# Петров;85;92;78
# Сидоров;100;88;94
# Иванов;58;72;85
# Sample Output:
#
# 85.0
# 94.0
# 71.666666667
# 81.0 84.0 85.666666667

with open('dataset_3363_4.txt') as inf:  # закрывается самостоятельно
    list_input = []
    for line in inf:
        line = line.strip()
        list_input.append(line.split(';'))
    for i in range(len(list_input)):
        for j in range(1, len(list_input[0])):
            list_input[i][j] = int(list_input[i][j])
    list_avg_grades_student = []
    avg_grades_student = 0
    for i in range(len(list_input)):
        for j in range(1, len(list_input[0])):
            if j == len(list_input[0]) - 1:
                avg_grades_student += list_input[i][j]
                list_avg_grades_student.append(avg_grades_student / (len(list_input[0]) - 1))
                avg_grades_student = 0
                continue
            avg_grades_student += list_input[i][j]
    print(list_avg_grades_student)

    list_avg_grades_subject = []
    avg_grades_subject = 0
    for j in range(1, len(list_input[0])):
        for i in range(len(list_input)):
            if i == len(list_input) - 1:
                avg_grades_subject += list_input[i][j]
                list_avg_grades_subject.append(str(avg_grades_subject / (len(list_input))))
                avg_grades_subject = 0
                continue
            avg_grades_subject += list_input[i][j]
    print(list_avg_grades_subject)
    list_avg_grades_subject_str = ' '.join(list_avg_grades_subject)
with open('output_data.txt', 'w') as ouf:
    for i in list_avg_grades_student:
        ouf.write(f'{i}\n')
    ouf.write(' '.join(list_avg_grades_subject))
