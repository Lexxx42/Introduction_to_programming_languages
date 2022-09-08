# Напишите программу, которая принимает на вход some число и проверяет, является ли оно палиндромом

from audioop import reverse


print("This program takes at least 2 digit number as input and checks if it is a palindrome")
print("Please, enter some number:")
number = int(input())


def validation(number_for_check):
    if number_for_check > 0 and number_for_check < 10:
        print("Number is 1 digit!")
        return False
    elif number_for_check < 0 and number_for_check > -10:
        print("Number is 1 digit!")
        return False
    elif number_for_check == 0:
        print("Number is 1 digit!")
        return False
    else:
        return True


def check_for_a_palindrome(number_for_check):
    number_for_check_saved = abs(number_for_check)
    number_for_check = abs(number_for_check)
    reversed_number = 0
    while number_for_check > 0:
        reversed_number *= 10
        reversed_number += number_for_check % 10
        number_for_check //= 10
    print("Your number is", number_for_check_saved,
          "reversed number is", reversed_number)
    if reversed_number == number_for_check_saved:
        print("Number is a palindrome")
    else:
        print("Number isn't a palindrome")


if validation(number) == True:
    check_for_a_palindrome(number)
else:
    print("Enter a valid number, please")
