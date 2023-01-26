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

input_json = [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

file = json.dumps(input_json)
data_read = json.loads(file)
dict_json = {}
for i, item in enumerate(data_read):
    if not data_read[i]["parents"]:
        dict_json["".join(data_read[i]["name"]) + "+"] = data_read[i]["name"]
        continue
    dict_json["".join(data_read[i]["parents"])] = data_read[i]["name"]
dict_json = dict(sorted(dict_json.items()))
print(dict_json)

for value in dict_json.values():
    count = 0
    for key in dict_json:
        if value in key:
            count += 1
    print(f"{value} : {count}")
