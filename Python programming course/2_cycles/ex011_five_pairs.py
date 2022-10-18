# читаем 5 пар чисел и выводим их произведение

# i = 0
# while i < 5:
#     a, b = input().split(',')
#     a = int(a)
#     b = int(b)
#     print(a*b)
#     i += 1


# прерывание цикла break

# i = 0
# while i < 2:
#     a, b = input().split(',')
#     a = int(a)
#     b = int(b)
#     if a == 0 and b == 0:
#         print("break of 1")
#         break  # досрочно прерываем цикл
#     print(a*b)
#     i += 1
# else: - условие если цикл завершился не по оператору break
# else:
#     print("end of 1")


# continue - оператор перехода к следующей итерации цикла (если она есть)

i = 0
while i < 5:
    a, b = input().split(',')
    a = int(a)
    b = int(b)
    if a == 0 and b == 0:
        print(i)
        break  # досрочно прерываем цикл
    if a == 0 or b == 0:
        continue  # переходим к след итерации
    print(a*b)
    i += 1
# else: - условие если цикл завершился не по оператору break
else:
    print("end of 2")
