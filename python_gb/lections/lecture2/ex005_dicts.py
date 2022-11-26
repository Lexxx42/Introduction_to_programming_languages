# Словари
# Неупорядоченные коллекции произвольных объектов с доступом по ключу

dictionary = {}
dictionary = \
    {
        'up': '↑',
        'left': '←',
        'right': '→',
        'down': '↓'
    }
print(dictionary)  # {'up': '↑', 'left': '←', 'right': '→', 'down': '↓'}
print(dictionary['left'])  # ←

for k in dictionary.keys():
    print(k, end=' ')  # up left right down
print()
for k in dictionary.values():
    print(k, end=' ')  # ↑ ← → ↓
print()
for k in dictionary:
    print(k, end=' ')  # up left right down
print()
for k in dictionary:
    print(dictionary[k], end=' ')  # ↑ ← → ↓
print()
for item in dictionary:
    print('{}: {}'.format(item, dictionary[item]), end=' ')  # up: ↑ left: ← right: → down: ↓
