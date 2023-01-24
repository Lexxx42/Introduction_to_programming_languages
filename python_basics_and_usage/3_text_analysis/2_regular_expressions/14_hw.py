# Вам дана последовательность строк.
# В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
# Буквой считается символ из группы \w.
# Sample Input:
#
# attraction
# buzzzz
# Sample Output:
#
# atraction
# buz


import sys
import re

pattern = r"(\w)\1+"
sys.stdin = open("hw14.txt")
for line in sys.stdin:
    line = line.strip()
    print(re.sub(pattern, r"\1", line))

[print(re.sub(r"(\w)\1+", r"\1", line), end="") for line in sys.stdin]
