
# Считываем 2 числа и выводим результат деления либо пишем, что деление невозможно.

a = int(input('enter a '))
b = int(input('enter b '))
if b!=0:
    print(a/b)
else:
    print('Division by zero!')
    b = int(input('enter not null b '))
    if b==0:
        print("You didn't enter valid value.")
    else:
        print(a/b)

