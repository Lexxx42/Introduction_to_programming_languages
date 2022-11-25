
# for i in d:
#     print(f(i))


n = int(input())
d = []
for i in range(n):
    d.append(int(input()))
print(d)


for i in range(len(d) - 1, 1, -1):
    if i == 0:
        continue
    else:
        if d[i] == d[i - 1]:
            d.remove(d[i])