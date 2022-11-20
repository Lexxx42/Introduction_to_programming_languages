n = int(input())
if n > 0:
    print(*range(-n, n + 1))  # raspacovka
else:
    print(*range(-n, n - 1, -1))
