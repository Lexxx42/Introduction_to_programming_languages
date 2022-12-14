# У любого объекта в языке Python есть тип

# Тип определяет то, что мы можем сделать с объектом
# Есть ли у объекта длина, длинный он или короткий, можем ли мы сложить два различных объекта
# Все это определяется типом обхекта

# Если тип объекта - числа, то мы можем их сложить
# А если это строка, то у нее есть какая-то длина

# Так же тип объекта определяет возможные принимаемые значения
# Т.е. если мы говорим, что тип объекта - это целое число, то мы не сильно удивимся,
# если оно принимает значение 0, 14 или 31
# Таким образом в языке Python тип определяет поведение объекта и возможные принимаемые значения

# Прежде всего стоит отметить, что тип объекта не меняется в течении жизни объекта
# потому что пока объект существует мы ждем от него примерно одинаковое поведение
# узнать тип объекта в языке Python можно встроенной функции type()

# Тип объекта
# Тип объекта не может быть изменен после создания объекта (как и идентификатор)
# Узнать тип объекта можно с помощью функции type()

x = [1, 2, 3]
print(type(x))  # <class 'list'>
print(type(1))  # <class 'int'>

print(type(type(x)))  # <class 'type'>
print(type(print()))  # <class 'NoneType'>
print(type(None))  # <class 'NoneType'>
print(id(type(x)))  # 140721002405008
print(id(type(type(x))))  # 140721002418064

# типы в языке Python являются объектами
