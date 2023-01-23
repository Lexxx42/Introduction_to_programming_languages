# Вам дана последовательность строк.
# Выведите строки, содержащие обратный слеш "\﻿".
# Sample Input:
#
# \w denotes word character
# No slashes here
# Sample Output:
#
# \w denotes word character

import sys

sys.stdin = open("hw9.txt")
for line in sys.stdin:
    if "\\" in line:
        print(line)
