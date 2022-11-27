n = int(input())
d = {}
while len(d) < n:
    temp = int(input())
    d[temp] = f(temp)
    print(d[temp])

