from functools import lru_cache

@lru_cache()
def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)

print(fib(499))


n = 5000
f1 = 0
f2 = 1
f3 = 0
i = 0
if n == 1:
        print(1)
else:
    while i in range(n):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        i += 1
print(f3)