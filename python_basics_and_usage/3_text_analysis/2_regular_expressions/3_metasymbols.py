# Метасимволов много и надо знать, что это металимвол просто потому что, когда в регулярном
# выражении встречается метасимвол оно не воспринимается как обычный символ.

# Это значит, что нужно сделать что-то специальное.
# А время от времени метасимвол нужно использовать в качестве обычного символа, например знак вопроса.

import re

pattern = r"english?"
string = "Do you speak english?"
match = re.search(pattern, string)
print(match)  # <re.Match object; span=(13, 20), match='english'>

# Мы увидим, что match не содержит знака вопроса.

# Дело в том, что знак вопроса является метасимволом в регулярном выражении.
# И если мы хотим найти символ вопросительного знака мы должны этот символ экранировать
# с помощью обратного слеша.

print('***')
pattern = r"english\?"
string = "Do you speak english?"
match = re.search(pattern, string)
print(match)  # <re.Match object; span=(13, 20), match='english'>

# И так будет с каждым метасимволом.
# В том числе мы должны экранировать обратный слеш.

# Метасимволы: . ^ $ * + ? { } [ ] \ | ( )

print('+++')
pattern = r"a[a-zA-Z]c"  # Указание диапазона доступных символов через "-".
# Все буквы английского алфавита.
string = "acc"
match_obj = re.match(pattern, string)
print(match_obj)

string = "abc, acc, aac, aBc, aAc"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)

# Также внутри нашего множества символов мы можем использовать
# символ циркумфлекс или крышка для того, чтобы описать те множества символов,
# которые нам не подходят.

print('%%%')
pattern = r"a[^a-zA-Z]c"  # Нам не подходят символы от a до z, и от A до Z.
string = "acc"
match_obj = re.match(pattern, string)
print(match_obj)

string = "abc, a.c, a-c, aBc, aAc"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)

# Так как некоторые группы символов используются в регулярных выражениях достаточно часто,
# то для них уже существует короткая запись.

# [] -- можно указать множество подходящих символов
# \d ~ [0-9] -- цифры
# \D ~ [^0-9]

# \s ~ [ \t\n\r\f\v] -- пробельные символы
#  - пробел
# \t - табуляция
# \n - перенос строки
# \r - перенос каретки
# \f - перенос страницы
# \v - вертикальная табуляция

# \S ~ [^ \t\n\r\f\v]
# \w ~ [a-zA-Z0-9_] -- буквы + цифры + _
# \W ~ [^a-zA-Z0-9_]

print('%%%')
pattern = r"a[\w.]c"  # Нам не подходят символы от a до z, и от A до Z.
string = "acc"
match_obj = re.match(pattern, string)
print(match_obj)

string = "abc, a.c, a-c, aBc, aAc"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)

# Метасимвол "." - любой символ кроме переноса строки будет подходить под точку.

print('№№№')
pattern = r"a.c"  # Все кроме переноса строки.
string = "acc"
match_obj = re.match(pattern, string)
print(match_obj)

string = "abc, a.c, a-c, aBc, aAc , a\tc"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)

# Таким образом, мы используем квадратные скобки, когда мы хотим перечислить множество символов,
# которое подходит под данный шаблон.
# Более того, некоторые множества символов заранее определены, например \d определяет
# множество всех цифр.

# Такие более короткие версии можно использовать внутри квадратных функций,
# чтобы дополнить то множество, которое нам нужно.
