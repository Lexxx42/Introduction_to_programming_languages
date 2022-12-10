# Функции синтаксис

# Определение функции начинается со слова def

def function_name(argument1, argument2):
    # function body
    return argument1 + argument2
    # отсутствие знака отступа означает завершение тела функции для интерпретатора

# Определения функция в языке Python не выполняется построчно. Сначала интерпретатор дочитывает до места, где функция кончается.
# И только после этого будет создан объект для функции. Функции в языке Python являются объектами.
# В оперативной памяти будет создан объект и function_name будет ссылаться на этот объект


x = function_name(2, 8)
y = function_name(x, 21)
print(x)
print(y)
print(type(function_name(2, 8)))
print(id(x))  # 140736485708872

# Объект функции хранит в себе много всего: название функции, которым его создали; аргументы, которые он принимает; самое главное - хранит в себе тело функции
# которое будет затем исполнено

# Что происходит, когда мы исполняем функцию
# Если интерпретатор встречает в коде строку: x = function_name(2, 8) - прежде всего он смотрит на переменную и на какой объект она ссылается
# Он видит, что ссылается на объект функцию. И понимает, что function_name() принимает аргументы 1 и 2.
# Поэтому до исполнения тела функции всегда происходит инициализация аргументов.
# Те аргументы, которые мы передаем, когда вызываем функцию в наем случае - это объекты 2 и 8
# Они так же лежат в памяти. И до исполнения любого кода происходи инициализация аргументов
# Произойдет вот что: аргумент1 начнет ссылаться на объект 2, аргумент2 начнет ссылаться на объект 8
# Таким образом тело функции будет исполняться с уже известными аргументами
# Код тела функции будет исполняться построчно.
# Суммой аргументов будет объект 10. В памяти, если еще не существовало, будет создан объект 10.

# ТАК! МОЙ ЭКСПЕРИМЕНТ!

a = 10
print(id(a))  # 140736485708872

c = 5
print(id(c))  # 140736485708712
print(id(c*2))  # 140736485708872

# По идее объекты а и с будут ссылаться на объект х, который так же равен 10 и был уже создан выше. сейчас посмотрим
# Так и есть!

# Важно понимать, что когда мы вызываем функцию мы создаем аргументы заново
# рассмотрим вызов функции и присваивание его переменной
# y = function_name(x, 21)
# как мы уже знаем, х ссылается на результат предыдущего вызова на объект 10
# 21 тоже некая константа в памяти. Когда мы вызовем функцию у нас произойдет инициализация аргументов
# арг1 будет ссылаться на 10, аргумент2 ссылаться на 21.
# произойдет сложение в теле функции и будет создан объект 31, если он не был создан в памяти
# результат функции будет ссылаться на 31. после присваивания у будет ссылаться на 31.