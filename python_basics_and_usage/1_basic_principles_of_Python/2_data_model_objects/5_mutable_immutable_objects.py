# У любого объекта есть значение и важно понимать какие значения могут принимать объекты того
# или иного типа
# Если объект может изменять значение в течении своей жизни, мы называем его изменяемым объектом
# или mutable
# Если не меняет значение в течении своей жизни мы называем его неизменяемым immutable
 
# Возможность объекта изменять свое значение чаще всего зависит лишь от типа объекта

# Необходимо понимать какие типы объектов в Python являются изменяемыми и не изменяемыми
# Не изменяемые: 

# 1. числа (сам объект при присвоении ему нового значения не изменялся) -> все операции и функции, 
# которые работают с числами не будут изменять сам объект, а будут возвращать (чаще всего) новые объекты
# int, float, complex

# 2. Логический тип bool. 2 значения True и False, интерперетатор этим экономно пользуется.
# В любой момент времени в оперативной памяти представлено всего 2 объекта логического типа
# Поэтому в любой момент времени любой объект логического типа, который у нас используется
# ссылается на один из этих двух
x = [1,2,3]
print(4 in x)  # False
# Такая оптимизация позволяет нам не хранить в оперативной памяти огромное число логических объектов
# Однако, такая оптимизация возможна лишь тогда, когда bool является неизменяемым типом данных

# 3. Кортеж tuple

# 4. строки str

# 5. неизменяемое множество frozenset

# Изменяемые: 

# 1. Список list
# Чтобы понять почему список является изменяемым типом, а кортеж не является изменяемым
# нужно понять, что же является значением списка
x = [1,2,3]
# в оперативной памяти хранятся объекты: 1, 2, 3, и есть объект для списка х [. , . , . ]
# значения списка - это упорядоченное множество ссылок на объекты
# [ссылка на 1, ссылка на 2, ссылка на 3]
# Мы можем изменить последовательность ссылок - отличительная особенность от кортежей
# можем дописать в конец ссылку на другой объект 4
x.append(4)
# Можем поменять ссылки местами, отсортировать в определенном порядке
# кортеж не меняется до конца жизни объекта, его нельзя изменять

# 2. Словари dict Можем изменить значение по ключу, можем добавить новую пару ключ: значение
# Можем избавится от пары ключ: значение

# 3. Множество set, можем добавлять и удалять из него элементы
# У множества есть неизменяемая версия


# Подытожим: всегда стоит помнить, какие типы данных являются изменяемыми, а какие не изменяемыми
# держать в голове, если несколько переменных ссылаются на один и тот же объект изменяемого типа
# это значит, что изменение какой-либо переменной, которая ссылается на этот объект
# изменит объект и как следствие все переменные, которые на него ссылаются
# стандартных изменяемых типа данных всего 3: list, dict, set.
# Нужно быть аккуратным, когда используешь данные типы!
