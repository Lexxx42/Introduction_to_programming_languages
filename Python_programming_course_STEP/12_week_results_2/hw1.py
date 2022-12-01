# Напишите программу, которая принимает на стандартный вход список игр футбольных команд
# с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
#
# За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
#
# Формат ввода следующий:
# В первой строке указано целое число n — количество завершенных игр.
# После этого идет n строк, в которых записаны результаты игры в следующем формате:
# Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
#
# Вывод программы необходимо оформить следующим образом:
# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
#
# Конкретный пример ввода-вывода приведён ниже.
#
# Порядок вывода команд произвольный.
#
# Sample Input:
#
# 3
# Спартак;9;Зенит;10
# Локомотив;12;Зенит;3
# Спартак;8;Локомотив;15
# Sample Output:
#
# Спартак:2 0 0 2 0
# Зенит:2 1 0 1 3
# Локомотив:2 2 0 0 6

# Команда:Всего_игр Побед Ничьих Поражений Всего_очков
count = int(input())
match_results = {}

for i in range(count):
    match_result = input().split(';')
    for j in range(1, len(match_result), 2):
        match_result[j] = int(match_result[j])
    for k in range(0, len(match_result), 2):
        result = []
        if match_result[k] in match_results:
            if k == 0:
                result = match_results[match_result[k]]
                result[0] += 1
                if match_result[1] > match_result[3]:
                    result[1] += 1
                elif match_result[1] == match_result[3]:
                    result[2] += 1
                elif match_result[1] < match_result[3]:
                    result[3] += 1
                total_score = result[1] * 3 + result[2]
                result[4] = total_score
            if k == 2:
                result = match_results[match_result[k]]
                result[0] += 1
                if match_result[1] < match_result[3]:
                    result[1] += 1
                elif match_result[1] == match_result[3]:
                    result[2] += 1
                elif match_result[1] > match_result[3]:
                    result[3] += 1
                total_score = result[1] * 3 + result[2]
                result[4] = total_score

        else:
            if k == 0:
                result.append(1)
                if match_result[1] > match_result[3]:
                    result.append(1)
                    result.append(0)
                    result.append(0)
                else:
                    result.append(0)
                    if match_result[1] == match_result[3]:
                        result.append(1)
                        result.append(0)
                    else:
                        result.append(0)
                        result.append(1)
                total_score = result[1] * 3 + result[2]
                result.append(total_score)
            if k == 2:
                result.append(1)
                if match_result[1] < match_result[3]:
                    result.append(1)
                    result.append(0)
                    result.append(0)
                else:
                    result.append(0)
                    if match_result[1] == match_result[3]:
                        result.append(1)
                        result.append(0)
                    else:
                        result.append(0)
                        result.append(1)
                total_score = result[1] * 3 + result[2]
                result.append(total_score)
        match_results[match_result[k]] = result

for q, w in match_results.items():
    print((q+':'), *w, end='\n')

