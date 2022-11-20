# sum from a to b
from re import A, I


a = int(input())
b = int(input())

s = 0
i = a
while i <= b:
    s += i
    i += 1
print(s)
