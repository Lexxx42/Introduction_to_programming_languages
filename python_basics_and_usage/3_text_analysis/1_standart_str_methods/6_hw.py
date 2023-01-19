# Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.
#
# Выведите одно число – количество вхождений строки t в строку s.
#
# Пример:
# s = "abababa"
# t = "aba"
#
# Вхождения строки t в строку s:
# abababa
# abababa
# abababa
#
# Sample Input 1:
#
# abababa
# aba
# Sample Output 1:
#
# 3
# Sample Input 2:
#
# abababa
# abc
# Sample Output 2:
#
# 0
# Sample Input 3:
#
# abc
# abc
# Sample Output 3:
#
# 1
# Sample Input 4:
#
# aaaaa
# a
# Sample Output 4:
#
# 5

import sys

sys.stdin = open("hw6.txt")


# s, t = input(), input()
# count, position = 0, 0
# c_set = set()
# while s.find(t, position) >= 0:
#     c_set.add(s.find(t, position))
#     position += 1
# print(len(c_set))

# s, t = input(), input()
#
# print(sum(1 for i in range(len(s)) if s.startswith(t, i)))

# import re
#
# s, t = input(), '(?=' + input() + ')'
# print(len(re.findall(t, s)))

def cross_count(s, t):
    try:
        return 1 + cross_count(s[s.index(t) + 1:], t)
    except (ValueError, IndexError):
        return 0


print(cross_count(input(), input()))
