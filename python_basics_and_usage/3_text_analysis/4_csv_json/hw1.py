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

input_json = [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
# input_json = json.loads(input())

file = json.dumps(input_json)
data_read = json.loads(file)

dict_json = {}

for i, item in enumerate(data_read):
    if not data_read[i]["parents"]:
        dict_json[data_read[i]["name"]] = set(data_read[i]["name"])
        continue
    for parent in data_read[i]["parents"]:
        if parent not in dict_json:
            dict_json[parent] = set(data_read[i]["name"])
        else:
            dict_json.get(parent).add(data_read[i]["name"])
sorted_tuples = sorted(dict_json.items(), key=lambda item: item[1])
dict_json = {k: v for k, v in sorted_tuples}
print(dict_json)  # parents:children
list_1 = []

children = set()
for j, item in enumerate(data_read):
    children.add(item['name'])
children = sorted(children)

print(children)

data2 = {i : 0 for i in children}
print(data2) # РЕБЕНОК : КОЛ-ВО ПОТОМКОВ

for i in dict_json:
    visited = []
    f()
