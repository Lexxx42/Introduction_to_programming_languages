# Также в языке python мы можем импортировать не весь модуль целиком, а лишь какие-то имена из него.
# Для этого мы можем использовать конструкцию from import.

# Т.е. если мы хотели импортировать только наше исключение BadName из модуля for_import
from for_import import BadName, greet as ext_greet
import for_import as exc

# from for_import import *

print(exc)


# Так как с процессом импорта модуля или имени из модуля связано создание локального имени в
# локальном неймспейсе, то можем явно указать то локальное имя, которое мы бы хотели использовать.

# Для этого мы можем использовать конструкцию as.

def greet():
    print("Hey!")


# Допустим нам необходимо использовать две функции greet()
# из локального неймспейса и импортированную.

greet()
print(ext_greet("Student"))
# Таким же образом можно импортировать целый модуль и использовать для него новое локальное имя.

# Так же в языке python, используя синтаксис from, вы можете импортировать все имена из какого-либо модуля.
# Для этого достаточно использовать *
# Однако такая практика является не самой рекомендуемой, потому что если модуль большой, в нем слишком
# много имен, то наверняка какие-то из этих имен могут пересекаться с теми, которые
# вы используете.

# Таким образом, чтобы импортировать все имена from for_import import *

# Однако через звездочку мы будем импортировать далеко не все имена.
# Прежде всего, мы можем определить такую конструкцию __all__, в которую мы
# определим все имена, которые мы можем импортировать с помощью *.

# И даже если мы эту конструкцию не определим, то тогда мы не будем импортировать имена, которые
# начинаются с нижнего подчеркивания.

# При отсутствии конструкции __all__ и наличии импорта со *
# print(_SECOND_GREETING) - не будет выводиться, т.к. начинается с нижнего подчеркивания
# print(GREETING) - будет импортировано

# Таким образом в языке python существуют удобные механизмы для того чтобы
# выбирать локальные имена для импортированных модулей и имен внутри модулей.

# Так же мы можем импортировать все имена из модуля, однако с этим следует быть
# более аккуратным, а также мы можем контролировать, какие имена
# будут импортированы, если наш модуль импортируют с помощью *.
