# Запуск внешних процессов
# Модуль subprocess - вызов другой программы внутри одной программы
import subprocess

# subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)
# stderr=None - вывод ошибок, можно направить в файл
# Запускает программу в соответствии с аргументами (args).
# Дожидается выполнения и возвращает код возврата.
subprocess.call(["python", "-h"])
