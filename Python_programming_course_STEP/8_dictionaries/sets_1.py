# Множества

s = set()  # создание пустого множества
basket = {'apple', 'orange', 'apple', 'pear', 'orange',
          'banana'}  # Множество инициализированное значениями
print(basket)  # {'pear', 'apple', 'banana', 'orange'}

print('apple' in basket)  # True
print(123 in basket)  # False

# Операции с множествами
element = 'apple'
# Добавление в множество. Если в множество добавить элемент, которой уже есть в множестве, множество не изменится
basket.add(element)
print(basket)
# Удаление элемента из множества. Если элемента нет в множестве, то возникнет ошибка
basket.remove('apple')
print(basket)
# basket.remove('apple')
# print(basket)  # KeyError: 'apple'

basket.discard('orange')
print(basket)
basket.discard('orange')
print(basket)
basket.clear()  # Удалить все элементы множества
len(basket)  # Узнать число элементов в множестве

# Перебор элементов множества
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
for x in basket:
    print(f'{x} ', end='')

print()
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
for i, item in enumerate(basket):
    if i % 2 == 0:
        print(item, end=' ')
