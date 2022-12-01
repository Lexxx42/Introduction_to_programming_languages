# В какой-то момент в Институте биоинформатики биологи перестали понимать, что говорят информатики:
# они говорили каким-то странным набором звуков.
#
# В какой-то момент один из биологов раскрыл секрет информатиков:
# они использовали при общении подстановочный шифр, т.е.
# заменяли каждый символ исходного сообщения на соответствующий ему другой символ.
# Биологи раздобыли ключ к шифру и теперь нуждаются в помощи:
#
# Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки.
# Программа принимает на вход две строки одинаковой длины,
# на первой строке записаны символы исходного алфавита,
# на второй строке — символы конечного алфавита, после чего идёт строка,
# которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно расшифровать.
#
# Пусть, например, на вход программе передано:
# abcd
# *d%#
# abacabadaba
# #*%*d*%
#
# Это значит, что символ a исходного сообщения заменяется
# на символ * в шифре, b заменяется на d, c — на % и d — на #.
# Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра.
#
# Получаем следующие строки, которые и передаём на вывод программы:
# *d*%*d*#*d*
# dacabac
#
# Sample Input 1:
#
# abcd
# *d%#
# abacabadaba
# #*%*d*%
# Sample Output 1:
#
# *d*%*d*#*d*
# dacabac
# Sample Input 2:
#
# dcba
# badc
# dcba
# badc
# Sample Output 2:
#
# badc
# dcba


input_alphabet = input()
output_alphabet = input()
encode_line = input()
decode_line = input()

encode_dict = {}
decode_dict = {}
for i in range(len(input_alphabet)):
    encode_dict[input_alphabet[i]] = output_alphabet[i]

for j in range(len(input_alphabet)):
    decode_dict[output_alphabet[j]] = input_alphabet[j]

for position, item in enumerate(encode_line):
    if item in encode_dict:
        encode_line = encode_line[:position] + encode_dict[item] + encode_line[position + 1:]
print(encode_line)

for position, item in enumerate(decode_line):
    if item in decode_dict:
        decode_line = decode_line[:position] + decode_dict[item] + decode_line[position + 1:]
print(decode_line)
