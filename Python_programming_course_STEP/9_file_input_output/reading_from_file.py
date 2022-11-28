# open('file.txt) указывается путь к файлу, если  не указывается, то файл будет открываться для чтения
inf = open('file.txt', 'r')
s1 = inf.readline()
s2 = inf.readline()
print(f'{s1}, {s2}', end='')  # 2
# , 5 в первой строке считается символ переноса строки
inf.close()  # закрытие файла


# Специальная конструкция для чтения

with open('file.txt') as inf:  # закрывается самостоятельно
    s1 = inf.readline()
    s2 = inf.readline()
    print(f'{s1}, {s2}', end='')  # тут также
