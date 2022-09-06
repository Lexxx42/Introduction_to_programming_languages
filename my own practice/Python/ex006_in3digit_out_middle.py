# Задача 1: Напишите программу, которая принимает на вход трёхзначное число и на выходе показывает вторую цифру этого числа.
print("This program takes a three-digit number as input and outputs the second digit of that number.")
print("Please enter 3 digit number")
number = int(input())
print()


def validation(number_for_check):
    if number_for_check > 99 and number_for_check < 1000:
        return True
    else:
        return False


def show_middle_digit(three_digit_number):
    three_digit_number //= 10  # // - деление, как целое число
    three_digit_number %= 10
    return three_digit_number


if validation(number) == True:
    print("Second digit =", show_middle_digit(number))
else:
    print("Your number isn't a 3 digit!")
