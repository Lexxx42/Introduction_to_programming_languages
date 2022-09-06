# Задача 3: Напишите программу, которая выводит третью цифру заданного числа или сообщает, что третьей цифры нет.
import array as arr


print("This program prints the third digit of the given number, or reports that there is no third digit.")
print("Please, enter some three-digit number")

number = int(input())


def validation(number_for_check):
    if number < 99:
        return False
    else:
        return True


if validation(number) == True:
    while number > 1000:
        number //= 10
    print(number % 10)
else:
    print("There is no third digit in this number")
    # works only with positives
