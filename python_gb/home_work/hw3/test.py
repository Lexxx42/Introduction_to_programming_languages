def fib(n):
    if n > -1:
        if n == 0 or n == 1:
            return n
        else:
            return fib(n - 1) + fib(n - 2)
    if n <= 1:
        return ((-1) ** (abs(n) + 1)) * fib(abs(n))


num = int(input('Enter a Fibonacci number: '))
if num == 0:
    print()
for i in range(-num, num+1):
    print(f'{fib(i)} ', end='')
