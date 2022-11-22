students = ['Sasha', 'Ivan', 'Masha']
print()
print('students = ',students)
# В алфавитном порядке. Изначальный список не меняется
ordered_students = sorted(students)
print('ordered students = ', ordered_students)

# Изменяет сам список
print()
print('students = ', students)
students.sort()
print('sorted students = ',students)


# Если нужен самый первый студент или самый последний в списке
print()
print('students = ',students)
print('1st = ', min(students))
print('last = ', max(students))

# Чтобы все эти методы работали, нужно чтобы все элементы списка были сравнимы
