# Задача 2: Напишите программу, которая выводит случайное трёхзначное число и удаляет вторую цифру этого числа.
import random

print("This program generates random 3 digit number and show the number without second digit")


def symbol_funcion():
    number_symbol = random.randint(0, 2)
    if number_symbol == 0:
        symbol = ''
    else:
        symbol = '-'
    return symbol


symbol = symbol_funcion()


def random_generator():
    number = random.randint(100, 1000)
    print("number generated =", symbol, number)
    return number


def cut_middle_digit(number):
    number_saved = number
    number //= 10
    number //= 10
    first_digit = number
    number_saved %= 10
    number_saved %= 10
    number_without_middle_digit = first_digit*10 + number_saved
    return number_without_middle_digit


print("Number without middle digit is:", symbol,
      cut_middle_digit(random_generator()))
