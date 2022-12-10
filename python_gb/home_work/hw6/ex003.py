# 3. Написать функцию, аргументы имена сотрудников,
# возвращает словарь, ключи — первые буквы имён,
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
#
# out
#
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'],
# 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}
#


dict_of_employees = {}
for name in iter(input, ''):
    if name[0].upper() in dict_of_employees:
        dict_of_employees[name[0].upper()].append(name)
    else:
        dict_of_employees[name[0].upper()] = [name]
print(dict(sorted(dict_of_employees.items())))
