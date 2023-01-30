#Задача 4: Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным

print('This program takes a number representing the day of the week as input and checks if that day is a holiday.')
print("Please, enter a number for day of a week from 1 to 7:")
day_of_a_week = int(input())


def validation(day):
    if day>0 and day<8:
        return True
    else:
        return False

def check_for_holliday(day):
    if day==1 or day == 7:
        holliday = 1
    else:
        holliday = 0
    return holliday

if validation(day_of_a_week)==True:
    if check_for_holliday(day_of_a_week)==1:
        print("Today is a holiday!")
    else:
        print("Today isn't a holiday")
else:
    print("Incorrect day of a week")
    