# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*
#
# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

def user_input_quarter_number():
    quarter_number = int(input('Please enter quarter number > '))
    print_quarter(quarter_number)


def print_quarter(number):
    if number == 1:
        print(f'{number} -> x > 0, y > 0')
    elif number == 2:
        print(f'{number} -> x < 0, y > 0')
    elif number == 3:
        print(f'{number} -> x < 0, y < 0')
    elif number == 4:
        print(f'{number} -> x > 0, y < 0')
    else:
        print('You entered incorrect number for a quarter, please enter the valid value')
        user_input_quarter_number()


print('This program for a given quarter number, '
      'shows the range of possible coordinates of points in this quarter (x and y)')
while True:
    user_input_quarter_number()
