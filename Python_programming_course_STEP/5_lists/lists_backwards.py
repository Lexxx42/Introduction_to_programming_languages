students = ['Sasha', 'Ivan', 'Masha']
print(students)
students.reverse()  # изменяет начальный список
print(students)

print()
print(students)
print(list(reversed(students)))  # не меняет начальный объект

print()
print(students)
print(students[::-1])  # не меняет начальный объект
print(students)