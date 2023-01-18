# Очень часто бывает, что часто часть текста в верхнем регистре,
# а другая в нижнем.
# Например, мы знаем, что все предложения начинаются с большой буквы.

# Однако это немного усложняет нам поиск конкретного слова в данном тексте
# Потому что слова в python написанные в разном регистре считаются отличными друг
# от друга.

# Для этого у нас есть методы lower(), upper()

s = "ku-Ku, blyAT!"
print(s.count("ku"))
print(s.lower())
print(s.lower().count("ku"))
print(s.upper())
print(s.upper().count("ku"))

# 1
# ku-ku, blyat!
# 2
# KU-KU, BLYAT!
# 0

# Метод replace() позволяет найти все вхождения
print("ppp")
s = "1, 2, 3, 4"
print(s)  # 1, 2, 3, 4
print(s.replace(",", "!"))  # 1! 2! 3! 4
# print(str.replace.__doc__)
# Как видим из документации replace() принимает аргумент count - максимальное число замен.
print(s.replace(",", "!", 2))  # 1! 2! 3, 4

print("***")
s = "1 2 3 4"
print(s.split(" "))  # ['1', '2', '3', '4']
# Можем разделить строку по заданному разделителю
# Метод split() возвращает список.
# print(str.split.__doc__)

print(s.split(" ", 2))  # ['1', '2', '3 4']

s = "            1\t\t\n     2  3 \n 4    "
print(s.split())

print(repr(s.lstrip()))
print(repr(s.strip()))
print(repr(s.rstrip()))

print("+++")
s = "_*__1, 2, 3, 4__*_"

print(repr(s.lstrip("*_")))
print(repr(s.strip("*_")))
print(repr(s.rstrip("*_")))

# Метод join()
print("QQQ")
numbers = map(str, [1, 2, 3, 4])
print(repr(" ".join(numbers)))
# Элементы последовательности для метода join() д.б строками.

# Часть из данных функций имеет правосторонние аналоги.
