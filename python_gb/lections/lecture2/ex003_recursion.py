# Рекурсия

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


list_1 = []
for w in range(1, 10):
    list_1.append(fib(w))
print(list_1)  # [1, 1, 2, 3, 5, 8, 13, 21, 34]
