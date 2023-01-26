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

data2 = {i: 0 for i in children}
print(data2)  # РЕБЕНОК : КОЛ-ВО ПОТОМКОВ

for i in dict_json:
    visited = []
    f()

# Для тех, кто отчаялся : из введенного текста json создаем первый словарь data( значение name становится ключом, а значение parents становится его значением), который имеет вид РЕБЕНОК : [РОДИТЕЛИ], второй словарь  data2 имеет вид РЕБЕНОК : КОЛ-ВО ПОТОМКОВ. Изначально значения ключей в data2 равны нулю. Запускаем цикл для data, и в нем будет создаваться пустой список visited и вызываться функция, в которую передаем ключ и его значение(РЕБЕНОК, [РОДИТЕЛИ]). В функции запускаем цикл для [РОДИТЕЛИ] , делаем в нем проверку, есть ли вершина в списке visited( вершина в данном случае - это переменная цикла). Если нету, то к значению data2[вершина] прибавляем 1(тут использовать конструкцию try..except, т.к. не факт, что данный класс объявлялся, и если ловим исключение то создаем ключ для данного класса в data2 со значением 1). Затем добавляем эту вершину в список visited и снова вызываем функцию(РЕБЕНОК, data[вершина]).  В конце просто вывести ключи со значениями data2 по алфавиту. Для тех, кто решил, можете посмотреть решение #27011572. Удачи)
