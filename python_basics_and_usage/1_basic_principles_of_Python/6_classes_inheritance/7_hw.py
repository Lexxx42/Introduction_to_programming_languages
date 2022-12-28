# Вам дано описание наследования классов в следующем формате.
# <имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
# Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.
#
# Или эквивалентно записи:
#
# class Class1(Class2, Class3 ... ClassK):
#     pass
# Класс A является прямым предком класса B, если B отнаследован от A:
#
#
# class B(A):
#     pass
#
#
# Класс A является предком класса B, если
# A = B;
# A - прямой предок B
# существует такой класс C, что C - прямой предок B и A - предок C
#
# Например:
# class B(A):
#     pass
#
# class C(B):
#     pass
#
# # A -- предок С
#
#
# Вам необходимо отвечать на запросы, является ли один класс предком другого класса
#
# Важное примечание:
# Создавать классы не требуется.
# Мы просим вас промоделировать этот процесс,
# и понять существует ли путь от одного класса до другого.
# Формат входных данных
# В первой строке входных данных содержится целое число n - число классов.
#
# В следующих n строках содержится описание наследования классов.
# В i-й строке указано от каких классов наследуется i-й класс.
# Обратите внимание, что класс может ни от кого не наследоваться.
# Гарантируется, что класс не наследуется сам от себя (прямо или косвенно),
# что класс не наследуется явно от одного класса более одного раза.
#
# В следующей строке содержится число q - количество запросов.
#
# В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
# Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.
#
# Формат выходных данных
# Для каждого запроса выведите в отдельной строке слово "Yes",
# если класс 1 является предком класса 2, и "No", если не является.
#
# Sample Input:
#
# 4
# A
# B : A
# C : A
# D : B C
# 4
# A B
# B D
# C D
# D A
# Sample Output:
#
# Yes
# Yes
# Yes
# No

import sys

sys.stdin = open("input.txt", "r")


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path:
                return new_path
    return None


n = int(input())
answer = dict()
for i in range(n):
    input_list = input().replace(':', "").split()
    if input_list[len(input_list) - 1] in answer:
        for k in range(1, len(input_list)):
            if input_list[k] in answer:
                answer.get(input_list[k]).append(input_list[0])
            else:
                answer[input_list[k]] = []
                answer.get(input_list[k]).append(input_list[0])
    else:
        for j in range(1, len(input_list)):
            answer_list = []
            answer_list.append(input_list[0])
            answer[input_list[j]] = answer_list

q = int(input())
for c in range(q):
    request = input().split()
    if find_path(answer, request[0], request[1]):
        print("Yes")
    else:
        print("No")
