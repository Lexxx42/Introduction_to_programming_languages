# Напишите программу, которая принимает на вход число и выдаёт сумму цифр в числе.


print("This program takes your number and provides the sum of digits in that number")
print("Please enter the number :")

number = int(input())


def sum_of_digits(number):
    number = abs(number)  # for negative values
    if (-10 < number and number < 1) or (0 < number and number < 10):
        return 1
    sum = 0
    while number >= 10:
        sum += number % 10
        number //= 10
    sum = sum+number
    return sum


print(sum_of_digits(number))
