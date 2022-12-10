# * 4. Функция принимает в качестве аргументов строки в формате «Имя Фамилия»,
# возвращает словарь, ключи — первые буквы фамилий,
# значения — словари, реализованные по схеме предыдущего задания.
# in
# "Иван Сергеев", "Инна Серова", "Петр Алексеев",
# "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
# "Борис Аркадьев", "Антон Серов", "Павел Анисимов"
#
# out
#
# {'С': {'А': ['Анна Савельева', 'Антон Серов'],
# 'И': ['Иван Сергеев', 'Инна Серова']}, 'А': {'Б': ['Борис Аркадьев'],
# 'П': ['Павел Анисимов', 'Петр Алексеев']}, 'И': {'И': ['Илья Иванов']},
# 'В': {'Ю': ['Юнона Ветрякова']}}


dict_of_employees = {}


def create_dict_employees(employee_n, employee_s) -> dict:
    """Creation of a dictionary of employees."""
    if employee_s[0] in dict_of_employees:
        if employee_n[0] in dict_of_employees.get(employee_s[0]):
            dict_of_employees.get(employee_s[0]).get(employee_n[0]).append(employee_n + ' ' + employee_s)
        else:
            dict_of_employees.get(employee_s[0])[employee_n[0]] = [employee_n + ' ' + employee_s]
    else:
        dict_of_employees[employee_s[0]] = {employee_n[0]: [employee_n + ' ' + employee_s]}
    print(dict(sorted(dict_of_employees.items())))
    return dict_of_employees


def user_input() -> None:
    name, surname = '', ''
    for line in iter(input, ''):
        name, surname = line.split()
    create_dict_employees(name, surname)


def main() -> None:
    """Main program."""
    user_input()


if __name__ == '__main__':
    main()
