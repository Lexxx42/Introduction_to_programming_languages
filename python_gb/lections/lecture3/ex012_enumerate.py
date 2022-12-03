# Функция enumerate() применяется к итерируемом объекту и возвращает новый итератор с кортежами из индекса и
# элементов входных данных.
print(list(enumerate(
    ['Kazan', 'Smolensk', 'Rybki', 'Chicago'])))  # [(0, 'Kazan'), (1, 'Smolensk'), (2, 'Rybki'), (3, 'Chicago')]

# Нельзя пройтись дважды
