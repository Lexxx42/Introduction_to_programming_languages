# Множества


colors = {'red', 'green', 'blue'}
print(type(colors))  # <class 'set'>

colors.add('red')
print(colors)  # {'red', 'green', 'blue'}

colors.add('white')
print(colors)  # {'red', 'green', 'blue', 'white'}

colors.remove('red')
print(colors)  # {'green', 'white', 'blue'}

# colors.remove('red') # KeyError: 'red'

colors.discard('red')  # Удаляет если есть, если нет то ок
print(colors)  # {'green', 'white', 'blue'}
colors.clear()  # Clear
print(colors)  # set()
