""" The function takes arguments - the names of employees,
returns a dictionary. Keys are the first letters of names,
values are lists containing names starting with the corresponding letter. """


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


def create_dict(*args: str) -> dict:
    """Creation of a dictionary of employees."""
    dict_of_employees = {}
    for arg in args:
        if arg[0].upper() in dict_of_employees:
            dict_of_employees[arg[0].upper()].append(arg)
        else:
            dict_of_employees[arg[0].upper()] = [arg]
    print(dict(sorted(dict_of_employees.items())))
    return dict_of_employees


def main() -> None:
    """Main program."""
    create_dict("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка")


if __name__ == '__main__':
    main()
