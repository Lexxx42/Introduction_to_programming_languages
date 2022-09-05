from ast import For


print("программа выводит все четные числа от 1 до N")
print("Введите число N >")
number = int(input())
print()

def output(number_for_check):
    if (number_for_check) == 1:
        print("нет чисел в диапазоне от", 1,"до" , number_for_check)
    elif (number_for_check == -1 or number_for_check == 0):
        print(0)
    elif number_for_check > 0:
        for i in range(1, number_for_check+1, 1):
            if i % 2 == 0:
                print(i)

    else:
        for i in range(1, abs(number_for_check)+1, 1):
            if i % 2 == 0:
                print(-i)
output(number)
