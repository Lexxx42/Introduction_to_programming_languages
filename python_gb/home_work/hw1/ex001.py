# 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def check_day_of_week(day_of_a_week):
    if day_of_a_week in range(6, 8):
        print(f'{day_of_a_week} -> да')
    elif day_of_a_week in range(1, 6):
        print(f'{day_of_a_week} -> нет')
    else:
        print('Day of a week is not correct, please enter the day again')
        user_input_day_of_week()


def user_input_day_of_week():
    day_of_a_week_input = int(input("Enter number of day of a week > "))
    check_day_of_week(day_of_a_week_input)


print("This program takes as input a number representing the day of the week and checks if that day is a holiday")
user_input_day_of_week()
