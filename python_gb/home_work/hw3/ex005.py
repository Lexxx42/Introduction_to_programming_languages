# 5. ** Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
#
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21

def neg_fib(num):
    fib_list = [0, 1]
    for i in range(1, num):
        fib_list.append(fib_list[i] + fib_list[i - 1])
    print(fib_list)
    fib_list.insert(0, 1)
    fib_list.insert(0, -1)
    for i in range(2, num):
        fib_list.insert(0, fib_list[i + 2] - fib_list[i + 2])
    print(fib_list)


print('This program generates a list of Fibonacci numbers, including those for negative indexes.')
n = int(input('Enter a Fibonacci number: '))
neg_fib(n)
