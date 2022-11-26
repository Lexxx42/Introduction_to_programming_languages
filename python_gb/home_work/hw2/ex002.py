# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]
from math import factorial


# Hard way
def fact(num):  # Factorial function.
    res = 1
    while num > 1:
        res *= num
        num -= 1
    return res


def print_fact(input_list):  # Print factorial function.
    if number < 0:
        print('Number must be positive')
        exit()
    elif number == 0 or number == 1:
        input_list.append(fact(0))
    else:
        for i in range(1, number + 1):
            input_list.append(fact(i))
    print(input_list)


print('This program takes the number N as input and '
      'outputs a set of products of numbers from 1 to N in the form of a list.')
print('Please enter a natural number > ', end='')
number = int(input())
list1 = []
print_fact(list1)

# Easy way :^)
# list1 = []
# for i in range(1, number+1):
#     list1.append(factorial(i))
# print(list1)
