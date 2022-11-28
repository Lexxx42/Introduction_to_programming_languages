list_input = [['Петров', 85, 92, 78], ['Сидоров', 100, 88, 94], ['Иванов', 58, 72, 85]]

list_avg_grades_subject = []
avg_grades_subject = 0
for j in range(1, len(list_input[0])):
    for i in range(len(list_input)):
        if i == len(list_input) - 1:
            avg_grades_subject += list_input[i][j]
            list_avg_grades_subject.append(avg_grades_subject / (len(list_input[0]) - 1))
            avg_grades_subject = 0
            continue
        avg_grades_subject += list_input[i][j]
print(list_input)
print(list_avg_grades_subject)
