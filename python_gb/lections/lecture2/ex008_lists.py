list1 = [1, 2, 3, 4, 5]
list2 = list1

# for e in list1:
#     print(e, end=' ')
# print()
# for e in list2:
#     print(e, end=' ')
# print()
#
# list1[0] = 123
# list2[1] = 32
#
# for e in list1:
#     print(e, end=' ')
# print()
# for e in list2:
#     print(e, end=' ')
# print()

list1 = [1, 2, 3, 4, 5]
# Удаление последнего элемента списка

print(list1.pop())
print(list1)
print(list1.pop())
print(list1)
print(list1.pop())
print(list1)


# Чтобы удалить конкретный элемент передаем изначение индекса в pop()
list1 = [1, 2, 3, 4, 5]
print(list1.pop(2))
print(list1)

# Вставка на нужную позицию
print(list1.insert(2, 11))
print(list1)
