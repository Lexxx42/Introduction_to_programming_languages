# Модули

# Модуль содержит функции и данные в отдельном файле.
# Объекты из модуля можно импортировать в другие модули.
# Имя файла = имя модуля + .py

# Импорт модуля
# Рассмотрим файл my_module.py
# Пусть в нем описана функция foo()

import my_module
my_module.foo()

# Другие способы импорта

# from my_module import foo  # импорт явно 1й функции
# foo()

# from my_module import *  # Импорт всех функций из модуля
# foo()

# from my_module import foo as my_foo
# my_foo()
