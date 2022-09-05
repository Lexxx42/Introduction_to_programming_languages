print("Программа проверяет введенное число, является ли оно четным или нет")
print("Введите число >")
number = int(input())

if number % 2 == 0:
    print("Number", number, "is even!")
else:
    print("Number", number, "isn't even!")
