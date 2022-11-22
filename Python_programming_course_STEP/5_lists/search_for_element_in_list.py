# Delete from list
students = ['Ivan', 'Masha', 'Sasha']

# Удаление по значению. УДАЛЯЕТ ТОЛЬКО ПЕРВОЕ ВХОЖДЕНИЕ В СПИСОК
students.remove('Sasha')
print(students)

# Удаление по индексу
del students[0]
print(students)

# Оба метода выдадут ошибку, если значения не будет в списке 
# или индекс выйдет за пределы и программа не сможет продолжиться

# Что если нам нужно сперва проверить, а потом удалять?

# Поиск элементов в списке
print()
students = ['Ivan', 'Masha', 'Sasha']
print(students)
if 'Ivan' in students:
    print('Ivan is here!')
if 'Ann' not in students:
    print('Ann is out')
if ['Sasha'] in students:  # not working!
    print('Sasha is a student')

ind = students.index('Sasha')
print(ind)  # 2
ind = students.index('Ann')
print(ind)  # ValueError: 'Ann' is not in list
