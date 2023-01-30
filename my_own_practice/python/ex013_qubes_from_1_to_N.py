# Задача 3
# Напишите программу, которая принимает на вход число (N) и выдаёт таблицу кубов чисел от 1 до N.
# 3 -> 1, 8, 27
# 5 -> 1, 8, 27, 64, 125

print("This program takes a number (N - natural) as input and produces a list of cubes of numbers from 1 to N.")
print("Please enter a number")
number = int(input())
if number == 0:
    print("0 ^ 3 =",0)
else:
    print("List of cubes: ", end='')
    if(number<0):
        for i in range(1,abs(number)+1):
            print(-i**3,' ',end='')
    else:
        for i in range(1,abs(number)+1):
            print(i**3,' ',end='')
