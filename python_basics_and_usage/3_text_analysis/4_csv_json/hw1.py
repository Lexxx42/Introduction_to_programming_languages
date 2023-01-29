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
import networkx as nx
from itertools import count

# Ответ:
#
# A : 5
# B : 1
# C : 4
# D : 2
# E : 1
# F : 3

# input_json = [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
input_json = [{"name": "beta", "parents": ["alpha", "gamma"]}, {"name": "gamma", "parents": ["alpha"]},
              {"name": "alpha", "parents": []}, {"name": "delta", "parents": ["gamma", "zeta"]},
              {"name": "epsilon", "parents": ["delta"]}, {"name": "zeta", "parents": []}]
# input_json = json.loads(input())

file = json.dumps(input_json)
data_read = json.loads(file)

dict_json = {}

for i, item in enumerate(data_read):
    for parent in item["parents"]:
        if parent not in dict_json:
            dict_json[parent] = {item["name"]}
        else:
            dict_json.get(parent).add(item["name"])
sorted_tuples = sorted(dict_json.items(), key=lambda item: item[0])
dict_json = {k: v for k, v in sorted_tuples}

for key, value in dict_json.items():
    dict_json[key] = set(sorted(value))
print("parents:children", dict_json)  # parents:children

list_1 = []

children = set()
for j, item in enumerate(data_read):
    children.add(item['name'])
children = sorted(children)

print(children)

data2 = {i: 0 for i in children}
print(data2)  # РЕБЕНОК : КОЛ-ВО ПОТОМКОВ

# for key in data2:
#     print(f"{key} : {(len(dict_json[key])+1) if key in dict_json else 1}")

dict_json_children = {}
for i, item in enumerate(data_read):
    dict_json_children[item["name"]] = set(sorted((data_read[i]["parents"])))
print("children:parents", dict_json_children)


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited



for child in children:
    list_1.append(dfs(dict_json_children, child))
print(list_1)
list_2 = []
for i, item in enumerate(list_1):
    print(item)
    for elem in item:
        list_2.append(elem)
print(sorted(list_2))
for child in children:
    print(f"{child} : {list_2.count(child)}")
