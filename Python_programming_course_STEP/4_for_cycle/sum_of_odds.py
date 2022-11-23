a, b = input().split()
a = int(a)
b = int(b)
s = 0

if a % 2 == 0:
    a += 1
for i in range(a, b+1, 2):
    s += i
print(s)
