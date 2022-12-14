# Давайте разбираться как устроена система импорта в языке python.

# Дело в том, что мы действительно будем исполнять код, когда будем импортировать модуль, однако
# мы будем это делать лишь единожды.
# Т.е. если у нас есть активная сессия интерпретатора, мы например исполняем импорт exceptions,
# тогда мы действительно исполним код нашего модуля exceptions и все глобальные имена,
# которые остались внутри данного неймспейса, мы закрепим за нашим объектом модулем.

# А если мы второй раз напишем import exceptions, то мы уже переиспользуем старый объект для нашего модуля.

# Прежде всего стоит отметить, что у нас есть такой объект, который называется sys.modules
# и он обычный словарь.

# Ключами у него являются имена наших модулей, а значения - model objects.

# Когда мы пишем: import exceptions
# Первое, что он делает он спрашивает у словаря sys.modules (dict) есть ли в нем ключ "exceptions".
# Потому что это имя нашего модуля. Он спрашивает: есть ли у тебя заимпортированный модуль exceptions?
# Он отвечает, что нет. И тогда происходит исполнение нашего модуля exceptions.
# И для него мы создаем module object и затем мы обновляем наш словарь и помещаем по ключу
# "exceptions" наш module object.

# Когда мы в следующий раз попробуем в нашем коде импортировать exceptions, то он так же обратится
# к нашему словарю и спросит, есть ли там ключ "exceptions" - есть. И нам вернется в качестве
# нашего модуля уже существующий module object.

# На самом деле все это можно и нужно попробовать. Потому что до данного словаря можно достучаться.
# Давайте это сделаем.
import sys

print(type(sys.modules))
print(sys.modules)
import check

print(sys.modules)
print(type(check))
print(id(check))
import check

print(type(check))
print(id(check))
# Таким образом, любой модуль в языке python будет исполнен лишь единожды несмотря на то,
# что внутри нашего кода мы могли импортировать его несколько раз.

# Однако осталась одна важная нерассмотренная деталь.
# А как же мы ищем имя модуля, если мы не нашли его в sys.modules?

# Ответ на самом деле достаточно простой: если мы не нашли какое-то имя модуля
# в нашем sys.modules, то мы попробуем найти файлик с расширением .py в текущей директории.
# Если мы не нашли его здесь, то тогда мы пойдем его искать во внешней библиотеке.

# Для того чтобы узнать в каком именно порядке это будет происходить мы можем перебрать все пути в
# списке sys.path.
print("+++\n")

for path in sys.path:
    print(path)

# Как можно заметить, все модули во внешних библиотеках представлены папками.
# Эти папки мы называем пакетами.

# Пакет - это такой удобный способ представления некоторого числа файлов в качестве одного модуля.

# В рамках данного урока мы не будем останавливаться на том, как устроены пакеты.
# Однако, если вы будете писать какую-нибудь свою библиотеку, вы обязательно в этом разберетесь.
# Для нас важно то, что по сути пакеты - это такие папки, которые могут вести себя как модули,
# которые мы тоже можем импортировать.

# Интерпретатор умеет определять по папке является ли она пакем по наличию файла __init__ внутри.
# Если внутри находится файл __инит__, то он исполняется при импорте.

# Таким образом, у нас есть модули и пакеты, которые ведут себя как модули.
# Мы можем их импортировать и тогда мы исполняем код внутри модуля, однако мы делаем
# это лишь в первый раз, когда импортируем модуль.
# Потому что затем мы можем найти имя модуля, как ключ в словаре sys.modules и
# понять, что его импортировать больше не нужно и просто вернуть уже готовый объект нашего модуля.
