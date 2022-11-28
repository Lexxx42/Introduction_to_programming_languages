# Убрать все служебные символы при чтении строки
import os


with open('file.txt') as inf:  # закрывается самостоятельно
    s1 = inf.readline().strip()
    s2 = inf.readline().strip()
    s = int(s1)+int(s2)
    print(f'{s1}, {s2}, {s}', end='')  # тут также

print('\n')
a = '\t abc \n'  #          abc + перенос
print(a)
print('\t abc \n'.strip())  # abc


# Распечатать путь к файлу
path = os.path.join('.', 'dirname', 'filename.txt')
                    #/    directory   filename
print(path)

# with open('file.txt') as inf:  # закрывается самостоятельно
    


