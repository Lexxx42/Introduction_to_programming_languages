
text = "Тестирование продукта→обнаружение ошибок→анализ ошибок 111"

old_char = '→'
new_char = '@'
text = text.replace(old_char, new_char)
print(text)


line = 'Если в строке есть символ "!", то заменить все символы после первого "!" на символ "*"'
index = line.find("!")

if index == -1:
    print('Символа "!" нет в строке, вывести об этом сообщение.')
else:
    line = line[0:index+1] + "*" * len(line[index+1:])
    print(f'line = {line}')


line = '!Hello World'
index = line.find("!")

if index == -1:
    print('\nСимвола "!" нет в строке, вывести об этом сообщение.')
else:
    line = line[0:index+1] + "*" * len(line[index+1:])
    print(f'line = {line}')
