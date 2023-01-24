# Вам дана последовательность строк.
# В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.
#
# Sample Input:
#
# I need to understand the human mind
# humanity
# Sample Output:
#
# I need to understand the computer mind
# computerity

import sys
import re

pattern = "human"
sys.stdin = open("hw11.txt")
for line in sys.stdin:
    line = line.strip().replace(pattern, "computer")
    print(line)

# print(re.sub(r'human', 'computer', sys.stdin.read()), end='')
