# 2. Напишите программу для проверки ложности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def check_for_falsity(x, y, z):
    if (x or y or z) != (not x and not y and not z):
        print('Statement is True')
    else:
        print('Statement is False')


def user_input():
    x = input('Please enter X value > ')
    y = input('Please enter Y value > ')
    z = input('Please enter Z value > ')
    check_for_falsity(x, y, z)


print("This program checks if the ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z assertion is false for all values of the predicate")
user_input()
