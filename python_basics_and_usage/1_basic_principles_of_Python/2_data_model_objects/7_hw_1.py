# Реализуйте программу, которая будет вычислять количество различных объектов в списке.
# Два объекта a и b считаются различными, если a is b равно False.

# Вашей программе доступна переменная с названием objects,
# которая ссылается на список, содержащий не более 100 объектов. Выведите количество различных объектов в этом списке.

# Формат ожидаемой программы:

# ans = 0
# for obj in objects: # доступная переменная objects
#     ans += 1

# print(ans)

# Примечание:
# Количеством различных объектов называется максимальный размер множества объектов, в котором любые два объекта являются различными.

# Рассмотрим пример:
# objects = [1, 2, 1, 2, 3] # будем считать, что одинаковые числа соответствуют одинаковым объектам, а различные – различным

# Тогда все различные объекты являют собой множество {1, 2, 3}﻿. Таким образом, количество различных объектов равно трём.


uniq_objects = set()

for obj in objects:
    uniq_objects.add(id(obj))
print(len(uniq_objects))


# В процессе решения данной задачи, вы в комментариях задали один очень интересный вопрос:
# почему внутри set 1 и True считаются одинаковыми элементами, в то время, как True is not 1.

# Ответ заключается в том, как в языке python устроены множества (сет) и словари (dict), а также, важная деталь про значения 1 и True.

# Прежде всего убедитесь в том, что 1 == True и True is not 1(запустите это в интерпретаторе)

# Объекты (коробки) ﻿действительно разные, однако оператор == будет возвращать значение True,
# равенство логических значений значениям 0 и 1 появилось в очень старые времена (во многих языках).

# Теперь проясним одну важную деталь языка python: чтобы узнать, лежит ли объект внутри множества (или ключей словаря)
# или нет, мы пользуемся hash и сравнением через == : https://docs.python.org/3/reference/datamodel.html#object.__hash__﻿

# Таким образом, раз 1 == True (и hash(1) == hash(True)) ﻿внутри множества эти объекты считаются одинаковыми,
# несмотря на то, что объекты различаются (так как 1 is not True).

# ﻿Похожим примером будет сравнение листов: вы можете убедиться, что [1, 2, 3] is not [1, 2, 3] однако [1, 2, 3] == [1, 2, 3]

# print(1 == True)  # True
# print(True is not 1)  # True
