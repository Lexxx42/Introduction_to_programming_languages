# Напишите простой калькулятор, который считывает с пользовательского ввода три строки: 
# первое число, второе число и операцию, 
# после чего применяет операцию к введённым числам 
# ("первое число" "операция" "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

# Обратите внимание, что на вход программе приходят вещественные числа.

def Call(operation_code, number_1, number_2):
    if operation_code == '+':
        result(summarize(number_1, number_2))
    elif operation_code == '-':
        result(diff(number_1, number_2))
    elif operation_code == '/':
        if number_2 == 0:
            print('Деление на 0!')
        else:
            result(divide(number_1, number_2))
    elif operation_code == '*':
        result(multiply(number_1, number_2))
    elif operation_code == "mod":
        if number_2 == 0:
            print('Деление на 0!')
        else:
            result(ostatok(number_1, number_2))
    elif operation_code == "pow":
        result(power(number_1, number_2))
    elif operation_code == "div":
        if number_2 == 0:
            print('Деление на 0!')
        else:
            result(div(number_1, number_2))


def summarize(num1, num2):
    return num1+num2


def diff(num1, num2):
    return num1-num2


def divide(num1, num2):
    return num1/num2


def multiply(num1, num2):
    return num1*num2


def ostatok(num1, num2):
    return num1 % num2


def power(num1, num2):
    return num1 ** num2


def div(num1, num2):
    return num1//num2

def result(number):
    print(number)

first_number = float(input())
second_number = float(input())
operation = input()
Call(operation, first_number, second_number)