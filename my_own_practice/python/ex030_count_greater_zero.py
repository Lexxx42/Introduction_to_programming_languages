# Задача 1: Пользователь вводит с клавиатуры M чисел. Посчитайте, сколько чисел больше 0 ввёл пользователь.
# 0, 7, 8, -2, -2 -> 2
# 1, -7, 567, 89, 223-> 3

# Counts numbers greater than zero.
def count_greater_zero(quantity):
    count = 0
    for i in range(0, quantity):
        print("Please enter", i+1, "number:")
        number = int(input())
        if number > 0:
            count = count+1
    return count


print("This program counts how many numbers user entered in a sequence of M numbers.")
print("Please enter how many numbers you want to enter:")
input_quantity = int(input())
print("User entered", count_greater_zero(
    input_quantity), "numbers greater than zero.")
