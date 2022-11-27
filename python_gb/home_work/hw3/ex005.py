# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
#
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

def fib(n):
    if n > -1:
        if n == 0 or n == 1:
            return n
        else:
            return fib(n - 1) + fib(n - 2)
    if n <= 1:
        return ((-1) ** (abs(n) + 1)) * fib(abs(n))


def main():
    print('This program generates a list of Fibonacci numbers, including those for negative indexes.')
    num = int(input('Enter a Fibonacci number: '))
    if num < 0:
        print('Number must be positive')
        exit()
    for i in range(-num, num + 1):
        print(f'{fib(i)} ', end='')


if __name__ == '__main__':
    main()
