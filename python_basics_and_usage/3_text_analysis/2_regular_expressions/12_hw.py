# Вам дана последовательность строк.
# В каждой строке замените первое вхождение слова,
# состоящего только из латинских букв "a" (регистр не важен), на слово "argh".

# Примечание:
# Обратите внимание на параметр count у функции sub.
# Sample Input:

# There’ll be no more "Aaaaaaaaaaaaaaa"
# AaAaAaA AaAaAaA
# Sample Output:

# There’ll be no more "argh"
# argh AaAaAaA

import sys
import re

pattern = r"\ba+\b"
sys.stdin = open("hw12.txt")
for line in sys.stdin:
    line = line.strip()
    print(re.sub(pattern, "argh", line, 1, re.IGNORECASE))

# [print(re.sub(r'\b[aA]+\b', 'argh', line.rstrip(), 1)) for line in sys.stdin]

[print(re.sub(r"\ba+\b", "argh", line, 1, re.IGNORECASE), end="") for line in sys.stdin]
