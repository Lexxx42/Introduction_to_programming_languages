# Построчное чтение файла

with open('file.txt') as inf:
    for line in inf:
        line = line.strip()
        print(line)
