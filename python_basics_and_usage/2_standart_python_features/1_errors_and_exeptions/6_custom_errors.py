from termcolor import colored

print(colored("Это будет выводиться красным", 'red'))

# До данного момента мы с вами сталкивались только с ошибками, которые возникают в процессе
# исполнения стандартных операций. Например, деление на ноль.
# Однако, мы в праве сами решать, когда в нашей программе произошла ошибка, которую нужно
# как-нибудь обработать.

# Научились ошибки ловить, научимся их и бросать.
# Мы используем терминология английскую "бросать", потому что тема исключений далеко не новая,
# и использовались в других языках программирования.

# В англоязычной литературе вы будете постоянно встречать термины throw и catch - кидать и ловить.
# Для того чтобы бросить исключение в языке python необходимо использовать конструкцию rise.
# В которую нужно затем передать объект нашего исключения.

# def greet(name):
#     if name[0].isupper():
#         return "Hello, " + name
#     else:
#         raise ValueError(name + " is inappropriate name")
#
#
# # Идеологически ValueError в python используется ровно тогда, когда аргумент, который мы передали в функцию
# # по типу подходит, а по значению - нет.
#
# print(greet("Anton"))
# print(greet("anton"))
# Так же конструктор нашего класса ValueError принимает единственную строку, которая является
# сообщением дополнительным к этому исключению.

# Тогда, когда мы захотим передать Антону привет, мы вызовем функцию принт(грит(Антон)).
# Когда мы передадим "антон" с маленькой буквы, то мы получим ошибку:

# Traceback (most recent call last):
#   File "/home/lexx42/introduction/Introduction_to_programming_languages/python_basics_and_usage
#   /2_standart_python_features/1_errors_and_exeptions/6_custom_errors.py", line 27, in <module>
#     print(greet("anton"))
#           ^^^^^^^^^^^^^^
#   File "/home/lexx42/introduction/Introduction_to_programming_languages/python_basics_and_usage
#   /2_standart_python_features/1_errors_and_exeptions/6_custom_errors.py", line 23, in greet
#     raise ValueError(name + " is inappropriate name")
# ValueError: anton is inappropriate name

# Давайте тогда сами напишем с помощью данной функции такую программу, в которую мы бы представлялись.
# Если мы представились ей правильно, то она с нами здоровается.
# Если бы представились неправильно, то она бы пыталась попросить нас представится снова.

print('===')


# def greet(name):
#     if name[0].isupper():
#         return "Hello, " + name
#     else:
#         raise ValueError(name + " is inappropriate name")
#
#
# while True:
#     try:
#         name = input("What is your name? ")
#         print(greet(name))
#     except ValueError:
#         print("Try again")
#     else:
#         break


# Хочу заметить, что все исключения, которые мы бросаем с помощью rise, и все исключения,
# которые мы ловим с помощью except, должны быть прежде всего экземплярами класса BaseException.

# BaseException - это встроенный тип языка python, который описывает все исключения языка python.

# Давайте на секунду представим, что нет такого класса исключений, который бы хорошо описывал
# именно ту ошибку, которая происходит у вас в коде.
# Тогда имеет смысл написать свой собственный класс исключений именно для этой ситуации.
# Как бы мы это сделали?

# Пишем свой собственный класс

class BadName(Exception):
    pass


def greet(name):
    if name[0].isupper():
        return "Hello, " + name
    else:
        raise BadName(name + " is inappropriate name")


while True:
    try:
        name = input("What is your name? ")
        print(greet(name))
    except ValueError:
        print("Try again")
    else:
        break
# Таким образом, чтобы бросить исключение в языке python, вы должны использовать
# конструкцию rise.
# А если мы хотим написать свой собственный класс исключений, то мы должны использовать
# наследование от класса Exception.
