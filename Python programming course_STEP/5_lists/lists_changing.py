# В отличии от узученных типов данных (int, float, str) 
# списки (lists) являются изменяемыми
# Можно изменить конкретный элемент списка

students = ['Ivan', 'Masha', 'Sasha']
print(students)
students[1]='Oleg'
print(students)
print()
# Вставка элементов в список
students = ['Ivan', 'Masha', 'Sasha']
print(students)
students.insert(1, 'Olga')
print(students)
