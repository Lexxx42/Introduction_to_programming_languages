# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам.
# У каждого JSON-объекта есть поле name, которое содержит имя класса,
# и поле parents, которое содержит список имен прямых предков.

# Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

# Эквивалент на Python:

# class A:
#     pass

# class B(A, C):
#     pass

# class C(A):
#     pass

# Гарантируется, что никакой класс не наследуется от себя явно или косвенно,
# и что никакой класс не наследуется явно от одного класса более одного раза.

# Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

# <имя класса> : <количество потомков>

# Выводить классы следует в лексикографическом порядке.

# Sample Input:

# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
# Sample Output:

# A : 3
# B : 1
# C : 2

import json


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


input_json = [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

file = json.dumps(input_json)
data_read = json.loads(file)

dict_json_children = {}
for i, item in enumerate(data_read):
    dict_json_children[item["name"]] = set(sorted((data_read[i]["parents"])))

children = set()
for j, item in enumerate(data_read):
    children.add(item['name'])
children = sorted(children)
list_1 = []

for child in children:
    list_1.append(dfs(dict_json_children, child))

list_2 = []
for i, item in enumerate(list_1):
    for elem in item:
        list_2.append(elem)

for child in children:
    print(f"{child} : {list_2.count(child)}")
