a = 7  # присваивание переменной значения
b = 3
print(a+b)
# новое значение
a = 6
print(a+b)
b = b+2
print(b)
# print(c)  ошибка с - переменная должна быть проинициализирована

a = 2
a += 3  # увеличиваем значение на 3
# += -= *= /= //= %= **=
# имя переменной
# может состоять из букв (строчных и прописных), цифр, подчеркивания _
# должно начинаться с буквы или подчеркивания
# не должно являться ключевым словом
# регистр букв имеет значение

# динамическая типизация
# a = 2
# a = 'asfdsadf'
# a = foo()
# type(a)=?

# в Python некорректно говорить, что какая-то переменная имеет какой-то конкретный тип
# можно говорить, что переменная имеет конкретный тип а конкретный момент выполнения программы
# когда переменная связана с каким-то конкретным объектом
# этим Python отличается от языков со статической типизацией, где тип переменной жестко фиксирован
