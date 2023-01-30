# Задача 5 *: Напишите программу, которая генерирует несколько случайных чисел, и в цикле проверяет, кратны ли эти числа предварительно введенному числу,
# при кратности - цикл прерывается.
import random

print("This program generates several random numbers, and in the loop checks if these numbers are multiples of the previously entered number, if the multiplicity is - the loop is interrupted.")
print("Please, enter the number:")
number = int(input())


def validation(number_for_check):
    if number_for_check == 0:
        print("Divided by zero!")
        return False
    else:
        return True


def generate_number():
    number_generated = random.randint(1, 256)
    return number_generated


if validation(number) == True:
    while (True):
        generated_number = generate_number()
        if generated_number % number == 0:
            print(generated_number, "%", number, "-YES")
            break
        else:
            print(generated_number, "%", number, "-NO")
else:
    print("Please, enter a valid number!")
