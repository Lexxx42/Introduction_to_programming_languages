genome = 'ATGG'

print(len(genome))

for i in range(len(genome)):
    print(f'{genome[i]} ', end='')

# genome[0] = A genome[-1] = G
# genome[1] = T genome[-2] = G
# genome[2] = G genome[-3] = T
# genome[3] = G genome[-4] = A

# genome[1] = 'C' - elements of str can't be changed like this!
# print(genome)

print('\n')
for c in genome:
    print(f'{c } ', end='')
print('\n')


# задача
# Дана геномная последовательность.
# Вывести сколько раз в ней встречается
# нуктеотид цитозин.
# входные данные 1: CACCTGGAC
# выходные данные 1: 4
# входные данные 2: GATTACA
# выходные данные 2: 1

# my
count = 0
genome = 'CACCTGGAC'
for c in genome:
    if c == 'C':
        count += 1
print(count)

# class
# same..

genome = 'CACCTGGAC'
print(genome.count('C'))
# Строки имеют методы
# функция, которая применяется к данной строке
# s.count(p) - сколько раз строка p встречается в строке s


genome = 'Дана геномная последовательность.'
print(genome.count('на'))
