x = 0
y = 0


# модуль, который отвечает за инициализацию двух переменных
def init(a, b):
    global x
    global y
    x = a
    y = b


# модуль, который отвечает за вычитание
def do_it():
    return x - y
