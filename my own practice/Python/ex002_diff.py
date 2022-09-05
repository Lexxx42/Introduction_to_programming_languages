print("Программа на вход принимает два числа и выдает, какое число большее, а какое меньшее")
print("Введите первое число >")
first_number = int(input())
print("Введите second число >")
second_number = int(input())

if first_number > second_number:
    print("max =", first_number, "min=", second_number)
else:
    print("max =", second_number, "min=", first_number)
