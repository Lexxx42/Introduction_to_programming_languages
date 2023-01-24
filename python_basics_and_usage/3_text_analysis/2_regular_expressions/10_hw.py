# Вам дана последовательность строк.
# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
#
# Sample Input:
#
# blabla is a tandem repetition
# 123123 is good too
# go go
# aaa
# Sample Output:
#
# blabla is a tandem repetition
# 123123 is good too

import sys
import re

pattern = r"\b(\w+)\1\b"
sys.stdin = open("hw10.txt")
for line in sys.stdin:
    line = line.strip()
    if re.search(pattern, line):
        print(line)

# https://habr.com/ru/post/349860/
