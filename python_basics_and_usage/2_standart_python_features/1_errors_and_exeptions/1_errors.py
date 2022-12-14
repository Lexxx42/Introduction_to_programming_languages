# С некоторыми ошибками мы уже встречались, допустим NameError, - это такая ошибка, которая встречается
# когда мы не можем найти имя в пространстве имен.
# Так же я уверен, что вы встречались с ошибками, когда пытались запустить тот или иной код
# у себя в интерпретаторе.

# Все ошибки в языке Python делятся на два типа:

# 1й тип ошибок языка Python - это ошибки синтаксические или Syntax errors, это когда мы даем
# какую-то конструкцию интерпретатору, а интерпретатор не может ее разобрать, потому что
# мы допустили в ней синтаксическую ошибку. Раз он не может ее разобрать, то не может ее исполнить.

# 2й тип ошибок - это те ошибки, которые уже возникают уже в процессе исполнения самого кода.
# Так называемые исключения.

# Давайте рассмотрим пример кода из прошлого модуля.

class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0


class MyList(list, EvenLengthMixin):
    pass


ml = MyList([1, 12, 4, 17])
ml.sort()
print(ml)

# Когда мы интерпретатором запускаем файл целиком, то интерпретатором проверяется файл целиком
# на синтаксические ошибки.
# Т.е. если в файле есть синтаксическая ошибка, тогда он не начнет свое исполнение.
# А если синтаксической ошибки нет, тогда он начнет исполнение строка за строкой.

# Чтобы в этом убедиться, добавим безобидную функцию принт() и снова совершим синтаксическую ошибку.

# Таким образом, синтаксические ошибки - это единственные ошибки, о которых мы можем узнать
# до исполнения самого кода.
# О всех остальных ошибках мы узнаем в процессе исполнения.

# Давайте совершим ошибку, о которой мы узнаем в процессе исполнения.

# ml = MyList([1, "ыыы", 4, 17])  # Поменяем одно число на строку
# TypeError: '<' not supported between instances of 'str' and 'int'
# ml.sort()
# print(ml)
# Получим ошибку типов, мы не можем сравнить для сортировки
# Мы целиком исполнили код до этой ошибки. И зачем приостановили свое исполнение,
# когда ошибка появилась.

# Ошибки встречаются часто и в очень важно их уметь исправлять.
# Для того чтобы уметь ошибки исправлять, нужно уметь читать сообщения об ошибках.

# У любой ошибки в языке Python есть три обязательные вещи:

# Прежде всего ошибки также являются объектами, поэтому у любой ошибки есть тип.
# Тип ошибки уже о многом нам говорит. Если мы встречаем TypeError, то мы вероятно передали
# в функцию что-нибудь неправильного типа. А если мы встречаем NameError, то мы вероятно попытались
# использовать переменную, которая еще не была определена.

# Так же у любой ошибки в языке python есть дополнительное сообщение, которое несет дополнительную информацию
# и часто может нам помочь понять что же пошло не так.

# И третья обязательная вещь, которую хранит в себе ошибка - это состояние стека вызовов на тот момент,
# когда у нас совершилась ошибка.

# Давайте научимся читать ошибки и запустим следующий код
print("****")


# x = [1, 2, 3]
# print(x[4])
# Чтобы убедиться, что запоминается стек, мы обернем код в функцию и вызовем ее.

def f():
    x = [1, 2, 3]
    print(x[4])


f()
# Traceback (most recent call last):
#   File "C:\Users\Konuhov\Desktop\intro\Introduction_to_programming_languages\python_basics_and_usage
#   \2_standart_python_features\1_errors_and_exeptions\1_errors.py", line 80, in <module>
#     f()
#   File "C:\Users\Konuhov\Desktop\intro\Introduction_to_programming_languages\
#   python_basics_and_usage\2_standart_python_features\1_errors_and_exeptions\1_errors.py", line 77, in f
#     print(x[4])
#           ~^^^
# IndexError: list index out of range

# Развернутый стек вызовов. На 80 строке мы вызвали функцию ф() в модуле
# Ошибка возникла на 77 строке внутри этой функции.

# Таким образом, ошибки нужны, чтобы сообщить нам, что в нашем коде произошло что-то такое
# из-за чего мы больше не можем продолжить исполнение данного кода.

# А текущее состояние стека вызовов, тип ошибки и дополнительное сообщение нужны для того,
# чтобы сказать где именно это произошло, и что именно у нас произошло.
