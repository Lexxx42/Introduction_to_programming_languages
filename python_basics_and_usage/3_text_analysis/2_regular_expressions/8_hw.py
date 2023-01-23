# Вам дана последовательность строк.
# Выведите строки, содержащие две буквы "z", между которыми ровно три символа.
# Sample Input:
#
# zabcz
# zzz
# zzxzz
# zz
# zxz
# zzxzxxz
# Sample Output:
#
# zabcz
# zzxzz

import sys
import re

pattern = r"z...z"
sys.stdin = open("hw8.txt")
for line in sys.stdin:
    line = line.strip()
    if re.search(pattern, line):
        print(line)
