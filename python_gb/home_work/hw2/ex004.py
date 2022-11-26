# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапазоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20
#
# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!


print('Enter the value of N: ', end='')
n = int(input())
print('Enter position one: ', end='')
position_one = int(input())
print('Enter position two: ', end='')
position_two = int(input())

list1 = []
for i in range(abs(n) * 2 + 1):
    list1.append(-n + i)
print(list1)

if len(list1) >= position_one > 0 and len(list1) >= position_two > 0:
    print(f' -> {list1[position_one - 1] * list1[position_two - 1]}')
else:
    print('There are no values for these positions!')
