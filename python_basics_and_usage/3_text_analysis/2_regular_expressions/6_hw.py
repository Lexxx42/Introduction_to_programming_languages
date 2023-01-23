# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
#
# Примечание:
# Считать все строки по одной из стандартного потока ввода вы можете, например, так
#
# import sys
#
# for line in sys.stdin:
#     line = line.rstrip()
#     # process line
#
# Sample Input:
#
# catcat
# cat and cat
# catac
# cat
# ccaatt
# Sample Output:
#
# catcat
# cat and cat


import sys
import re

# sys.stdin = open("hw6.txt")
# pattern = "cat"
#
# for line in sys.stdin:
#     line = line.strip()
#     print(line + '\n' if len(re.findall(pattern, line)) >= 2 else "", end='')


sys.stdin = open("hw6.txt")
pattern = r"(cat.*){2,}"
for line in sys.stdin:
    line = line.strip()

    if re.search(pattern, line):
        print(line)
