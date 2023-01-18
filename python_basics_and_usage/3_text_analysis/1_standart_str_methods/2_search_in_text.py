# Говоря о поиске в тексте важно понимать, что в языке python мы храним текстовую информацию
# в переменных текстового типа.
# Поэтому было бы неплохо вспомнить какие функции и методы есть у строк в стандартной библиотеке,
# которые могли бы пригодиться для решения наших конкретных задач.

# print("abc" in "abcba")
# print("abce" in "abcba")

# Однако, если нас интересует конкретное место, начиная с которого наша строка входит в строку,
# то

print("cabcd".find("abc"))  # Индекс первого вхождения или -1: 1
print("cabcd".find("фыв"))  # -1

# Здесь и далее, когда мы будем использовать стандартные методы и функции языка python
# я советую читать их документацию.
# Прежде всего в документации вы найдете те аргументы, которые имеют значение по умолчанию
# и чаще всего замалчиваются.
# А именно эти аргументы помогут нам расширить область применения функции.

# print(str.find.__doc__)

print("cabcd"[1:].find("abc"))

print("***")
print("cabcd".index("abc"))  # Индекс первого вхождения или ValueError
# print("cabcd".index("aaa"))  # ValueError: substring not found

print("+++")
# Мы можем использовать метод startswith(), чтобы проверять, начинается ли строка с
s = "One way to get the value of a property is to call the function."
# print(s.startswith("One way to"))  # True
# print(s.startswith("asdf"))  # False
# print(str.startswith.__doc__)
print(s.startswith(("one way", "Two ways", "One way")))

print("---")
s = "image.png"
print(s.endswith(".jpg"))

print("@@@")
s = "ababa"
print(s.count("aba"))  # Сколько раз строка входит в строку.
# print(str.count.__doc__)

# У многих методов есть правосторонние аналоги, которые читают строку справа налево.
print("$$$")
s = "abacaba"
print(s.find("aba"))  # 0
print(s.rfind("aba"))  # 4
