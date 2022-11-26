# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')  # если использовать w то произойдет перезапись
# # data.writelines(colors)  # разделителей не будет
# data.write('LINE 121\n')
# data.write('LINE 131\n')
# data.close()

# with open('file.txt', 'w') as data:  # ручное закрытие файла не нужно
#     data.write('line 1\n')
#     data.write('line 2\n')
#


path = 'file.txt'  # Все что хранится в тексте является строкой, чтобы работать с числами их надо конвертировать в int
data = open(path, 'r')
for line in data:
    print(line)
data.close()

exit()  # все что ниже не использвуется
